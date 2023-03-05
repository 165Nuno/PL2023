import json
import re
import collections
from collections import defaultdict


# Função responsável por fazer o parse
def processarFile():
    with open("processos.txt","r") as file_D:
        linhas = file_D.readlines()

        pattern= re.compile(r"^(?P<Pasta>\d+)::(?P<Data>\d{4}\-\d{2}\-\d{2})?::(?P<Nome>[a-zA-Z \,\.\(\)]+)?::(?P<Pai>[a-zA-Z \,\.\(\)]+)?::(?P<Mae>[a-zA-Z \,\.\(\)]+)?::(?P<Observacoes>(\s*.*\s*)*)?::$")
        processedLinhas = []
        for linha in linhas:
            match_result = pattern.match(linha)
            if match_result:
                processedLinhas.append(match_result.groupdict())
    return processedLinhas


# Função para alínea A ----------------------------------------------
def criarDictFrequencias(processedLinhas):
    # Criar um dicionário para armazenar as frequências de processos por ano
    freq_por_ano = {}

    # Criar um set para armazenar as pastas já contadas em cada ano
    pastas_contadas_por_ano = {}

    # Iterar sobre as linhas processadas
    for linha in processedLinhas:
        # Extrair o ano e a pasta do processo
        ano = linha["Data"][:4]
        pasta = linha["Pasta"]

        # Se a pasta já foi contada para o ano, passar para a próxima linha
        if ano in pastas_contadas_por_ano and pasta in pastas_contadas_por_ano[ano]:
            continue

        # Se o ano já estiver no dicionário, incrementar a contagem de processos
        if ano in freq_por_ano:
            freq_por_ano[ano] += 1
        # Caso contrário, adicionar o ano ao dicionário com uma contagem inicial de 1
        else:
            freq_por_ano[ano] = 1

        # Adicionar a pasta ao set de pastas contadas para o ano
        if ano in pastas_contadas_por_ano:
            pastas_contadas_por_ano[ano].add(pasta)
        # Caso contrário, criar um novo set com a pasta
        else:
            pastas_contadas_por_ano[ano] = {pasta}

    return freq_por_ano

# Função para a alínea D ---------------------------------------------------------------
def converter_to_json():
    with open("processos.txt", "r") as file:
        linhas = file.readlines()

    # Expressão regular para extrair os campos
    pattern = re.compile(
        r"^(?P<Pasta>\d+)::(?P<Data>\d{4}\-\d{2}\-\d{2})?::(?P<Nome>[a-zA-Z \,\.\(\)]+)?::(?P<Pai>[a-zA-Z \,\.\(\)]+)?::(?P<Mae>[a-zA-Z \,\.\(\)]+)?::(?P<Observacoes>(\s*.*\s*)*)?::$"
    )

    registros = []  
    for linha in linhas[:20]:
        match_result = pattern.match(linha)
        if match_result:
            # Extrai os campos do registro
            registro = match_result.groupdict()

            # Adiciona o registro à lista
            registros.append(registro)

    # Escreve a lista de registros no novo ficheiro em formato JSON
    with open("processos.json", "w") as file:
        json.dump(registros, file, indent=4)

def processaNomes(lista):
    dic = {}
    patternAno = re.compile(r"(\d{4})")
    patternNome = re.compile(r"[a-zA-Z]+")
    for l in lista:
        ano = patternAno.match(l['Data']).group(0)
        seculo = int(int(ano)/100 +1)
        if seculo not in dic:
            dic[seculo] = {}
        for campo in ['Nome', 'Pai', 'Mae']:
            if l[campo] is not None:
                nome = patternNome.findall(l[campo])
                if len(nome) !=0:
                    if nome[0] not in dic[seculo]:
                        dic[seculo][nome[0]] = 0
                    if nome[-1] not in dic[seculo]:
                        dic[seculo][nome[-1]] = 0
                    dic[seculo][nome[0]] += 1
                    dic[seculo][nome[-1]] += 1

    dicResultado = {}
    for k in dic.keys():
        dic[k] = collections.OrderedDict(sorted(dic[k].items(), key=lambda x: x[1], reverse=True))
        lista = list(dic[k].keys())[0:5]
        dicResultado[k] = lista

    return dicResultado



