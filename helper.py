def validar_id(texto, limite):
    id_time = int(input(texto))

    while id_time > limite:
        print("ID inválido!")
        id_time = int(input(texto))
    return id_time