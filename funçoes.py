lista_colaboradores = [
    {"nome": "Cesar", "CPF": "509.944.754-45", "cargo": "Gerente", "salario": 3000},
    {"nome": "Gabi", "CPF": "515.675.123-54", "cargo": "Caixa", "salario": 1500},
    {"nome": "Bruno", "CPF": "654.768.124-66", "cargo": "Vendedor", "salario": 2500},
    {"nome": "Guilherme", "CPF": "543.218.122-65", "cargo": "Estoquista", "salario": 2000},
    {"nome": "Leticia", "CPF": "423.566.123-98", "cargo": "Supervisora", "salario": 5000}
]

#Listar colaboradores

def lista():
    print("lista de colaboradores:")
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador["nome"]}, CPF: {colaborador["CPF"]}, Cargo: {colaborador["cargo"]}, Salario: {colaborador["salario"]}")

#Lista em ordém alfabética

def ordem_alfabética():
    print(f"\nLista em ordem alfabética:")
    for colaborador in sorted(lista_colaboradores, key = lambda x: x ["nome"]):
        print(f"Nome: {colaborador["nome"]}, CPF: {colaborador["CPF"]}, Cargo: {colaborador["cargo"]}, Salario: {colaborador["salario"]}")

#Lista em ordém de salário

def ordem_salário():
    print(f"\nLista por ordem de salário:")
    for colaborador in sorted(lista_colaboradores, key = lambda x: x ["salario"]):
        print(f"Nome: {colaborador["nome"]}, CPF: {colaborador["CPF"]}, Cargo: {colaborador["cargo"]}, Salario: {colaborador["salario"]}")

#Listar Cargos  
      
def lista_de_cargos():
    print("\nCargos existentes:")
    for colaborador in sorted(lista_colaboradores, key = lambda x: x ["cargo"]):
        print(f"-{colaborador["cargo"]}")


#Listar colaboradores por cargo(o usuario deve digitar o cargo)

def listar_por_cargo():
    while True:
        cargo_desejado = input("\nDigite o cargo desejado: ").lower()
        if cargo_desejado == "sair":
            print("\nVocê saiu da listagem por cargo.")
            break

        colaboradores_filtrados = []

        for colaborador in lista_colaboradores:
            if colaborador["cargo"].lower() == cargo_desejado:
                    colaboradores_filtrados.append(colaborador)

        if colaboradores_filtrados:
            for colaborador in colaboradores_filtrados:
                print(f"Nome: {colaborador["nome"]}, CPF: {colaborador["CPF"]}, Cargo: {colaborador["cargo"]}, Salario: {colaborador["salario"]}")
                for colaborador in colaboradores_filtrados:
                    print("\nSe deseja sair da busca por cargo digite: 'sair'.")
                break
        else:
            print("Nenhum colaborador com esse cargo encontrado.")
