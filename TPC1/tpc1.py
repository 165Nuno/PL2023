import csv

def parse_csv_to_dict(filename):
    data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader, None)  # primeira linha como cabeçalho, se existir
        for row in reader:
            if headers:
                data_row = dict(zip(headers, row))
            else:
                data_row = row
            # Adicionamos o dicionário criado a um dicionário maior, onde cada elemento é uma linha.
            data[len(data)] = data_row
    return data

# Função que calcula a quantidade de homens
def conta_homens(dic):
    homens = 0
    for key,valor in dic.items():
        if valor['sexo'] == 'M':
            homens += 1
    return homens

# Função que calcula a quantidade de mulheres 
def conta_mulheres(dic):
    mulheres = 0
    for key,valor in dic.items():
        if valor['sexo'] == 'F':
            mulheres += 1
    return mulheres

# Função que calcula a quantidade de homens doentes 
def conta_homens_doentes(dic):
    homens_doentes = 0
    for key,valor in dic.items():
        if valor['sexo'] == 'M'and valor['temDoença'] == '1':
            homens_doentes += 1
    return homens_doentes

# Função que calcula a quantidade de mulheres doentes
def conta_mulheres_doentes(dic):
    mulheres_doentes = 0
    for key,valor in dic.items():
        if valor['sexo'] == 'F'and valor['temDoença'] == '1':
            mulheres_doentes += 1
    return mulheres_doentes

# Função que devolve a idade mínima
def idade_minima(dic):
    min = 1000;
    for key,valor in dic.items():
        if int(valor['idade']) < min:
            min = int(valor['idade'])
    return min

# Função que devolve a idade máxima
def idade_maxima(dic):
    max = 0;
    for key,valor in dic.items():
        if int(valor['idade']) > max:
            max = int(valor['idade'])
    return max

# Função para ver quantas pessoas com idades daquele intervalo com doenca
def etaria_doenca(min,max,dic):
    contador = 0;
    for key,valor in dic.items():
        if int(valor['idade']) >= min and int(valor['idade']) <= max and valor['temDoença'] == '1':
            contador += 1
    return contador

# Função para ver quantas pessoas com idades daquele intervalo
def quantos_faixa(min,max,dic):
    contador = 0;
    for key,valor in dic.items():
        if int(valor['idade']) >= min and int(valor['idade']) <= max:
            contador += 1
    return contador

# Função que utilizei inicialmente para visualizar a distribuição etária
def dist_etaria(idade_min, idade_max, tamanho_intervalo,dic):
    for i in range(idade_min, idade_max + 1, tamanho_intervalo):
        inicio_intervalo = i
        fim_intervalo = i + tamanho_intervalo - 1
        if fim_intervalo > idade_max:
            fim_intervalo = idade_max
        doentes = etaria_doenca(inicio_intervalo,fim_intervalo,dic)
        total = quantos_faixa(inicio_intervalo,fim_intervalo,dic)
        p = round((doentes / total) * 100,2)
        print(f"[{inicio_intervalo}-{fim_intervalo}] -> Existem {doentes} doentes em {total} pessoas, {p}%")

# Função que devolve o colesterol máximo
def col_max(dic):
    max = 0;
    for key,valor in dic.items():
        if int(valor['colesterol']) > max:
            max = int(valor['colesterol'])
    return max

# Função que devolve o colesterol minimo
def col_min(dic):
    min = 1000;
    for key,valor in dic.items():
        if int(valor['colesterol']) < min and int(valor['colesterol'])!=0:
            min = int(valor['colesterol'])
    return min


# Função que calcula quantas pessoas tem colesterol e doenca naquele intervalo
def etaria_cols(min,max,dic):
    contador = 0;
    for key,valor in dic.items():
        if int(valor['colesterol']) >= min and int(valor['colesterol']) <= max and valor['temDoença'] == '1':
            contador += 1
    return contador

# Função que calcula quantas pessoas tem colesterol com valores do intervalo
def quantos_cols(min,max,dic):
    contador = 0;
    for key,valor in dic.items():
        if int(valor['colesterol']) >= min and int(valor['colesterol']) <= max:
            contador += 1
    return contador

# Função que eu utilizei para visualizar inicialmente a distribuição colesterol
def dist_col(idade_min, idade_max, tamanho_intervalo,dic):
    
    for i in range(idade_min, idade_max + 1, tamanho_intervalo):
        inicio_intervalo = i
        fim_intervalo = i + tamanho_intervalo - 1
        if fim_intervalo > idade_max:
            fim_intervalo = idade_max
        doentes = etaria_cols(inicio_intervalo,fim_intervalo,dic)
        total = quantos_cols(inicio_intervalo,fim_intervalo,dic)
        if doentes == 0:
            p = 0
        else:
            p = round((doentes / total) * 100,2)
        print(f"[{inicio_intervalo}-{fim_intervalo}] -> Existem {doentes} doentes  em {total} pessoas nesta faixa de colesterol, {p}%")


