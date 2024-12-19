**Autor: João Pedro Costa**

# Passo-a-Passo para Criar uma Aplicação Web

## 1. Crie um Diretório

Antes de começar a criar sua aplicação web, é importante organizar os arquivos em um diretório específico.

## 2. Crie o Ambiente Virtual

Para criar um ambiente virtual, utilize o comando abaixo:

<p style="text-align: center; font-size: 18px;">
  <code>python3 -m venv venv</code>
</p>

Com este comando, estamos pedindo ao **Python** para executar o pacote `venv`, que cria um ambiente virtual chamado `venv`. O primeiro `venv` no comando refere-se ao pacote do ambiente virtual, enquanto o segundo `venv` é o nome do ambiente que você está criando. 

Se achar isso confuso, você pode substituir o segundo `venv` por outro nome à sua escolha para o ambiente virtual.

## 3. Ativando o Ambiente Virtual

Após criar o ambiente virtual, é necessário ativá-lo para começar a utilizá-lo. Para isso, utilize o comando:

<p style="text-align: center; font-size: 18px;">
  <code>source venv/bin/activate</code>
</p>

Agora, seu ambiente virtual estará ativo e você poderá instalar pacotes e bibliotecas isoladamente para a sua aplicação.

Para saber que o ambiente está ativo, o prompt ficará da seguinte forma:

<p style="text-align: center; font-size: 18px;">
  <code>(venv) $(nomedousuario):Local_do_repositório</code>
</p>

## 4. Instalando Bibliotecas no Ambiente Virtual

Agora você está pronto para instalar bibliotecas. Você pode fazer da seguinte forma:

<p style="text-align: center; font-size: 18px;">
  <code>pip install flask</code>
</p>

## 5. Criando uma Aplicação

Para criar a aplicação é necessário criar um arquivo **.py** que hospedará o aplicativo. Note que o arquivo **não** pode estar na pasta `venv`, e sim em outra pasta que pode ser a pasta em que **venv** está dentro.

Ex:
```
\codigo
  \app.py
\venv
```

`Obs.:É costume chamar o aplicativo de app.py`

## 6. Criar arquivo requirements
O arquivo requirements.txt serve para listar todas as dependências externas que sua aplicação precisa para rodar corretamente. Quando você cria o ambiente virtual (geralmente com o comando python -m venv venv), você instala bibliotecas dentro dele, e o arquivo requirements.txt mantém um registro dessas dependências.

Para criar o requirements.txt, você pode rodar o seguinte comando dentro da pasta onde está o seu ambiente virtual e o seu arquivo app.py:

`pip freeze > requirements.txt`

## 7. Instalando dependências

Após criar o requirements.txt, qualquer outra pessoa que for rodar o seu projeto pode instalar as dependências de uma maneira simples com o comando:

`pip install -r requirements.txt`

## Resumo
- Criar diretório.
- Crie o ambiente virtual.
- Ativar ambiente virtual.
- Criar a pasta `app/` (fora do ambiente virtual venv/).
- Criar o arquivo `app.py` dentro da pasta `app/` com o código da aplicação.
- Criar o arquivo `requirements.txt` listando as dependências, que pode ser feito com o comando `pip freeze > requirements.txt`.
- Instalar as dependências com `pip install -r requirements.txt`.