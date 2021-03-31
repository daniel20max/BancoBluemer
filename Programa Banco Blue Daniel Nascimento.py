nome = str(input("Nome: "))
saldo = float(1000)
idade = int(input("Idade: "))
endereco = str(input("Endereço: "))
passw = input("Sua senha: ")
while True:
    if  len(passw) <= 5:
        passw = input("Sua senha ")
    elif len(passw) <= 6:
        break
while True:
    op = int(input("Qual Opareção deseja fazer Deposito'0', Saque'1', Saldo'2', Sair'3': "))
    if op == 0:
        deposito = float(input("Quanto Deseja Depositar: "))
        saldo = saldo + deposito
    elif op == 1:
        saque = float(input("Valor de Saque: "))
        if saque > saldo:
            print("Você não Possui Cheque Especial")
            break
        saldo = saldo - saque
    elif op == 2:
        print("Seu Valor atual é:",saldo)
    elif op == 3:
        break
cadastro = [nome,idade,saldo,endereco]
while True:
    op2 = int(input("Qual Opareção deseja fazer Cadastro'0', Modificar nome'1', Mod idade'2', Mod endereço'3', Sair'4': "))
    if op2 == 0:
        for x in cadastro:
            print(x)
    elif op2 == 1:
        nome = str(input("Nome: "))
    elif op2 == 2:
        idade = int(input("Idade: "))
    elif op2 == 3:
        endereco = str(input("Endereço: "))
    elif op2 == 4:
        break
    cadastro = [nome,idade,saldo,endereco]