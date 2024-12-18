# Backlog

O projeto de Análise de Gastos Públicos do Distrito Federal tem como objetivo proporcionar aos cidadãos do Distrito Federal uma plataforma transparente e acessível para acompanhar, analisar e entender os gastos públicos realizados pelo governo local. Através deste sistema, os usuários poderão acessar dados detalhados sobre as despesas governamentais, como categorias de gastos, departamentos envolvidos, períodos específicos e informações sobre os fornecedores contratados com recursos públicos.

O objetivo principal é fornecer uma ferramenta que facilite a busca, visualização e análise de dados financeiros, promovendo a transparência e permitindo que os cidadãos participem ativamente no acompanhamento dos recursos públicos. Este backlog foi estruturado com as Histórias de Usuário (US) e seus respectivos Critérios de Aceitação, que visam guiar o desenvolvimento do sistema, garantindo que ele atenda às necessidades e expectativas dos usuários finais, com foco em usabilidade, acessibilidade e desempenho.

O sistema será composto por diversas funcionalidades, incluindo a busca de dados por categoria, departamento e período, a aplicação de filtros para análise detalhada dos gastos, a possibilidade de download dos dados em formatos acessíveis (como CSV e Excel), além de outras funcionalidades que garantirão uma experiência completa e intuitiva para o usuário. A seguir, estão descritas as Histórias de Usuário que detalham os requisitos do sistema, com seus respectivos critérios de aceitação.


## US01
**Como colaborador do projeto, eu quero uma documentação clara sobre os padrões de qualidade do Git/GitHub, para que eu possa seguir práticas consistentes e garantir a qualidade e a organização do código compartilhado.**

### Critérios de Aceitação:
- A documentação deve incluir padrões de nomeação de branches, commits, tags e pull requests.
- Deve conter uma seção sobre como escrever mensagens de commit claras e informativas.
- Instruções de como estruturar e revisar pull requests.
- Deve existir uma seção que defina o uso de labels, milestones e issues para organização do projeto.

---

## US02
**Como arquiteto de software ou líder de projeto, quero definir a arquitetura do projeto, para que eu possa estabelecer uma base sólida e escalável para o desenvolvimento de protótipos de baixa e alta fidelidade, garantindo que todos os componentes interajam de forma eficiente e atendam às necessidades dos usuários.**

### Critérios de Aceitação:
- **Definição das Camadas da Arquitetura:**
  - A arquitetura deve incluir camadas claras: Apresentação (Frontend) e Lógica de Negócio (Backend).
  - Cada camada deve ter suas responsabilidades e tecnologias definidas.
- **Seleção de Ferramentas e Tecnologias:**
  - As tecnologias e ferramentas utilizadas para cada camada devem ser definidas e aprovadas pela equipe de desenvolvimento.
  - A escolha das ferramentas deve considerar a facilidade de uso, a escalabilidade e a integração entre os componentes.
- **Revisão:**
  - A arquitetura proposta deve ser revisada e validada com as partes interessadas antes da implementação.
  - Feedbacks devem ser incorporados para garantir alinhamento com as expectativas do projeto.
- **Preparação para Implementação:**
  - A documentação da arquitetura deve estar pronta para ser usada como referência durante o desenvolvimento.
  - Deve incluir diagramas, fluxos de dados e descrições de como as camadas se comunicam.

---

## US03
**Como designer de UX/UI ou Product Owner, quero criar um protótipo de baixa fidelidade, para que eu possa validar rapidamente a estrutura e a navegação do produto antes de investir em design detalhado ou desenvolvimento.**

### Critérios de Aceitação:
- **Protótipo com Estrutura Simples:**
  - O protótipo deve ser criado com ferramentas básicas, como Figma.
  - Deve ser fácil de editar e modificar conforme necessário.
- **Cobertura das Telas Principais:**
  - Deve incluir as telas principais e fluxos essenciais do produto.
  - As telas devem refletir as principais funcionalidades e jornadas do usuário.
- **Interações Básicas:**
  - Deve incluir indicações visuais de navegação, como botões e links, para testar o fluxo de navegação.
- **Compreensão:**
  - O protótipo deve ser claro e fácil de entender.
  - Permitir feedback e validação inicial sobre o fluxo e a usabilidade do produto.
- **Ajustes Iterativos:**
  - O protótipo deve permitir ajustes rápidos com base no feedback recebido.
  - Deve possibilitar adaptações conforme as revisões e necessidades identificadas.

