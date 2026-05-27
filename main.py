from preprocess import preprocess
from lexer import lexer
from parser import parser

# usuário escolhe arquivo
arquivo = input('Digite o nome do arquivo: ')

# abre arquivo
with open(arquivo, 'r') as file:
    code = file.read()

# pré-processamento
clean_code = preprocess(code)

# processamento
for line in clean_code:

    print('\nLinha:', line)

    # lexer
    tokens = lexer(line)

    print('Tokens:', tokens)

    # parser
    parser(tokens)