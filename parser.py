def parser(tokens):

    if len(tokens) == 0:
        return

    first = tokens[0][1]

    # CREATE
    if first == 'CREATE':

        if len(tokens) != 3:
            print('Erro sintático no CREATE')
            return

        if tokens[1][0] != 'STRING':
            print('Erro: esperado STRING')
            return

        if tokens[2][0] != 'SEMICOLON':
            print('Erro: esperado ;')
            return

        print('CREATE válido')

    # LIST
    elif first == 'LIST':

        if len(tokens) != 2:
            print('Erro sintático no LIST')
            return

        if tokens[1][0] != 'SEMICOLON':
            print('Erro: esperado ;')
            return

        print('LIST válido')

    # DONE
    elif first == 'DONE':

        if len(tokens) != 3:
            print('Erro sintático no DONE')
            return

        if tokens[1][0] != 'NUMBER':
            print('Erro: esperado NUMBER')
            return

        if tokens[2][0] != 'SEMICOLON':
            print('Erro: esperado ;')
            return

        print('DONE válido')

    # REMOVE
    elif first == 'REMOVE':

        if len(tokens) != 3:
            print('Erro sintático no REMOVE')
            return

        if tokens[1][0] != 'NUMBER':
            print('Erro: esperado NUMBER')
            return

        if tokens[2][0] != 'SEMICOLON':
            print('Erro: esperado ;')
            return

        print('REMOVE válido')

    else:
        print('Comando inválido')