from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly
import json
import random

app = Flask(__name__)

# Página de introdução
@app.route('/')
def index():
    return render_template('index.html')

# Página de gráficos
@app.route('/charts')
def charts():
    # Dados e configuração do gráfico com Plotly
    labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
    values = [200, 300, 400, 500, 600]
    
    # Configuração do gráfico com título em português e layout padrão
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])

    # Ajuste no layout para manter o estilo original
    fig.update_layout(
        title='Gastos Mensais',  
        title_x=0.5,  

    )

    # Convertendo o gráfico para JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('charts.html', graphJSON=graphJSON)

# Página de tabelas
@app.route('/tables')
def tables():
    # Exemplo de dados para a tabela
    data = [
        {'name': 'Alice', 'expense': 230},
        {'name': 'Bob', 'expense': 150},
        {'name': 'Charlie', 'expense': 320},
        {'name': 'Daniel', 'expense': 500},
        {'name': 'Eva', 'expense': 450},
        {'name': 'Frank', 'expense': 300},
        {'name': 'Grace', 'expense': 350},
    ]
    
    search_query = request.args.get('search')
    if search_query:
        data = [item for item in data if search_query.lower() in item['name'].lower()]

    # Obtemos os parâmetros de ordenação da URL
    sort_by = request.args.get('sort', 'name')  # Se não houver, ordena por 'name' por padrão
    sort_order = request.args.get('sort_order', 'asc')  # A ordem padrão é 'asc' (crescente)

    # Ordenar a lista de acordo com o parâmetro de ordenação e a direção
    reverse = True if sort_order == 'desc' else False
    data.sort(key=lambda x: x[sort_by], reverse=reverse)

    return render_template('tables.html', data=data, search_query=search_query, sort_by=sort_by, sort_order=sort_order)
if __name__ == '__main__':
    app.run(debug=True)
