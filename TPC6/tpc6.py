from ply import lex
import re 
import os

tokens = (
    "CONDITION",
    "CICLE",
    "COMENTARIOSIMPLES",
    "COMENTARIOMULTIPLO",
    "PROGRAM",
    "FUNCOES",
    "TIPO",
    "TAM",
    "NUMERO",
    "VARIAVEL",
    "OPERADOR",
    "STRINGEND",
    "RANGE",
    "CHAINIT", 
    "CHAEND",
    "PARENTESESINIT",
    "PARENTESESEND"
)

t_CONDITION = r"if|else|in\s"
t_CICLE = r"while|for"
t_COMENTARIOSIMPLES = r"\/\/.*"
t_COMENTARIOMULTIPLO = r"\/\*(.|\n)*\*\/"

def t_PROGRAM(t):
    r"program\s(\w+)"
    result = re.match(r"program\s(\w+)", t.value)
    t.value = result.group(1)
    return t

t_FUNCOES = r"(function\s)?\w+(?=\()"
t_TIPO = r"int"
t_TAM = r"\[\w+\]"
t_NUMERO = r"\d+"
t_VARIAVEL = r"\w+"
t_OPERADOR = "\+|-|\*|%|=|<|>|\,"
t_STRINGEND = r";"
t_RANGE = r"\[\d+\.\.\d+\]"
t_CHAINIT = r"{"
t_CHAEND = r"}"
t_PARENTESESINIT = r"\("
t_PARENTESESEND = r"\)"

def t_whitespace(t):
    r"\s+"
    pass

def t_error(t):
    print(f"Inválido: '{t.value[0]}'")
    t.lexer.skip(1)


# Função para imprimir os tokens de forma mais bonita
def print_tokens(tokens):
    print("TOKEN".ljust(15) + "VALOR")
    print("-" * 25)
    for token in tokens:
        print(token.type.ljust(15) + token.value)

# Menu principal
while True:
    print("MENU")
    print("1. Ler arquivo max.p")
    print("2. Ler arquivo fatorial.p")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_arquivo = "max.p"
    elif escolha == "2":
        nome_arquivo = "fatorial.p"
    elif escolha == "0":
        break
    else:
        print("Opção inválida!")
        continue

    # Verifica se o arquivo existe
    if not os.path.isfile(nome_arquivo):
        print("Arquivo não encontrado!")
        continue

    # Leitura do arquivo e tokenização
    with open(nome_arquivo, "r") as arquivo:
        texto = arquivo.read()

    lexer = lex.lex()
    lexer.input(texto)
    tokens = list(lexer)

    # Impressão dos tokens
    print_tokens(tokens)
