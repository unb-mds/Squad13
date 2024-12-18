# Tags de Release no GitHub

As tags da release no GitHub (ou no Git em geral) são marcadores que apontam para um commit específico no histórico do repositório. Elas são usadas para identificar versões estáveis ou significativas de um projeto, como versões de produção, versões beta ou marcos importantes.

Essas tags permitem que você crie uma referência clara e imutável para uma versão do código no estado em que estava no momento da liberação. No contexto das Releases no GitHub, as tags desempenham um papel central na organização e no versionamento do projeto.

## Por que usar tags para releases?

- **Organização**: Ajuda a rastrear e identificar versões do projeto de maneira clara.
- **Imutabilidade**: As tags são "fixas" e apontam para um commit específico, garantindo que o código daquela versão não será alterado.
- **Compatibilidade**: Ferramentas de automação, CI/CD e gerenciadores de dependências usam tags para referenciar versões específicas.
- **Facilidade de uso**: Usuários e desenvolvedores podem baixar o código de uma versão específica com base na tag associada.

## Como funcionam as tags no Git?

- **Tags anotadas**: Contêm metadados adicionais como mensagem, nome do criador e data. Geralmente são usadas para releases públicas.
- **Tags leves**: Apenas marcam um commit sem informações adicionais, sendo mais simples e rápidas de criar.

## Como criar uma tag no Git?

Você pode criar uma tag localmente antes de associá-la a uma release no GitHub.

### Criar uma tag anotada:

```bash
git tag -a v1.0.0 -m "Versão 1.0.0 estável"
```

## Criar uma tag leve:

```bash
git tag v1.0.0
```

## Enviar a tag para o repositório remoto:

```bash
git push origin v1.0.0
```

## Enviar todas as tags locais de uma vez (opcional):

```bash
git push --tags
```

## Usando Tags para Releases no GitHub

Quando você cria uma Release no GitHub, uma das etapas é associar uma tag:

- No campo de tag, você pode escolher uma existente ou criar uma nova.
- A tag será vinculada automaticamente ao commit atual ou ao que você selecionar.
- Essa tag se torna a referência para aquela versão, permitindo que outros façam download do código-fonte ou o usem em automações.

## Exemplo Prático de Tag e Release

Se você está lançando a versão `v1.0.0` do seu software:

1. Crie a tag `v1.0.0` no commit estável correspondente.
2. Publique uma release no GitHub associada à tag `v1.0.0`.
3. Inclua Release Notes detalhando mudanças e melhorias feitas nessa versão.

[Documentação sobre Gerenciamento de Releases no GitHub](https://docs.github.com/pt/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
