# Guia de Uso do MkDocs

Este é um guia completo para começar a usar o **MkDocs** e criar documentação de forma simples e eficiente utilizando **Markdown**.

## Introdução

O **MkDocs** é uma ferramenta de documentação de código aberto que permite criar sites estáticos de forma rápida e fácil. Ele utiliza **Markdown** para criar conteúdo e oferece uma interface de configuração simples.

## Instalação

Para instalar o MkDocs, basta ter o Python e o `pip` instalados em sua máquina. Siga os passos abaixo:

1. Instale o MkDocs com o seguinte comando:

```
pip install mkdocs
```
2. Instale o MkDocs Material com o seguinte comando:
```
pip install mkdocs-material
```
3. Inicie um novo projeto MkDocs com o comando:
```
mkdocs new .
```

4. Esse comando criará a estrutura básica de diretórios e arquivos do projeto. O diretório do seu projeto agora conterá os seguintes arquivos e pastas:

```
projeto/
├── docs/
│   └── index.md
├── mkdocs.yml
```

5. Detalhamento da Estrutura:
```
docs/: Este diretório contém todos os arquivos Markdown que compõem a documentação. O arquivo principal, index.md, é a página inicial do seu site de documentação.
```
```
mkdocs.yml: Este é o arquivo de configuração do MkDocs. Nele, você define as configurações do projeto, como o título do site, o tema utilizado e a navegação entre as páginas.
```

6. Configurando o projeto:

O arquivo mkdocs.yml é onde você configura as propriedades principais do seu projeto. Aqui estão alguns exemplos de configurações comuns:
```
site_name: Minha Documentação
theme: material
nav:
  - Home: index.md
  - Guia de Instalação: instalacao.md
  - FAQ: faq.md

```
- site_name: Define o nome do site de documentação.
- theme: Especifica o tema que será usado. O MkDocs oferece o tema padrão e outros como o Material.
- nav: Define a navegação do site, ou seja, a estrutura de links entre as páginas da documentação.

7. Adicionando mais paginas:
```
nav:
  - Home: index.md
  - Guia de Instalação: instalacao.md
  - FAQ: faq.md
  - Tutorial: tutorial.md
```

8. Servindo o Projeto Localmente:

Use o comando:
```
mkdocs serve
```
9. Gerando o Site Estático:
```
mkdocs build
```
Esse comando criará uma pasta chamada `site` com os arquivos necessários para a elaboração do site.

10. Publique/Atualize o site na branch gh-pages:

Para publicar ou atualizar o `site`, basta copiar a pasta site criada pela build e colá-la na raiz da branch `gh-pages`. No entanto, para isso, deve-se fazer um PR indicando a intenção.

#### Extra.

O MkDocs utiliza o tema Material for MkDocs ou outros temas e permite que você personalize o estilo da documentação utilizando CSS. Com o CSS, é possível alterar a aparência da sua documentação, como cores, fontes, espaçamento e muito mais. O arquivo CSS pode ser encontrado em: `mkdocs/docs/style/style.css`.
