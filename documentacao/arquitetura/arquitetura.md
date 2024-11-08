# **Arquitetura do Projeto**

![Diagrama de Arquitetura](../assets/DiagramaArquitetura.png)

## **Introdução**

### Propósito
O propósito deste projeto é descrever a arquitetura de software do projeto **Esquadrão 13**, uma iniciativa que visa promover a transparência na gestão dos gastos públicos no Distrito Federal.

### Objetivo
O objetivo principal do projeto é desenvolver uma plataforma que permita o monitoramento e análise de gastos públicos, facilitando o acesso à informação e promovendo a transparência para os cidadãos do Distrito Federal.

### Definições, Acrônimos e Abreviações
- **API**: Application Programming Interface (Interface de Programação de Aplicações).
- **PTGF**: Portal da Transparência do Governo Federal.
- **MVC**: Model-View-Controller (Modelo-Visão-Controlador).

## **Tecnologias Escolhidas**

| Tecnologia     | Versão      |
|----------------|-------------|
| Python         | 3.13.0      |
| Flask          | 3.0.3       |
| HTML           | HTML5       |
| CSS            | CSS3        |
| GitHub Pages   | -           |

## **Visão dos Componentes**

### **Model-View-Controller (MVC)**
O projeto será desenvolvido utilizando a arquitetura **MVC** (Model-View-Controller). A separação em camadas facilita a manutenção, escalabilidade e a organização do código.

#### **Model**
A camada **Model** é responsável por gerenciar os dados do sistema e implementar as regras de negócios. Ela faz a comunicação com a base de dados e com fontes externas, como APIs, para garantir que os dados corretos sejam processados e disponibilizados.

#### **View**
A camada **View** é responsável pela apresentação dos dados ao usuário final. A interface gráfica será construída utilizando **HTML** e **CSS**, garantindo que o usuário tenha uma experiência visual agradável e acessível.

#### **Controller**
O **Controller** atua como intermediário entre a **Model** e a **View**. Ele recebe as ações do usuário, processa essas ações de acordo com as regras de negócios e atualiza a **View** com os resultados. O **Controller** também faz a mediação entre o **front-end** e o **back-end**, garantindo que os dados corretos sejam exibidos.

#### **Outros Componentes**
Além das camadas principais do modelo **MVC**, o projeto inclui componentes adicionais, como arquivos de configuração para o **Flask** e **Python**, variáveis de ambiente, chaves de **API** e bibliotecas externas para manipulação e visualização dos dados.

### **Front-end**
O **front-end** será desenvolvido utilizando **HTML**, **CSS** e **Python** para interatividade. A interface será otimizada para facilitar a navegação e a compreensão dos dados relacionados aos gastos públicos.

### **Back-end**
O **back-end** será desenvolvido em **Python**, utilizando o **Flask** como framework para construção da API. O **Flask** permitirá a criação de rotas e a manipulação de dados de forma eficiente e escalável, servindo de ponte entre o **back-end** e o **front-end**.

#### **Interação com Sistemas Externos**
O sistema será integrado com a **API** do **PTGF**, permitindo que os dados sobre os gastos públicos sejam obtidos diretamente do Portal da Transparência do Governo Federal.

##### **Coleta de Dados**
A coleta de dados será feita por meio da **API** do **PTGF**, que disponibiliza informações detalhadas sobre os gastos públicos. O sistema filtrará esses dados para focar nos gastos específicos relacionados ao Distrito Federal, permitindo que a plataforma forneça informações precisas e relevantes para a análise.

#### **Modelagem de Dados**
- **Valores dos Gastos Públicos**: Os dados serão disponibilizados mensalmente e anualmente, permitindo uma análise temporal dos gastos.
- **Órgãos**: Os dados serão organizados e apresentados separadamente por órgão público, para facilitar a visualização dos gastos específicos de cada instituição.
- **Análises e relatórios gráficos**: A implementação de ferramentas de visualização de dados (como gráficos e dashboards) pode melhorar a interpretação das informações.

O sistema irá incluir métricas e indicadores de fácil compreensão, ajudando o usuário a realizar uma análise aprofundada dos gastos públicos, com base nos critérios de interesse.