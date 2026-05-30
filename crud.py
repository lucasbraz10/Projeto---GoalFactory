from banco_de_dados.conexao import conectar, fechar_conexao


def adicionar_time():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            nome_time = input("Digite o nome do time: ")

            cursor.execute("""
                INSERT INTO tbl_times (nome_time) VALUES (%s)
                """,(nome_time,))
            conexao.commit()
            
            print ("\nTime cadastrado com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)

def listar_time():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id_time, nome_time FROM tbl_times")

        times = cursor.fetchall()

        print("\n===== LISTA DE TIMES =====")
        for time in times:
            print(f"ID: {time[0]} | {time[1]}")

        cursor.close()
        fechar_conexao(conexao)

def atualizar_time():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            listar_time()
            id_time = input("Digite o ID do time que deseja atualizar: ")
            novo_nome = input("Digite o nome atualizado do time: ")
            cursor.execute("""
                UPDATE tbl_times SET nome_time = %s WHERE id_time = %s
                """,(novo_nome, id_time))
            conexao.commit()
            
            print("\n Time atualizado com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)


def excluir_time():
    conexao = conectar()

    if conexao:
        try:
            listar_time()
            cursor = conexao.cursor()
            id_time = input("Digite o ID do time que deseja excluir: ")
            cursor.execute("DELETE FROM tbl_times WHERE id_time = %s", (id_time,))
            conexao.commit()
            
            print ("\nTime excluído com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)


#jogadores
def adicionar_jogador():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            nome_jogador = input("Digite o nome do jogador: ")
            id_time = input("Digite o ID do time do jogador: ")

            cursor.execute("""
                INSERT INTO tbl_jogadores (nome_jogador, time_jogador) VALUES (%s, %s)
                """,(nome_jogador, id_time))
            conexao.commit()
            
            print ("\n Jogador cadastrado com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)
      

def listar_jogador():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute(""" 
        SELECT
            tbl_jogadores.id_jogador, 
            tbl_jogadores.nome_jogador,
            tbl_times.nome_time 
        FROM tbl_jogadores 
        INNER JOIN tbl_times ON tbl_jogadores.time_jogador = tbl_times.id_time
        """)

        jogadores = cursor.fetchall()

        print("\n===== LISTA DE JOGADORES =====")
        for jogador in jogadores:
            print(f"{jogador[0]} | {jogador[1]} | {jogador[2]}")

        cursor.close()
        fechar_conexao(conexao)
    

def atualizar_jogador():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            
            jogador_uptd = input("Digite o nome do jogador que deseja atualizar: ")
            
            cursor.execute("SELECT id_jogador FROM tbl_jogadores WHERE nome_jogador = %s", (jogador_uptd,))
            ids = cursor.fetchone()
            for id in ids:
                id_jogador = id
            novo_nome = input("Digite o nome atualizado do jogador: ")
            cursor.execute("""
                UPDATE tbl_jogadores SET nome_jogador = %s WHERE id_jogador = %s
                """,(novo_nome, id_jogador))
            conexao.commit()
            
            print ("\n Jogador atualizado com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)

      

def excluir_jogador():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            jogador_delete = input("Digite o nome do jogador que deseja excluir: ")
            
            cursor.execute("SELECT id_jogador FROM tbl_jogadores WHERE nome_jogador = %s", (jogador_delete,))
            ids = cursor.fetchone()
            for id in ids:
                id_jogador = id
            cursor.execute("DELETE FROM tbl_jogadores WHERE id_jogador = %s", (id_jogador,))
            conexao.commit()
            
            print ("\nJogador excluído com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)

#partidas

def adicionar_partida():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()

            id_time_vencedor = input("Digite o ID do time vencedor: ")
            id_time_perdedor = input("Digite o ID do time perdedor: ")
            placar_vencedor = input("Digite os gols do time vencedor: ")
            placar_perdedor = input("Digite os gols do time perdedor: ")

            cursor.execute("""
                INSERT INTO tbl_partidas_realizadas
                (time_vencedor, time_perdedor, placar_vencedor, placar_perdedor)
                VALUES (%s, %s, %s, %s)
            """, (id_time_vencedor, id_time_perdedor, placar_vencedor, placar_perdedor))

            conexao.commit()

            print("\n Partida cadastrada com sucesso!")

        except Exception as erro:
            conexao.rollback()
            print(f"\n Erro: {erro}")

        finally:
            cursor.close()
            fechar_conexao(conexao)


def listar_partida():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute(""" 
        SELECT 
            p.id_partida,
            tv.nome_time AS vencedor,
            placar_vencedor,
            placar_perdedor,
            tp.nome_time AS perdedor
        FROM tbl_partidas_realizadas p
        INNER JOIN tbl_times tv
            ON p.time_vencedor = tv.id_time
        INNER JOIN tbl_times tp
            ON p.time_perdedor = tp.id_time;
        """)

        partidas = cursor.fetchall()

        print("\n===== LISTA DE PARTIDAS =====")
        for partida in partidas:
            print(f"{partida[0]} | {partida[1]} {partida[2]} X {partida[3]} {partida[4]}")

        cursor.close()
        fechar_conexao(conexao)
    
          

def atualizar_partida():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()

            listar_partida()

            id_partida = input("\nDigite o ID da partida que deseja atualizar: ")
            id_time_vencedor = input("Digite o ID do time vencedor: ")
            id_time_perdedor = input("Digite o ID do time perdedor: ")
            placar_vencedor = input("Digite os novos gols do time vencedor: ")
            placar_perdedor = input("Digite os novos gols do time perdedor: ")

            cursor.execute("""
                UPDATE tbl_partidas_realizadas
                SET time_vencedor = %s,
                    time_perdedor = %s,
                    placar_vencedor = %s,
                    placar_perdedor = %s
                WHERE id_partida = %s
            """, (id_time_vencedor, id_time_perdedor, placar_vencedor, placar_perdedor, id_partida))

            conexao.commit()

            print("\n Partida atualizada com sucesso!")

        except Exception as erro:
            conexao.rollback()
            print(f"\n Erro: {erro}")

        finally:
            cursor.close()
            fechar_conexao(conexao)



def excluir_partida():
    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor()
            listar_partida()
            partida_delete = input("Digite o ID da partida que deseja excluir: ")
            
            cursor.execute("DELETE FROM tbl_partidas_realizadas WHERE id_partida = %s", (partida_delete,))
            conexao.commit()
            
            print ("\n Partida excluída com sucesso!")
            
        except Exception as erro:
            conexao.rollback()
            print(f"Erro: {erro}")
            
        finally:
            cursor.close()
            fechar_conexao(conexao)


def menu():
    opcoes = {
        "1": ("Adicionar Time", adicionar_time),
        "2": ("Listar Times", listar_time),
        "3": ("Atualizar Time", atualizar_time),
        "4": ("Excluir Time", excluir_time),
        "5": ("Adicionar Jogador", adicionar_jogador),
        "6": ("Listar Jogadores", listar_jogador),
        "7": ("Atualizar Jogador", atualizar_jogador),
        "8": ("Excluir Jogador", excluir_jogador),
        "9": ("Adicionar Partida", adicionar_partida),
        "10": ("Listar Partidas", listar_partida),
        "11": ("Atualizar Partida", atualizar_partida),
        "12": ("Excluir Partida", excluir_partida)
    }

    while True:
        print("\n=== MENU - CRUD SQL ===")
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