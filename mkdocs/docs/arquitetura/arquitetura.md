# **Arquitetura do Projeto**

![Diagrama de Arquitetura](../assets/DiagramaArquitetura.png)

## **Introdução**

### Propósito

O propósito deste projeto é descrever a arquitetura de software do projeto **Gastos-DF-2024-02**, uma iniciativa que visa promover a transparência na gestão dos gastos públicos no Distrito Federal.

### Objetivo

O objetivo principal do projeto é desenvolver uma plataforma que permita o monitoramento e análise de gastos públicos, facilitando o acesso à informação e promovendo a transparência para os cidadãos do Distrito Federal.

### Definições, Acrônimos e Abreviações

- **API**: Application Programming Interface (Interface de Programação de Aplicações).
- **PTGF**: Portal da Transparência do Governo Federal.
- **MVC**: Model-View-Controller (Modelo-Visão-Controlador).

## **Tecnologias Escolhidas**

| Tecnologia   | Versão |
| ------------ | ------ |
| Python       | 3.13.0 |
| Flask        | 3.0.3  |
| HTML         | HTML5  |
| CSS          | CSS3   |
| GitHub Pages | -      |

## **Visão dos Componentes**

### **Front-end**

O **front-end** será desenvolvido utilizando **HTML** e **CSS** para interatividade. A interface será otimizada para facilitar a navegação e a compreensão dos dados relacionados aos gastos públicos.

### **Back-end**

O **back-end** será desenvolvido em **Python**, utilizando o **Flask** como framework para construção da API. O **Flask** permitirá a criação de rotas e a manipulação de dados de forma eficiente e escalável, servindo de ponte entre o **back-end** e o **front-end**.

#### **Interação com Sistemas Externos**

O sistema será integrado com a **API** do **PTGF**, permitindo que os dados sobre os gastos públicos sejam obtidos diretamente do Portal da Transparência do Governo Federal.

#### **Coleta de Dados**

A coleta de dados será feita por meio da **API** do **PTGF**, que disponibiliza informações detalhadas sobre os gastos públicos. O sistema filtrará esses dados para focar nos gastos específicos relacionados ao Distrito Federal, permitindo que a plataforma forneça informações precisas e relevantes para a análise.

#### **Modelagem de Dados**

- **Valores dos Gastos Públicos**: Os dados serão disponibilizados mensalmente e anualmente, permitindo uma análise temporal dos gastos.
- **Órgãos**: Os dados serão organizados e apresentados separadamente por órgão público, para facilitar a visualização dos gastos específicos de cada instituição.
- **Análises e relatórios gráficos**: A implementação de ferramentas de visualização de dados (como gráficos e dashboards) pode melhorar a interpretação das informações.

O sistema irá incluir métricas e indicadores de fácil compreensão, ajudando o usuário a realizar uma análise aprofundada dos gastos públicos, com base nos critérios de interesse.

| Versão  |    Data    | Descrição                                      | Autor                                              | Revisão                                      |
| :-----: | :--------: | ---------------------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| `0.1.0` | 08/11/2024 | Criação do documento de arquitetura do projeto | [Gabriel Barbaceli](https://github.com/Nibaacriba) | [João Pedro](https://github.com/johnaopedro) |