---

## US04
**Como designer de UX/UI, quero criar um protótipo de alta fidelidade, para que eu possa apresentar o design final com detalhes visuais e interações realistas para validação com stakeholders e testes de usabilidade com usuários.**

### Critérios de Aceitação:
- **Finalização do Protótipo de Baixa Fidelidade:**
  - O protótipo de alta fidelidade deve ser iniciado somente após a aprovação do protótipo de baixa fidelidade.
  - Todas as alterações e feedback do protótipo de baixa fidelidade devem ser incorporados.
- **Detalhamento Visual:**
  - Deve incluir todos os elementos visuais finais, como cores, tipografia, ícones e branding.
  - Deve refletir o design visual e estético esperado no produto final.
- **Interações Realistas:**
  - O protótipo deve simular interações complexas, incluindo animações, transições e feedback visual.
  - As interações devem ser próximas ao comportamento esperado no POC.
- **Funcionalidade de Navegação Completa:**
  - Deve permitir que os usuários naveguem entre as telas do produto de forma intuitiva e fluida.
  - Deve incluir todos os fluxos de navegação definidos, possibilitando uma experiência completa.

---

## US05
**Como um cidadão do Distrito Federal, quero visualizar gráficos e tabelas interativas que representem os gastos públicos, para que eu possa entender melhor como o dinheiro público está sendo utilizado e participar ativamente da fiscalização e tomada de decisões.**

### Critérios de Aceitação:
- **Visualização de Dados:**
  - Os gráficos devem representar diferentes categorias de gastos (saúde, educação, infraestrutura, etc.) e permitir que o usuário selecione a categoria que deseja visualizar.
  - As tabelas devem mostrar dados detalhados de cada categoria, incluindo montantes, datas e descrições.
- **Interatividade:**
  - O usuário deve ser capaz de interagir com os gráficos (ex. passar o mouse sobre os elementos para ver informações adicionais).
- **Acessibilidade:**
  - Os gráficos e tabelas devem ser responsivos e acessíveis em diferentes dispositivos (desktop, tablet e mobile).
- **Atualização de Dados:**
  - Os dados apresentados devem ser atualizados regularmente, de preferência em tempo real ou em intervalos predefinidos (ex. diariamente).
  - Deve ser informado para o usuário a data da última atualização dos dados.
  - O usuário deve ser informado quando os dados foram atualizados.

---

## US06
**Como um cidadão do Distrito Federal, quero ter a opção de filtrar os dados de gastos públicos por categorias (ex.: saúde, educação, segurança), para que eu possa analisar mais facilmente as informações relacionadas a áreas específicas e entender como o orçamento está sendo alocado.**

### Critérios de Aceitação:
- **Exibição de Filtros:**
  - O sistema deve apresentar opções de filtros visíveis e acessíveis para cada categoria de gasto (ex.: saúde, educação, segurança).
  - Os filtros devem ser apresentados em um formato amigável, como botões ou uma lista suspensa.
- **Interatividade dos Filtros:**
  - O usuário deve ser capaz de selecionar uma categoria de gastos ao mesmo tempo.
  - A seleção de um filtro deve atualizar os gráficos e tabelas de maneira dinâmica, sem a necessidade de recarregar a página.
- **Resetar Filtros:**
  - Deve haver uma opção para limpar todos os filtros aplicados e retornar à visualização padrão de todos os gastos.

---

## US07
**Como um cidadão do Distrito Federal, quero ter a opção de visualizar os gastos públicos por diferentes períodos (ano, trimestre, mês), para que eu possa analisar as tendências de gastos ao longo do tempo e entender melhor a evolução do orçamento.**

### Critérios de Aceitação:
- **Exibição de Períodos:**
  - O sistema deve apresentar opções de visualização por ano, trimestre e mês de forma clara e acessível.
  - As opções devem ser apresentadas em um formato intuitivo, como botões de seleção ou um menu suspenso.
- **Interatividade na Seleção de Período:**
  - O usuário deve ser capaz de selecionar um período específico e visualizar os dados correspondentes de forma dinâmica, sem recarregar a página.
  - A visualização deve atualizar automaticamente os gráficos e tabelas para refletir os dados do período selecionado.
- **Combinação com Filtros de Categoria:**
  - O sistema deve permitir que os usuários combinem a visualização por período com filtros de categoria de gastos, como saúde, educação, segurança, etc.
