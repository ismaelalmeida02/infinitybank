from banco import  obterconta


def transferir(contaOri:int, contades:int,valor:float) -> None:
    contaOrigem = obterconta(contaOri)
    contadestino = obterconta(contades)
    if contaOrigem and contadestino:
        if contaOrigem['saldo'] >= valor:
            contadestino['saldo'] += valor
            contaOrigem['saldo'] -= valor
            print('transferencia realizada com secesso!')
        else:
            print('saldo insulficiente')

    else:
        print('umas das contas não existe!')