def relacoes_freq(parsed):
    dic = defaultdict(int)
    pattern = re.compile(r",((?:Pai|Filho|Irmao|Avo|Neto|Tio|Sobrinho|Mae|Primo])s?\b\s*[^.\d\(\)]*).")
    for d in parsed:
        if d['Observacoes']:
            relacoes = pattern.findall(d['Observacoes'])
            for r in relacoes:
                dic[r] += 1
    return dict(dic)



def tabelaAnoFrequencia(dic):
    # ordena o dicionário pelas chaves em ordem crescente
    dicOrdenado = dict(sorted(dic.items()))

    # determina o tamanho das colunas
    col1 = max(len(str(k)) for k in dicOrdenado.keys())
    col2 = max(len(str(v)) for v in dicOrdenado.values())

    # imprime a tabela
    print(f"{('Ano').ljust(col1)} {'Frequência'}")
    for k, v in dicOrdenado.items():
        print(f"{str(k).ljust(col1)} {str(v).rjust(col2)}")


def tabelaRelacoes(dic):
    # ordena o dicionário pelas chaves em ordem alfabética
    dicOrdenado = dict(sorted(dic.items()))

    # determina o tamanho das colunas
    col1 = max(len(k) for k in dicOrdenado.keys())
    col2 = max(len(str(v)) for v in dicOrdenado.values())

    # imprime a tabela
    print(f"{('Relação').ljust(col1)} {'Frequência'}")
    for k, v in dicOrdenado.items():
        print(f"{k.ljust(col1)} {str(v).rjust(col2)}")

def tabelaNomes(dic):
    # ordena o dicionário pelas chaves em ordem crescente
    dicOrdenado = dict(sorted(dic.items()))

    # determina o tamanho das colunas
    col1 = max(len(str(k)) for k in dicOrdenado.keys())
    col2 = max(len(str(dicOrdenado[k][0])) for k in dicOrdenado.keys())
    col3 = max(len(str(dicOrdenado[k][1])) for k in dicOrdenado.keys())
    col4 = max(len(str(dicOrdenado[k][2])) for k in dicOrdenado.keys())
    col5 = max(len(str(dicOrdenado[k][3])) for k in dicOrdenado.keys())
    col6 = max(len(str(dicOrdenado[k][4])) for k in dicOrdenado.keys())

    # imprime a tabela
    print(f"{'Século'.ljust(col1)} {'Nome 1'.ljust(col2)} {'Nome 2'.ljust(col3)} {'Nome 3'.ljust(col4)} {'Nome 4'.ljust(col5)} {'Nome 5'.ljust(col6)}")
    for k, v in dicOrdenado.items():
        print(f"{str(k).ljust(col1)} {v[0].ljust(col2)} {v[1].ljust(col3)} {v[2].ljust(col4)} {v[3].ljust(col5)} {v[4].ljust(col6)}")

def main():
    file = processarFile()
    while True:
        print("Selecione uma opção:")
        print("1 - Frequência de processos por ano ")
        print("2 - Frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos (5 MAIS USADOS)")
        print("3 - Frequência dos vários tipos de relação")
        print("4 - Converter os 20 primeiros registos num novo ficheiro de output mas em formato Json")
        print("5 - Sair")
    
        opcao = input("Opção escolhida: ")
    
        if opcao == "1":
            # Frequência de processos por ano
            alineaA= criarDictFrequencias(file)
            tabelaAnoFrequencia(alineaA)
            break
        elif opcao == "2":
            #Frequência de nomes próprios nos séculos
            alineaB = processaNomes(file)
            tabelaNomes(alineaB)
            break
        elif opcao == "3":
            #Frequência dos vários tipos de relação
            alineaC = relacoes_freq(file)
            tabelaRelacoes(alineaC)
            break
        elif opcao == "4":
            # Faz a conversão para ficheiro json
            print("Conversão feita com sucesso...")
            converter_to_json()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()