- **Persistência da Seleção de Período:**
  - Verificar a viabilidade de manter a seleção do período ao navegar para diferentes seções do aplicativo, permitindo que o usuário continue sua análise sem precisar refazer a seleção.

---

## US08
**Como um usuário do site, quero ter uma barra de navegação acessível, para que eu possa navegar facilmente entre diferentes seções do site e encontrar as informações que estou procurando.**

### Critérios de Aceitação:
- **Design da Barra de Navegação:**
  - A barra de navegação deve ser visualmente clara e fácil de usar, com links para todas as seções principais do site (ex.: Home, Gastos Públicos, Relatórios, Contato).
  - A barra deve ser responsiva e adaptar-se a diferentes tamanhos de tela (desktop, tablet, mobile).
- **Interatividade:**
  - A barra deve incluir um efeito visual (ex.: mudança de cor ou sublinhado) para indicar qual seção está atualmente ativa.
- **Responsividade:**
  - A barra de navegação deve ser colapsável em dispositivos móveis, exibindo um menu hambúrguer que se expande quando clicado.
  - O design deve garantir que todos os itens de navegação sejam facilmente acessíveis em telas menores.
- **Feedback ao Usuário:**
  - O sistema deve fornecer feedback visual ao usuário quando um item da barra de navegação é clicado, como uma animação ou uma transição suave.

---

## US09
**Como um cidadão interessado na análise do orçamento público, quero acessar uma área com informações sobre os valores médios gastos e receber alertas caso os gastos diários estejam fora do comum, para que eu possa monitorar possíveis anomalias e garantir o uso eficiente dos recursos públicos.**

### Critérios de Aceitação:
- **Alertas de Gastos Anômalos:**
  - Um alerta visual deve aparecer caso os gastos diários excedam uma variação aceitável (ex.: 20% acima da média).
- **Média de Gastos Visível:**
  - Deve ser exibida a média de gastos calculada automaticamente para um período definido (ex.: semanal, mensal).

---

## US10
**Como um cidadão do Distrito Federal, quero poder buscar informações sobre gastos públicos por categorias de gastos, departamentos e períodos específicos, para que eu possa encontrar rapidamente os dados que me interessam e realizar análises mais detalhadas.**

### Critérios de Aceitação:
- **Campo de Busca:**
  - Deve haver um campo de busca visível e acessível na interface, permitindo que os usuários insiram termos de pesquisa relacionados a categorias de gastos, departamentos ou períodos.
  - O campo deve ter um placeholder que indique claramente o que pode ser buscado (ex.: "Pesquisar por categoria, departamento ou período").
- **Sugestões e Auto-completar:**
  - À medida que o usuário digita, o sistema deve oferecer sugestões de categorias de gastos, departamentos e períodos disponíveis, facilitando a busca.
  - As sugestões devem ser exibidas em uma lista suspensa abaixo do campo de busca.
- **Resultados Filtrados:**
  - Após a pesquisa, os resultados devem ser exibidos em uma tabela ou gráfico, filtrando os dados de acordo com os critérios inseridos.
  - O sistema deve atualizar a visualização automaticamente com os resultados correspondentes à busca, sem necessidade de recarregar a página.
- **Combinação de Filtros:**
  - O usuário deve ser capaz de combinar múltiplos critérios de busca (ex.: buscar por uma categoria de gastos específica dentro de um departamento e em um período determinado).
  - A interface deve permitir que o usuário adicione ou remova critérios de busca de forma intuitiva.
- **Feedback Visual:**
  - O sistema deve fornecer feedback visual ao usuário quando a busca for realizada, como animações ou mensagens que indiquem que os resultados estão sendo carregados.
- **Acessibilidade:**
  - A funcionalidade de busca deve ser acessível, permitindo que todos os usuários, incluindo aqueles com deficiências, possam utilizá-la facilmente.
  - O campo de busca e as sugestões devem ser navegáveis por teclado, com foco visível nos elementos.

---

## US11
**Como uma pessoa interessada em finanças públicas, quero aplicar filtros por tipo de despesa (ex.: folha de pagamento, investimentos), para que eu possa visualizar e analisar facilmente os gastos por categoria específica.**

### Critérios de Aceitação:
- **Filtro por Tipo de Despesa:**
  - Deve ser possível selecionar diferentes tipos de despesa para filtrar os resultados (ex.: folha de pagamento, investimentos).
