import crud
import sorteios_salvando_no_banco as sorteios_banco
import sorteios_generico


def menu_principal():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Menu CRUD ")
        print("2. Menu Sorteios do banco de dados")
        print("3. Menu Sorteios do 0 sem salvar")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            crud.menu()
        elif escolha == '2':
            sorteios_banco.menu()
        elif escolha == '3':
            sorteios_generico.menu()
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()