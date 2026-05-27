def preprocess(code):
    lines = code.split('\n')
    clean_lines = []

    for line in lines:
        line = line.strip()

        # remove comentários
        if line.startswith('#'):
            continue

        # remove linhas vazias
        if line == '':
            continue

        clean_lines.append(line)

    return clean_lines