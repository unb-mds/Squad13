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
    return render_template('tables.html')
if __name__ == '__main__':
    app.run(debug=True)
