from ply import lex
import re 

tokens = (
    "LEVANTAR",
    "POUSAR",
    "MOEDA",
    "CONTACTO",
    "ABORTAR"
)

t_LEVANTAR = r"LEVANTAR"
t_POUSAR = r"POUSAR"
t_ABORTAR = r"ABORTAR"

saldo = 0
f = 0 
#0 corresponde pousado 
# 1 corresponde a levantado
# 2 corresponde a abortar


def t_MOEDA(t):
    r"MOEDA\s((\w+\,?\s?)+)"
    match = re.match(r"MOEDA\s((\w+\,?\s?)+)", t.value)
    t.value = match.group(1)
    return t

def t_CONTACTO(t):
    r"T\=(\d{9})"
    match = re.match(r"T\=(\d{9})", t.value)
    t.value = match.group(1)
    return t

def t_error(t):
    print("Erro")
    t.lexer.skip(1)


def calculaSaldo():
    global saldo
    centimos = saldo % 100
    euros = (saldo - centimos) // 100
    string = f"{euros}e{centimos:02}c"
    return string

def pMoedas(listaMoedas):
    global saldo
    print(listaMoedas)
    moedas = re.findall(r"\d+[ce]", listaMoedas)
    string = "maq: "

    for moeda in moedas:
        valor = int(re.findall(r"\d+", moeda)[0])
        if "c" in moeda:
            if valor not in [1, 2, 5, 10, 20, 50]:
                string += str(valor) + "c -> moeda inválida;"
            else:
                saldo += valor
        elif "e" in moeda:
            if valor not in [1, 2]:
                string += str(valor) + "e -> moeda inválida;"
            else:
                saldo += valor * 100

    string += "saldo = " + calculaSaldo()
    print(string)



# Função responsável por realizar o parse dos contactos
def pContacto(contacto):
    global saldo
    
    if contacto.startswith(('601', '641')):
        print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
    elif contacto.startswith('00') and saldo > 150:
        saldo -= 150
        print("maq: saldo = " + calculaSaldo())
    elif contacto.startswith('2') and saldo > 25:
        saldo -= 25
        print("maq: saldo = " + calculaSaldo())
    elif contacto.startswith('800'):
        print("maq: saldo = " + calculaSaldo())
    elif contacto and saldo > 10:
        saldo -= 10
        print("maq: saldo = " + calculaSaldo())
    else:
        print("maq: Saldo Insuficiente" if saldo > 0 else "maq: Contacto inválido")


# Função responsável pelo parse dos tokens
def pTokens(token):
    global f

    if token.type == "LEVANTAR":
        if f == 0:
            print("maq: Introduza moedas.")
            f = 1
        else:
            print("maq: O telefone já se encontra levantado...")
    
    elif token.type == "POUSAR":
        if f == 1:
            saldoFinal = calculaSaldo()
            print(f"maq: Troco = {saldoFinal}; Volte sempre!")
            f = 0
        else:
            print("maq: O telefone já se encontra pousado...")

    elif token.type == "MOEDA":
        if f == 0:
            print("maq: O telefone está pousado...")
        else:
            pMoedas(token.value)

    elif token.type == "CONTACTO":
        if f == 0:
            print("maq: O telefone está pousado...")
        else:
            pContacto(token.value)
    
    elif token.type == "ABORTAR":
        f = 2
    else:
        print("Erro no input")


def principal():
    lexer = lex.lex()
    while True:
        info = input("> ")
        lexer.input(info)
        for tok in lexer:
            pTokens(tok)
            if f == 2:
                break
        if f == 2:
            break

def print_art():
    print("               _              _ ")
    print("             | |------------| |")
    print("          .-'| |            | |`-.")
    print("        .'   | |            | |   `.")
    print("     .-'      \ \          / /      `-.")
    print("   .'        _.| |--------| |._        `.")
    print("  /    -.  .'  | |        | |  `.  .-    \\")
    print(" /       `(    | |________| |    )'       \\")
    print("|          \  .i------------i.  /          |")
    print("|        .-')/                \(`-.        |")
    print("\\    _.-'.-'/     ________     \`-.`-._    /")
    print(" \\.-'_.-'  /   .-' ______ `-.   \  `-._`-./\\")
    print("  `-'     /  .' .-' _   _`-. `.  \     `-' \\\\")
    print("         | .' .' _ (3) (2) _`. `. |        //")
    print("        / /  /  (4)  ___  (1)_\\  \ \       \\\\")
    print("        | | |  _   ,'   `.==' `| | |       //")
    print("        | | | (5)  | B.T.| (O) | | |      //")
    print("        | | |   _  `.___.' _   | | |      \\\\")
    print("        | \\  \\ (6)  _   _ (9) /  / |      //")
    print("        /  `. `.   (7) (8)  .' .'  \      \\\\")
    print("       /     `. `-.______.-' .'     \     //")
    print("      /        `-.________.-'        \ __//")
    print("     |                                |--'")
    print("     |================================|hjw")
    print("                                                         ")
    print("             Cabine Telefónica                       ")

def executa():
    print_art()
    principal()

executa()