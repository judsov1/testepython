lista=[]
def cadastrar():
    cliente = int(input("digite a quantidade de clientes que pretende cadastrar:"))
    i = 0
    while(i < cliente):
        print("---Novo Cadastro---")
        nome = input("-digite seu nome completo: ")
        cpf = input("-digite seu CPF: ")
        numero = input("-digite seu numero de telefone: ")
        print("------CLIENTE CADASTRADO------")
        print("--------------------------------------")
        cliente_dados = [nome,cpf,numero]
        lista.append(cliente_dados)
        i= i+1
def buscar(nome_busca):
    encontrado = False
    for cliente in lista:
        if(nome_busca.lower() in cliente[0].lower()):
            print("----BUSCA BEM SUCEDIDA----")
            print("Nome:",cliente[0])
            print("CPF: ",cliente[1])
            print("Numero: ",cliente[2])
            print("----------------------------------")
            encontrado = True
    if not encontrado:
        print("-----------------------")
        print("Cliente não cadastrado.")
        print("-----------------------")
def remover(nome_remover):
    encontrado = False
    for cliente in lista:
        if(nome_remover.lower() in cliente[0].lower()):
            opcao = input(("Tem certeza que deseja remover?(sim/não): "))
            if(opcao == "sim"):
                encontrado = True
                del cliente[0]
            else:
                print("cliente não removido....Redirecionando para tela de início.")
                encontrado = inicio()
    if not encontrado:
        print("Usuário não encontrado")
    print("----USUÁRIO REMOVIDO----")
    
def inicio():
    print("-----Início-----")
    print(" 0 - cadastrar um novo cliente")
    print(" 1 - buscar cliente por nome")
    print(" 2 - remover cliente do sistema")
    print(" 3 - sair")
    return int(input("escolha alguma das opções acima: "))
escolhido = inicio()
while escolhido != 3:
    if(escolhido == 0):
        cadastrar()
    elif(escolhido == 1):
        nome_busca =input("Escolha um nome para buscar: ")
        buscar(nome_busca)
    elif(escolhido == 2):
        nome_remover = input("Digite o cliente a ser removido: ")
        remover(nome_remover)
    else:
        print("-Opção Inválida-")
        escolhido = inicio()
        
    escolhido = inicio()
print("Obrigado por usar o programa!")