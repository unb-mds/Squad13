# 🛡️ Política de Segurança

## 🔒 Versões com Atualizações de Segurança

Abaixo estão as versões do projeto que estão ativamente sendo mantidas com patches de segurança.

| Versão   | Atualizações Ativas |
| -------- | ------------------- |
| 1.0.0    | ✅                  |

---

## 🚨 Como Relatar uma Vulnerabilidade

Se você descobrir uma vulnerabilidade, siga estas orientações para reportá-la de maneira responsável:

### Passos para Reportar:
- Envie um e-mail para [gastosdfmonitor@gmail.com](mailto:gastosdfmonitor@gmail.com) com o assunto **"Vulnerabilidade"**.
- Inclua os seguintes detalhes:
  - Descrição detalhada da vulnerabilidade.
  - Passos claros para reproduzir o problema.
  - Qualquer prova relevante, como prints ou arquivos que mostrem o erro.

### O que Esperar:
- Confirmamos o recebimento do seu relatório em até **48 horas**.
- Analisaremos e corrigiremos a falha crítica dentro de **15 dias**, dependendo da complexidade.
- Se a vulnerabilidade não for aceita, explicaremos os motivos em detalhes.

---

## 📋 Escopo da Política

Esta política aplica-se a:

1. **Código do Projeto**: Garantimos que o código fonte está livre de vulnerabilidades evidentes.
2. **Bibliotecas e Dependências**: Monitoramos e atualizamos regularmente as dependências externas para evitar problemas de segurança.

---

## 🔐 Práticas de Segurança

1. **Validação de Entrada de Dados**:
   - Todos os dados fornecidos pelos usuários são rigorosamente verificados para prevenir falhas como injeção de código ou execução de scripts maliciosos.

2. **Controle de Dependências**:
   - Realizamos auditorias periódicas nas bibliotecas externas e mantemos as versões mais seguras atualizadas.

3. **Proteção de Dados Sensíveis**:
   - Informações sensíveis nunca são armazenadas diretamente no repositório. Elas são gerenciadas usando variáveis de ambiente de maneira segura.

---

## 🛠️ Diretrizes para Contribuidores

Para manter a integridade e a segurança do projeto, é essencial que todos os colaboradores sigam as práticas descritas abaixo:

1. **Proteção de Dados Sensíveis**:
   - Nunca inclua informações confidenciais no repositório, como senhas, tokens de autenticação ou chaves privadas. Certifique-se de que esses dados sejam armazenados de forma segura, fora do controle de versão, para evitar exposição acidental.
     
2. **Gerenciamento de Dependências de Forma Consciente**:
   - Ao adicionar bibliotecas externas, seja cauteloso e sempre verifique se são seguras e compatíveis com as versões mais recentes. Dependências desatualizadas ou mal mantidas podem introduzir riscos significativos para o projeto.

3. **Revisão Constante e Testes Rigorosos**:
   - É fundamental realizar revisões regulares do código para detectar possíveis vulnerabilidades e melhorar a segurança do projeto. Além disso, cada nova implementação deve passar por uma bateria de testes, com ênfase em garantir que novas falhas não sejam introduzidas.

---

## 🔄 Atualizações de Segurança

Estamos comprometidos em manter o projeto seguro e sempre atualizá-lo para corrigir possíveis falhas.

- **Atualizações Críticas**: Cada correção crítica será destacada no changelog do projeto para manter todos informados.

---

