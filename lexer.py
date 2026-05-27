import re

TOKENS = [
    ('KEYWORD', r'CREATE|LIST|DONE|REMOVE'),
    ('STRING', r'"[^"]*"'),
    ('NUMBER', r'\d+'),
    ('SEMICOLON', r';'),
    ('SPACE', r'\s+'),
    ('INVALID', r'.')
]

def lexer(code):

    tokens = []

    while code:

        matched = False

        for token_type, pattern in TOKENS:

            regex = re.match(pattern, code)

            if regex:

                matched = True
                value = regex.group(0)

                # ignora espaços
                if token_type == 'SPACE':
                    pass

                # erro léxico
                elif token_type == 'INVALID':
                    print(f'Erro léxico: {value}')

                else:
                    tokens.append((token_type, value))

                code = code[len(value):]
                break

        if not matched:
            break

    return tokens