from banco import banco, obterconta

def consultarsaldo(conta:int) ->None:
    cliente = obterconta(conta)
    if cliente:
        print(f'seu saldo é:{cliente["saldo"]}')
    else:
        print('conta não encotrada!')

consultarsaldo(1)
print(banco)