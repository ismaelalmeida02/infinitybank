from banco import banco, obterconta

def depositar(conta:int,valor:float) -> None:
    cliente = obterconta(conta)
    if cliente:
        cliente['saldo'] += valor
        print('deposito realizado com sucesso')
    else:
        print("conta não encontrada!")