# Função que cria o array com a informação de um intervalo colesterol
def cria_array_col(idade_min, idade_max, tamanho_intervalo,dic):

    array_de_array = []
    for i in range(idade_min, idade_max + 1, tamanho_intervalo):
        inicio_intervalo = i
        fim_intervalo = i + tamanho_intervalo - 1
        if fim_intervalo > idade_max:
            fim_intervalo = idade_max
        doentes = etaria_cols(inicio_intervalo,fim_intervalo,dic)
        total = quantos_cols(inicio_intervalo,fim_intervalo,dic)
        if doentes == 0:
            p = 0
        else:
            p = round((doentes / total) * 100,2)
        subarray = [f"[{inicio_intervalo}-{fim_intervalo}]", f"{doentes}", f"{total}", f"{p}%"]
        array_de_array.append(subarray)
    return array_de_array


# Função que cria o array com a informação de um intervalo etário
def criar_array_dist_etaria(idade_min, idade_max, tamanho_intervalo, dic):
    array_de_array = []
    
    for i in range(idade_min, idade_max + 1, tamanho_intervalo):
        inicio_intervalo = i
        fim_intervalo = i + tamanho_intervalo - 1
        if fim_intervalo > idade_max:
            fim_intervalo = idade_max
        doentes = etaria_doenca(inicio_intervalo, fim_intervalo, dic)
        total = quantos_faixa(inicio_intervalo, fim_intervalo, dic)
        p = round((doentes / total) * 100, 2)
        subarray = [f"[{inicio_intervalo}-{fim_intervalo}]", f"{doentes}", f"{total}", f"{p}%"]
        array_de_array.append(subarray)
    
    return array_de_array


# Função responsável pela a criação das tabelas de cada distribuição
def tabela(dados,cabecalhos):

    # Imprime os cabeçalhos
    print(f"{cabecalhos[0]:<10} {cabecalhos[1]:<7} {cabecalhos[2]:<5}  {cabecalhos[3]:<17}")

    # Imprime as linhas de dados
    for linha in dados:
        print(f"{linha[0]:<10} {linha[1]:<7} {linha[2]:<5} {linha[3]:<17}")


# Representação ascii para o menu
def ascii():
    print(" _________  _______     ______   __     ")
    print("|  _   _  ||_   __ \  .' ___  | /  |    ")
    print("|_/ | | \_|  | |__) |/ .'   \_| `| |    ")
    print("    | |      |  ___/ | |         | |    ")
    print("   _| |_    _| |_    \ `.___.'\ _| |_   ")
    print("  |_____|  |_____|    `.____ .'|_____|  ")
    print("                                        ")
    print("      Processamento de Linguagens       \n")

def main():

    # Primeiro ponto no trabalho de Casa
    filename = 'myheart.csv'
    data = parse_csv_to_dict(filename)

    # Segundo ponto no trabalho de Casa -> Dicionário
    
    # Variáveis do sexo, homens total e doentes e mulheres total e doentes
    homensTotal = conta_homens(data)
    mulheresTotal = conta_mulheres(data)
    homensDoentes = conta_homens_doentes(data)
    mulheresDoentes = conta_mulheres_doentes(data)

    # Variáveis da idade min e max
    min = idade_minima(data)
    max = idade_maxima(data)

    # Variáveis do colesterol, max e min
    max_col = col_max(data)
    min_col = col_min(data)

    ascii()
    while True:
        print("Selecione uma opção:")
        print("[1] - Distribuição por sexo")
        print("[2] - Distribuição por faixa etária")
        print("[3] - Distribuição por colesterol")
        print("[0] - Saír")
        opcao = input("Opção selecionada: ")
        if opcao.isdigit() and int(opcao) in range(0, 5):
            if int(opcao) == 1: # Tabela da distribuição por sexo
                    print("\n==> DISTRIBUIÇÃO DA DOENÇA POR SEXO <==\n")
                    cabecalhos_sexo = ["Sexo", "Doentes", "Total", "Percentagem"]
                    arrayx = [['Homem',homensDoentes,homensTotal,round((homensDoentes / homensTotal) * 100, 2)],['Mulher',mulheresDoentes,mulheresTotal,round((mulheresDoentes / mulheresTotal) * 100, 2)]]
                    tabela(arrayx,cabecalhos_sexo)
                    print("\n")
            elif int(opcao) == 2: # Tabela da distribuição por escalão etários
                    print("\n==> DISTRIBUIÇÃO DA DOENÇA POR ESCALÕES ETÁRIOS <==\n")
                    dred = criar_array_dist_etaria(min,max,5,data)
                    cabecalhos = ["Faixa", "Doentes", "Total", "Percentagem"]
                    tabela(dred,cabecalhos)
                    print("\n")
            elif int(opcao) == 3: # Tabela da distribuição por nível de colesterol
                        print("\n==> DISTRIBUIÇÃO DA DOENÇA POR NÍVEIS DE COLESTEROL <==\n")
                        col = cria_array_col(min_col,max_col,10,data)
                        cabecalhos_col = ["Faixa", "Doentes", "Total", "Percentagem"]
                        tabela(col,cabecalhos_col)
                        print("\n")
            elif int(opcao) == 0: # Opção de sair
                break
                
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == '__main__':
    main()