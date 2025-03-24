import funçoes

def menu():
    print("\nEscolha uma das opções: ")
    print("1. Listar Colaboradores: ")
    print("2. Relatório de Colaboradores em Ordem Alfabética: ")
    print("3. Relatório de Colaboradores por Ordem de Salário: ")
    print("4. Listar Colaboradores por cargo, selecione o cargo desejado.")
    print("5. Se deseja fechar o programa.")

    while True:

        opção = input("\nEscolha uma das opções (1-5): ")

        if opção == "1":
            funçoes.lista()
        elif opção == "2":
            funçoes.ordem_alfabética()
        elif opção == "3":
            funçoes.ordem_salário()
        elif opção == "4":
            funçoes.lista_de_cargos()
            funçoes.listar_por_cargo()
            menu()
        elif opção == "5":
            print("Byee...")
            exit()
        else:
            print("\nOpção inválida.")

menu()

