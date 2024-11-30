import os
from flask import Flask, render_template
import shutil

# Criação da aplicação Flask
app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost'  # Define um nome de servidor padrão (opcional)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

def generate_static():
    """Gera os arquivos estáticos para o GitHub Pages."""
    output_folder = 'docs'

    # Remove o diretório existente para evitar arquivos obsoletos
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    try:
        # Cria o contexto da aplicação e de uma requisição
        with app.app_context():
            with app.test_request_context():
                # Renderiza e salva cada página estática
                for page in ['index', 'charts', 'tables']:
                    with open(os.path.join(output_folder, f'{page}.html'), 'w') as f:
                        f.write(render_template(f'{page}.html'))

                # Copia os arquivos estáticos (CSS, JS, imagens)
                static_folder = os.path.join(output_folder, 'static')
                shutil.copytree('static', static_folder, dirs_exist_ok=True)

        print("Arquivos estáticos gerados com sucesso.")

    except Exception as e:
        print(f"Erro ao gerar os arquivos estáticos: {e}")

if __name__ == '__main__':
    generate_static()
