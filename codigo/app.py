import os
import json
from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly
import requests
import re
from PyPDF2 import PdfReader

app = Flask(__name__)

#Caminho para o arquivo que armazena os dados
CACHE_FILE = "somas_mensais.json"

#Buscar dados da API
def buscar_dados_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#Baixar o arquivo PDF ou o extra TXT
def baixar_arquivo(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

#Extrair texto de um PDF
def extrair_texto_pdf(pdf_content):
    try:
        with open("temp.pdf", "wb") as f:
            f.write(pdf_content)
        reader = PdfReader("temp.pdf")
        texto = ""
        for pagina in reader.pages:
            texto += pagina.extract_text()
        return texto
    except Exception as e:
        return ""

#Buscar todos os valores em reais (R$)
def buscar_valores_em_reais(texto):
    padrao = r"R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}"
    return re.findall(padrao, texto)

#Converter valores para float
def converter_para_float(valor):
    valor = valor.replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(valor)

#Processar a API e retornar a soma dos valores por mês
def processar_gazettes(api_url):
    dados = buscar_dados_api(api_url)
    if not dados:
        return [], []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    soma_mensal = [0] * len(meses)
    for gazette in dados.get("gazettes", []):
        texto = ""
        if gazette.get("url"):
            pdf_content = baixar_arquivo(gazette["url"])
            if pdf_content:
                texto += extrair_texto_pdf(pdf_content)
        if gazette.get("txt_url"):
            txt_content = baixar_arquivo(gazette["txt_url"])
            if txt_content:
                texto += txt_content.decode("utf-8", errors="ignore")
        valores = buscar_valores_em_reais(texto)
        if valores:
            valores_convertidos = [converter_para_float(valor) for valor in valores]
            soma_diario = sum(valores_convertidos)

            #Determina o mes a partir da data
            mes = gazette['date'][5:7]
            mes_index = int(mes) - 1
            if 0 <= mes_index < len(meses):
                soma_mensal[mes_index] += soma_diario

    #Salvar os resultados em um arquivo json
    with open(CACHE_FILE, "w") as f:
        json.dump({"meses": meses, "soma_mensal": soma_mensal}, f)
    return meses, soma_mensal

#Carregar os dados do cache, se existir
def carregar_dados_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            dados = json.load(f)
            return dados["meses"], dados["soma_mensal"]
    return None, None

#Pré-processamento (Basicamente checa se o json existe com os dados, se nao existir ele faz uma busca na api)
def preprocessar_dados():
    meses, soma_mensal = carregar_dados_cache()
    if not meses or not soma_mensal:
        api_url = "https://queridodiario.ok.org.br/api/gazettes?territory_ids=5300108&published_since=2024-01-01&querystring=despesas&size=500&sort_by=relevance"
        meses, soma_mensal = processar_gazettes(api_url)

    return meses, soma_mensal
meses, soma_mensal = preprocessar_dados()

#Página de gráficos
@app.route('/charts')
def charts():
    #Cria gráfico com os meses e valores.
    fig = go.Figure(data=[go.Bar(x=meses, y=soma_mensal)])
    fig.update_layout(
        title='Gastos Mensais',
        title_x=0.5,
    )
    #Convertendo o gráfico para JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON, meses=meses, soma_mensal=soma_mensal)

#Pagina de introdução
@app.route('/')
def index():
    return render_template('index.html')

#Mapear mes a um numero.
meses_map = {
    "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
    "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
}

#Pagina de tabelas
@app.route('/tables')
def tables():
    #Combinar meses e soma_mensal em um único conjunto de dados
    data = list(zip(meses, soma_mensal))
    
    #Organizar os dados em uma lista de dicionários
    table_data = [{'mes': mes, 'gasto': gasto} for mes, gasto in data]
    
    #Filtrando a busca
    search_query = request.args.get('search')
    if search_query:
        table_data = [item for item in table_data if search_query.lower() in item['mes'].lower()]

    #Ordenação
    sort_by = request.args.get('sort', 'mes')
    sort_order = request.args.get('sort_order', 'asc')
    reverse = True if sort_order == 'desc' else False
    if sort_by == 'mes':
        #Ordena os meses
        table_data.sort(key=lambda x: meses_map[x['mes']], reverse=reverse)
    elif sort_by == 'gasto':
        #Ordena os gastos
        table_data.sort(key=lambda x: x['gasto'], reverse=reverse)
    return render_template('tables.html', data=table_data, search_query=search_query, sort_by=sort_by, sort_order=sort_order)
if __name__ == '__main__':
    app.run(debug=True)