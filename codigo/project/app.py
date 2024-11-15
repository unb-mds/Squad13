from flask import Flask, render_template
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
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    values = [200, 300, 400, 500, 600]
    
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    fig.update_layout(title='Gastos Mensais')

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
    ]
    return render_template('tables.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
