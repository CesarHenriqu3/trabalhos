import trabalhofunçoes

def menu():
    print("\nEscolha uma das opções: ")
    print("1. Listar Colaboradores: ")
    print("2. Relatório de Colaboradores em Ordem Alfabética: ")
    print("3. Relatório de Colaboradores por Ordem de Salário: ")
    print("4. Listar Cargos")
    print("5. Listar Colaboradores por cargo")
    print("6. Sair")

    while True:

        opção = input("\nEscolha uma das opções (1-6):")

        if opção == "1":
            trabalhofunçoes.lista()
        elif opção == "2":
            trabalhofunçoes.ordem_alfabética()
        elif opção == "3":
            trabalhofunçoes.ordem_salário()
        elif opção == "4":
            trabalhofunçoes.lista_de_cargos()
        elif opção == "5":
            trabalhofunçoes.listar_por_cargo()
        elif opção == "6":
            print("Tchaaau")
            break
        else:
            print("\nNenhum colaborador encotrado.")

menu()

