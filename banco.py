from typing import Optional
from time import sleep
banco = [
    {"conta": 1, "cliente": "lucas", "saldo":1000.0},
    {"conta": 2, "cliente": "mariana", "saldo":2500.0}
]

conta_atual = 2

def adicionarconta(cliente:str,saldo:float) -> None:
    global conta_atual
    conta_atual +=1
    conta = {"conta":conta_atual,
             "cliente":cliente,
             "saldo":saldo
             }
    banco.append(conta)
    print("cadastro realizado com sucesso!")


def obterconta(conta:int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente["conta"] == conta:
            return cliente

    return None


def deletarconta(conta:int) -> bool:
    cliente = obterconta(conta)
    if cliente:
        banco.remove(cliente)
        print("cliente removido com sucesso!")
    else:
        print("cliente não encontrado!")

def listarcontas() -> None:
    for cliente in banco:
        print("---dados do cliente---")
        print(f"N. conta: {cliente['conta']}")
        print(f"cliente: {cliente['cliente']}")
        print(f"saldo: {cliente['saldo']}")
        print("--------------------------------")
        sleep(2)

def atualiizarnome(conta:int, novo_nome:str) ->None:
    cliente = obterconta(conta)
    if cliente:
        cliente['cliente']= novo_nome
        print('dados alterados com sucesso!')
    else:
        print('cliente não encontrado!')

def atualizarsaldo(conta:int,novo_saldo:float)->None:
    cliente = obterconta(conta)
    if cliente:
        cliente['saldo'] = novo_saldo
        print('dados alterados com sucesso!')
    else:
        print('cliente não encontrado!')

adicionarconta("carlos", 500)
print(obterconta(2))
deletarconta(2)
print(banco)
atualiizarnome(1,"joão")
atualizarsaldo(1,1000)
listarcontas()