import random

def chaveamento_4_times_gen():
    times = ["Time A", "Time B", "Time C", "Time D"]
    random.shuffle(times)

    print("\n====== CHAVEAMENTO ======")

    for time in range(0, len(times), 2):
        print(f"{times[time]} X {times[time+1]}")
        print("=========================")
    print("Os vencedores desses confrontos se enfrentarão na final.")
        

def chaveamento_6_times_gen():
    times = ["Time A", "Time B", "Time C", "Time D", "Time E", "Time F"]    

    random.shuffle(times)
    grupo_a = times[:3]
    grupo_b = times[3:]
    print("======GRUPO A======")
    for time1 in range(len(grupo_a)):
        for time2 in range(time1 + 1, len(grupo_a)):
            print(f"{grupo_a[time1]} X {grupo_a[time2]}")
    print("======GRUPO B======")
    for time1 in range(len(grupo_b)):
        for time2 in range(time1 + 1, len(grupo_b)):
            print(f"{grupo_b[time1]} X {grupo_b[time2]}")
    print("==============================================")
    print("O melhor colocado de cada grupo enfrentará o segundo melhor do grupo os confrontos devem seguir no seguinte modelo: ")
    print("1° do grupo A X 2° do grupo B")
    print("1° do grupo B X 2° do grupo A")
    print("Os terceiros colocados dos grupos estarão eliminados.")
    print("==============================================")
    
def chaveamento_8_times_gen():

    times = ["Time A", "Time B", "Time C", "Time D", "Time E", "Time F", "Time G", "Time H"]

    random.shuffle(times)
    print("======CHAVEAMENTO======")
    jogo = 1
    for time in range(0, len(times), 2):
        print(f"JOGO {jogo}")
        print(f"{times[time]} X {times[time+1]}")
        print("==============================")
        jogo += 1

    print("Os vencedores do jogo 1 e do jogo 2 se enfrentarão, assim como os vencedores do jogo 3 e do jogo 4, seguindo o modelo abaixo:")
    print("Vencedor do jogo 1 X Vencedor do jogo 2")
    print("Vencedor do jogo 3 X Vencedor do jogo 4")
    print("Os vencedores desses confrontos se enfrentarão na final.")

def quantidade_de_times_genericos():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Chaveamento com 4 times")
        print("2. Chaveamento com 6 times")
        print("3. Chaveamento com 8 times")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            chaveamento_4_times_gen()
        elif escolha == '2':
            chaveamento_6_times_gen()
        elif escolha == '3':
            chaveamento_8_times_gen()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
            

def quatro_vs_quatro_4_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(4):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")

    chaveamento_4_times_gen()

def quatro_vs_quatro_6_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(4):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")


def quatro_vs_quatro_8_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        "Time G",
        "Time H"
    ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(4):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")

def cinco_vs_cinco_4_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(5):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")

def cinco_vs_cinco_6_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(5):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")


def cinco_vs_cinco_8_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        "Time G",
        "Time H"
    ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(5):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")

def seis_vs_seis_4_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(6):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")
    

def seis_vs_seis_6_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(6):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")
    

def seis_vs_seis_8_times():
    times = [
        "Time A",
        "Time B",
        "Time C",
        "Time D",
        "Time E",
        "Time F",
        "Time G",
        "Time H"
    ]

    equipes = {}

    for time in times:
        equipes[time] = []

        print(f"\nCadastro do {time}")

        for i in range(6):
            nome = input(f"Jogador {i+1}: ")
            equipes[time].append(nome)

    print("\n=== EQUIPES ===")

    for time, jogadores in equipes.items():
        print(f"{time}: {jogadores}")
    
def quantidade_de_jogadores():
    while True:
        print("=== OPÇÕES PARA SORTEIO ===")
        print("1. 4 vs 4 com 4 times")
        print("2. 4 vs 4 com 6 times")
        print("3. 4 vs 4 com 8 times")
        print("4. 5 vs 5 com 4 times")
        print("5. 5 vs 5 com 6 times")
        print("6. 5 vs 5 com 8 times")
        print("7. 6 vs 6 com 4 times")
        print("8. 6 vs 6 com 6 times")
        print("9. 6 vs 6 com 8 times")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            quatro_vs_quatro_4_times()
            break
        elif escolha == '2':
            quatro_vs_quatro_6_times()
            break
        elif escolha == '3':
            quatro_vs_quatro_8_times()
            break
        elif escolha == '4':
            cinco_vs_cinco_4_times()
            break
        elif escolha == '5':
            cinco_vs_cinco_6_times()
            break
        elif escolha == '6':
            cinco_vs_cinco_8_times()
            break
        elif escolha == '7':
            seis_vs_seis_4_times()
            break
        elif escolha == '8':
            seis_vs_seis_6_times()
            break
        elif escolha == '9':
            seis_vs_seis_8_times()
            break
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
        
def menu():
    opcoes = {
        "1": ("Sortear jogadores para time", quantidade_de_jogadores),
        "2": ("Sortear jogos para times ", quantidade_de_times_genericos),
    }

    while True:
        print("\n=== MENU DE SORTEIOS ===")
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