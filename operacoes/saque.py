from banco import banco, obterconta

def sacar(conta:int,valor:float) ->None:
    cliente =obterconta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('saque realizado com sucesso!')
        else:
            print('saldo insulficiente!')
    else:
        print('conta não encontrada!')


sacar(1,500)
print(banco)