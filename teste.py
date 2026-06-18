lista_cliente=[]
lista_funcionario=[]
lista_gerente=[]
lista_geral = [lista_funcionario,lista_cliente,lista_gerente]
def cadastrar():
    usuario = int(input("digite a quantidade de usuários que pretende cadastrar: "))

    print("1 - cliente")
    print("2 - funcionário ")
    print("3 - gerente ")
    cargo = int(input("escolha um cargo para cadastrar: "))
    i = 0
    while(i < usuario):
        if(cargo == 1):
            print("---Novo Cadastro de Cliente---")
            nome_c = input("-digite seu nome completo: ")
            cpf_c = input("-digite seu CPF: ")
            numero_c = input("-digite seu numero de telefone: ")
            cargo_t = "Cliente"
            print("------CLIENTE CADASTRADO------")
            print("--------------------------------------")
            cliente_dados = [nome_c,cpf_c,numero_c,cargo_t]
            lista_cliente.append(cliente_dados)
            i=i+1
        elif(cargo == 2):
            print("---Novo Cadastro de Funcionário---")
            nome_f = input("-digite seu nome completo: ")
            cpf_f = input("-digite seu CPF: ")
            numero_f = input("-digite seu numero de telefone: ")
            cargo_t = "Funcionário"
            print("------FUNCIONÁRIO CADASTRADO------")
            print("--------------------------------------")
            funcionario_dados = [nome_f,cpf_f,numero_f,cargo_t]
            lista_funcionario.append(funcionario_dados)
            i=i+1
        elif(cargo == 3):
            print("---Novo Cadastro de Gerência---")
            nome_g = input("-digite seu nome completo: ")
            cpf_g = input("-digite seu CPF: ")
            numero_g = input("-digite seu numero de telefone: ")
            cargo_t = "Gerente"
            print("------GERENTE CADASTRADO------")
            print("--------------------------------------")
            gerente_dados = [nome_g,cpf_g,numero_g,cargo_t]
            lista_gerente.append(gerente_dados)
            i= i+1
        else:
            print("--Opção inválida--")
            opcao3 = input("Deseja voltar ao cadastro?s/n: ")
            if(opcao3 == "s"):
                cadastrar()
            elif(opcao3 == "n"):
                escolhido = inicio()


def buscar(nome_busca):
    encontrado = False
    for lista in lista_geral:
        for usuario in lista:
            if(nome_busca.lower() in usuario[0].lower()):
                print("----BUSCA BEM SUCEDIDA----")
                print("Nome:",usuario[0])
                print("CPF: ",usuario[1])
                print("Numero: ",usuario[2])
                print("Cargo:", usuario[3])
                print("----------------------------------")
                encontrado = True
    if not encontrado:
        print("-----------------------")
        print("Usuário não cadastrado.")
        print("-----------------------")
def remover(nome_remover):
    encontrado = False
    for usuario in lista:
        if(nome_remover.lower() in usuario[0].lower()):
            opcao = input(("Tem certeza que deseja remover?(s/n): "))
            if(opcao == "s"):
                encontrado = True
                lista.remove(usuario)
            else:
                print("Usuário não removido....Redirecionando para tela de início.")
                escolhido = inicio()
            print("----Usuário Removido----")
    if not encontrado:
        print("Usuário não encontrado")
def totalclientes():
    total = 0
    for lista in lista_geral:
        total+=lista
    print("------ Relatório de Usuários Cadastrados ------")
    print("-O sistema possui", total , "usuários")
    if(len(lista) == 0 ):
        print("o sistema não possui nenhum usuário ainda...")
        desejo = input("Deseja cadastrar um novo?s/n: ")
        if(desejo == "s"):
            escolhido = cadastrar()
        elif(desejo == "n"):
            escolhido = inicio()
    else:
        for usuario in lista:
            print("dados do usuário : " , usuario)
            print("-------------------------")
    
def inicio():
    print("-----Início-----")
    print(" 0 - cadastrar um novo usuário na empresa")
    print(" 1 - buscar usuário por nome")
    print(" 2 - remover usuário do sistema")
    print(" 3 - relátorio de usuários cadastrados")
    print(" 4 - sair do programa")
    return int(input("escolha alguma das opções acima: "))
escolhido = inicio()
saioufica=0
while saioufica != "s":
    if(escolhido == 0):
        cadastrar()
        opcao2 = input("Deseja cadastrar mais um usuário?s/n: ")
        if(opcao2 == "s"):
            cadastrar()
        else:
            escolhido = inicio()
    elif(escolhido == 1):
        nome_busca =input("Escolha um nome para buscar: ")
        buscar(nome_busca)
    elif(escolhido == 2):
        nome_remover = input("Digite o usuário a ser removido: ")
        remover(nome_remover)
    elif(escolhido == 3):
        totalclientes()
    elif(escolhido == 4):
        saioufica = input("Tem certeza que deseja sair?s/n: ")
        if(saioufica == "n"):
            escolhido = inicio()
        elif(saioufica == "s"):
            print("----- Obrigado por usar o programa!! -----")
            break
    else:
        print("-Opção Inválida-")
        opcao3 = input("Deseja voltar ao início?s/n: ")
        if(opcao3 == "s"):
            escolhido = inicio()
        elif(opcao3 == "n"):
            print("----- Obrigado por usar o programa!! -----")
            break

        
    escolhido = inicio()