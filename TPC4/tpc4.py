
import re
import json
import sys

def oi(nome_ficheiro):
    lista = []
    regexp= re.compile(r"(?P<Numero>[^,]+),(?P<Nome>[^,]+),(?P<Curso>[^,]+),?(?P<Notas>[^{,]+)?(?P<Intervalo>\{\d(?:,\d)?\})?(?:::)?(?P<Agregação>[^,]+)?")
    with open(nome_ficheiro,'r') as file:
        linha_informação = file.readline()[:-1]
        cab = (regexp.match(linha_informação).groupdict())
        lines = file.readlines()
        for line in lines:
            aux = {}
            pos_split = line.replace('\n', '').split(',')  ## Fazer o split da line com o delimitador ","

            if(cab['Numero']is not None):
                aux['Numero'] = pos_split[0]

            if(cab['Nome']is not None):
                aux['Nome'] = pos_split[1]

            if(cab['Curso']is not None):
                aux['Curso'] = pos_split[2] 

            if (cab['Notas'] is not None):
                if (cab['Intervalo'] is not None):
                    regexp_intervalos = re.compile(r"{(?P<Minimo>\d),?(?P<Maximo>\d)?}")
                    numeros = (regexp_intervalos.match(cab['Intervalo']).groupdict())
                    numero_minimo_notas = int(numeros['Minimo'])
                    if(numeros['Maximo'] is not None):                                        ## Número Minimo de Notas
                        numero_maximo_notas = int(numeros['Maximo'])                                        ## Número Máximo de Notas
                        notas = [int(x) for x in pos_split[3:3+numero_maximo_notas] if x.isdigit()]
                    else: 
                        notas = [int(x) for x in pos_split[3:3+numero_minimo_notas] if x.isdigit()]        ## Criamos a lista das notas que vão da posicao 3 do pos_split ate à posição 3+ número máximo de notas
                    if (cab['Agregação'] is not None):
                        if (cab['Agregação'] == 'sum'):
                            soma = sum(notas)
                            aux['Nota'] = soma
                        else:
                            media = sum(notas) / len(notas)
                            aux['Nota'] = media
                    else:
                        aux['Nota'] = notas
                else:
                    aux['Nota'] = pos_split[3]
            lista.append(aux)   
        return lista
    

def escrever_json(lista_de_dicionarios, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        #json.dump(lista_de_dicionarios, f,indent= 1)
        json.dump(lista_de_dicionarios, f, indent=2, separators=(',', ': '))

def main_menu():
    print("========== MENU PRINCIPAL ==========")
    print("1. ALUNOS.CSV")
    print("2. ALUNOS2.CSV")
    print("3. ALUNOS3.CSV")
    print("4. ALUNOS4.CSV")
    print("5. ALUNOS5.CSV")
    print("6. SAIR")

    choice = input("Digite sua escolha: ")
    if choice == '1':
        l = oi("alunos.csv")
        escrever_json(l,"ALUNOS1.json")
        print("Criou o json ALUNOS1...")
    elif choice == '2':
        l = oi("alunos2.csv")
        escrever_json(l,"ALUNOS2.json")
        print("Criou o json ALUNOS2...")
    elif choice == '3':
        l = oi("alunos3.csv")
        escrever_json(l,"ALUNOS3.json")
        print("Criou o json ALUNOS3...")
    elif choice == '4':
        l = oi("alunos4.csv")
        escrever_json(l,"ALUNOS4.json")
        print("Criou o json ALUNOS4...")
    elif choice == '5':
        l = oi("alunos5.csv")
        escrever_json(l,"ALUNOS5.json")
        print("Criou o json ALUNOS5...")
    elif choice == '6':
        print("Saindo do menu...")
        return
    else:
        print("Opção inválida. Tente novamente.")
        main_menu()

def main():
    main_menu()
    
if __name__ == '__main__':
    main()