- **Atualização Automática dos Resultados:**
  - Os dados devem ser atualizados em tempo real conforme o filtro é aplicado, exibindo apenas os resultados relevantes.
- **Facilidade de Remoção de Filtro:**
  - O usuário deve poder limpar os filtros facilmente para retornar à visualização completa dos dados.

---

## US12
**Como um visitante do site, quero acessar uma seção de "Sobre" que explique o objetivo do projeto e o propósito do site, para que eu possa entender o contexto e a importância das informações apresentadas.**

### Critérios de Aceitação:
- **Conteúdo Claro e Informativo:**
  - A seção "Sobre" deve conter uma explicação clara e objetiva sobre o objetivo do projeto e a finalidade do site.
- **Visibilidade e Acesso Fácil:**
  - A seção "Sobre" deve estar visível no menu principal ou em uma área facilmente acessível, permitindo que os visitantes encontrem a informação rapidamente.
- **Estilo Consistente com o Site:**
  - A seção deve seguir o mesmo estilo visual do site, mantendo uma experiência de navegação coerente.

---

## US13
**Como um usuário do site, quero ter acesso a um guia de uso, para que eu possa entender como navegar e utilizar as principais funcionalidades do site de forma eficaz.**

### Critérios de Aceitação:
- **Localização do Guia de Uso:**
  - O guia de uso deve estar facilmente acessível em uma área visível do site, como no menu principal ou em uma seção dedicada.
  - Um ícone de ajuda ou botão "Guia de Uso" deve ser adicionado em um local destacado para que os usuários saibam onde encontrar o guia.
- **Conteúdo do Guia:**
  - O guia deve incluir instruções claras e visuais sobre como acessar as principais funcionalidades, como filtros de gastos, visualização por período, busca por categorias e navegação entre as seções.
  - Exemplos e capturas de tela devem ser utilizados para ilustrar as instruções e facilitar a compreensão dos usuários.
- **Formato Interativo:**
  - O guia deve incluir uma versão interativa (ex.: tour guiado, pop-ups de instrução) para novos usuários, destacando as funcionalidades principais conforme eles navegam pela primeira vez.
  - O guia interativo deve permitir que o usuário pule etapas ou encerre o tour a qualquer momento.
- **Atualização e Manutenção:**
  - O guia de uso deve ser atualizado sempre que houver mudanças ou adição de novas funcionalidades.
  - A manutenção deve garantir que as informações do guia permaneçam precisas e relevantes.
- **Acessibilidade:**
  - O guia deve ser acessível para todos os usuários, incluindo aqueles com deficiências, e deve seguir as diretrizes de acessibilidade (ex.: texto alternativo para imagens, navegação por teclado).
  - O conteúdo deve ser claro e simples, evitando jargões técnicos para garantir a compreensão de todos os públicos.
- **Feedback do Usuário:**
  - Deve haver uma opção para que os usuários deixem feedback sobre a utilidade do guia, permitindo melhorias futuras baseadas nas sugestões recebidas.

---

## US14
**Como um cidadão interessado na transparência pública, quero acessar dados básicos sobre os fornecedores pagos com dinheiro público, para que eu possa entender como os recursos estão sendo alocados e quais empresas estão sendo contratadas pelo governo.**

### Critérios de Aceitação:
- **Interface de Fornecedores:**
  - Deve existir uma interface ou página onde o usuário possa visualizar os dados dos fornecedores, incluindo informações como nome do fornecedor, CNPJ, valor total recebido e descrição do serviço ou produto fornecido.
- **Atualização dos Dados:**
  - Os dados devem ser atualizados regularmente, refletindo as transações mais recentes feitas com os fornecedores pagos com recursos públicos.

---

## US15
**Como um usuário que visualiza dados, quero ter uma opção para baixar os dados em formatos comuns (como CSV, e Excel), para que eu possa analisar e compartilhar as informações facilmente fora do sistema.**

### Critérios de Aceitação:
- **Botão de Download:**
  - Deve existir um botão ou link visível na interface de visualização de dados que permita ao usuário baixar os dados em formatos selecionáveis (CSV e Excel).
- **Manutenção de Formatação:**
  - Os dados exportados devem manter a formatação e o conteúdo conforme exibido na interface de visualização, incluindo todas as colunas, filtros e ordenações aplicados pelo usuário.
- **Download Intuitivo e Rápido:**
  - O download deve ser rápido e intuitivo, exibindo uma mensagem de confirmação ou feedback visual após a conclusão do download.
