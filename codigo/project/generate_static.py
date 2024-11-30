import os
from flask import Flask, render_template

# Inicializar o app Flask
app = Flask(__name__)

# Configurar o diretório de saída para arquivos estáticos
OUTPUT_DIR = "docs"
STATIC_DIR = os.path.join(app.root_path, 'static')

# Função para garantir que o diretório de saída existe
def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

# Função para salvar arquivos estáticos
def copy_static_files():
    output_static_dir = os.path.join(OUTPUT_DIR, 'static')
    if os.path.exists(output_static_dir):
        return  # Evitar recriar se já estiver configurado

    os.system(f'cp -r {STATIC_DIR} {OUTPUT_DIR}')

# Rotas de renderização de templates
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

# Função para gerar arquivos HTML
def generate_static_pages():
    print("Gerando páginas estáticas...")

    # Renderizar e salvar cada página
    with app.test_request_context():
        pages = {
            "index.html": index(),
            "base.html": base(),
            "charts.html": charts(),
            "tables.html": tables(),
        }

        for filename, content in pages.items():
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                print(f"Página gerada: {filepath}")

# Executar o processo de geração
if __name__ == "__main__":
    ensure_output_dir()
    copy_static_files()
    generate_static_pages()
    print("Páginas estáticas geradas com sucesso!")
