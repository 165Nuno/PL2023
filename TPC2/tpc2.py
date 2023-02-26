import sys
    
def programa_tpc2():
    soma_ativada = True  
    total = 0  
    try:
        while True:
            linha = sys.stdin.readline().strip()  # lê uma linha de texto do stdin
            if linha.lower() == "on":
                soma_ativada = True
            elif linha.lower() == "off":
                soma_ativada = False
            for l in linha.split():
                if l.isdigit() == True and soma_ativada == True:
                        total += int(l)
                if "=" in linha:
                    print(total)
    except KeyboardInterrupt:
        print("\nSoma interrompida pelo usuário.")
        print(f"Último resultado calculado: {total}")

def menu():
    print("_____________________________________________________________")
    print("|                  Explicação do Programa                   |")
    print("|                                                           |")
    print("| -> Ao digitar ON(de qualquer forma), a soma é ativada     |") 
    print("|                                                           |")
    print("| -> Ao digitar OFF(de qualquer forma), a soma é desativada |") 
    print("|                                                           |")
    print("| -> Ao digitar = a soma calculada é devolvida              |") 
    print("|                                                           |")
    print("|         * Por default, a soma começa ativada *            |") 
    print("|___________________________________________________________|")
    print("Pronto para começar")   
    

def main():
    menu()
    programa_tpc2()


if __name__ == '__main__':
    main()