#definindo funções de sorteio
import random
from banco_de_dados.conexao import conectar, fechar_conexao
from crud import listar_time
from helper import validar_id

def limite_id():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id_time FROM tbl_times ORDER BY id_time DESC LIMIT 1")

        times = cursor.fetchall()

        for id in times:
            limite = id[0]

        cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
        return limite

def chaveamento_4_times():
    conexao = conectar()
    limite = limite_id()
    if conexao:
        print("======TIMES DISPONÍVEIS PARA SORTEIO======")
        listar_time()
        print("==========================================")
        print("Digite o ID do time que deseja sortear:")
        id_time1 = validar_id("ID 1: ", limite)
        id_time2 = validar_id("ID 2: ", limite)
        id_time3 = validar_id("ID 3: ", limite)
        id_time4 = validar_id("ID 4: ", limite)

        cursor = conexao.cursor()
        cursor.execute(
            """SELECT nome_time FROM tbl_times WHERE id_time = %s 
            OR id_time = %s OR id_time = %s OR id_time = %s
            """,(id_time1, id_time2, id_time3, id_time4))

        times = cursor.fetchall()
        random.shuffle(times)
        print("======CHAVEAMENTO======")
        for time in range(0, len(times), 2):
            print(f"{times[time][0]} X {times[time+1][0]}")
            print("==============================")

        cursor.close()
        fechar_conexao(conexao)
    
def chaveamento_6_times():
    conexao = conectar()
    if conexao:
        limite = limite_id()
        print("======TIMES DISPONÍVEIS PARA SORTEIO======")
        listar_time()
        print("==========================================")
        print("Digite o ID do time que deseja sortear:")
        id_time1 = validar_id("ID 1: ", limite)
        id_time2 = validar_id("ID 2: ", limite)
        id_time3 = validar_id("ID 3: ", limite)
        id_time4 = validar_id("ID 4: ", limite)
        id_time5 = validar_id("ID 5: ", limite)
        id_time6 = validar_id("ID 6: ", limite)

        cursor = conexao.cursor()
        cursor.execute(
            """SELECT nome_time FROM tbl_times WHERE id_time = %s 
            OR id_time = %s OR id_time = %s OR id_time = %s
            OR id_time = %s OR id_time = %s
            """,(id_time1, id_time2, id_time3, id_time4, id_time5, id_time6))

        times = cursor.fetchall()
        random.shuffle(times)
        grupo_a = times[:3]
        grupo_b = times[3:]
        print("======PARTIDAS DO GRUPO A======")
        for time1 in range(len(grupo_a)):
            for time2 in range(time1 + 1, len(grupo_a)):
                print(f"{grupo_a[time1][0]} X {grupo_a[time2][0]}")
        print("======PARTIDAS DO GRUPO B======")
        for time1 in range(len(grupo_b)):
            for time2 in range(time1 + 1, len(grupo_b)):
                print(f"{grupo_b[time1][0]} X {grupo_b[time2][0]}")
        print("==============================================")
        print("O melhor colocado de cada grupo enfrentará o segundo melhor do grupo os confrontos devem seguir no seguinte modelo: ")
        print("1° do grupo A X 2° do grupo B")
        print("1° do grupo B X 2° do grupo A")
        print("Os terceiros colocados dos grupos estarão eliminados.")
        print("==============================================")
        

def chaveamento_8_times():
    conexao = conectar()
    if conexao:
        limite = limite_id()
        print("======TIMES DISPONÍVEIS PARA SORTEIO======")
        listar_time()
        print("==========================================")
        print("Digite o ID do time que deseja sortear:")
        id_time1 = validar_id("ID 1: ", limite)
        id_time2 = validar_id("ID 2: ", limite)
        id_time3 = validar_id("ID 3: ", limite)
        id_time4 = validar_id("ID 4: ", limite)
        id_time5 = validar_id("ID 5: ", limite)
        id_time6 = validar_id("ID 6: ", limite)
        id_time7 = validar_id("ID 7: ", limite)
        id_time8 = validar_id("ID 8: ", limite)

        cursor = conexao.cursor()
        cursor.execute(
            """SELECT nome_time FROM tbl_times WHERE id_time = %s 
            OR id_time = %s OR id_time = %s OR id_time = %s
            OR id_time = %s OR id_time = %s OR id_time = %s OR id_time = %s
            """,(id_time1, id_time2, id_time3, id_time4, id_time5, id_time6, id_time7, id_time8))

        times = cursor.fetchall()
        random.shuffle(times)
        print("======CHAVEAMENTO======")
        jogo = 1
        for time in range(0, len(times), 2):
            print(f"JOGO {jogo}")
            print(f"{times[time][0]} X {times[time+1][0]}")
            print("==============================")
            jogo += 1

        print("Os vencedores do jogo 1 e do jogo 2 se enfrentarão, assim como os vencedores do jogo 3 e do jogo 4, seguindo o modelo abaixo:")
        print("Vencedor do jogo 1 X Vencedor do jogo 2")
        print("Vencedor do jogo 3 X Vencedor do jogo 4")
        print("Os vencedores desses confrontos se enfrentarão na final.")
        cursor.close()
        fechar_conexao(conexao)

#Menu
def menu():
    opcoes = {
        "1": ("Chaveamento com 4 times", chaveamento_4_times),
        "2": ("Chaveamento com 6 times", chaveamento_6_times),
        "3": ("Chaveamento com 8 times", chaveamento_8_times)
    }

    while True:
        print("\n=== OPÇÕES PARA FORMATO DO TORNEIO===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
        else:
            print("Opcao invalida. Tente novamente.")