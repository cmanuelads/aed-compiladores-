# TaskScript - Mini-Interpretador

Este projeto foi desenvolvido como parte da Atividade de Estudo Dirigido (AED) para a disciplina de Compiladores. Trata-se de uma pequena linguagem de domínio específico (DSL) voltada para o gerenciamento básico de tarefas (To-Do List).

## 📋 Proposta da Linguagem
A finalidade da linguagem é permitir o gerenciamento de tarefas por meio de comandos simples. O interpretador valida as instruções e simula o comportamento das etapas iniciais de um compilador.

## 🛠️ Passos da Aplicação

### 1. Pré-processamento (`preprocess.py`)
Remove linhas vazias, espaços desnecessários e ignora totalmente comentários iniciados com o caractere `#`.

### 2. Analisador Léxico (`lexer.py`)
Lê o código limpo e utiliza Expressões Regulares (RegEx) para identificar os lexemas e categorizá-los nos seguintes tokens:
- **KEYWORD**: `CREATE`, `LIST`, `DONE`, `REMOVE`
- **STRING**: Textos entre aspas duplas para os nomes das tarefas
- **NUMBER**: Identificadores numéricos das tarefas
- **SEMICOLON**: O delimitador `;`
- **INVALID**: Captura e trata os erros léxicos

### 3. Analisador Sintático (`parser.py`)
Valida a estrutura dos comandos com base na seguinte **Gramática Livre de Contexto (GLC)**:

```text
<Programa> ::= <Comando> <Programa> | ε
<Comando> ::= <ComandoCreate> | <ComandoList> | <ComandoDone> | <ComandoRemove>

<ComandoCreate> ::= "CREATE" STRING ";"
<ComandoList>   ::= "LIST" ";"
<ComandoDone>   ::= "DONE" NUMBER ";"
<ComandoRemove> ::= "REMOVE" NUMBER ";"