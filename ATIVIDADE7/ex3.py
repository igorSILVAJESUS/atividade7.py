def obter_convidados():
    convidados = []
    while True:
        nome = input("Digite o nome do convidado (ou 'fim' para terminar): ")
        if nome.lower() == 'fim':
            break
        convidados.append(nome)
    return convidados

def main():
    convidados = obter_convidados()

    convidados_unicos = sorted(set(convidados))
   
    print("Lista final de convidados (sem duplicatas e ordenada):", convidados_unicos)

if __name__ == "__main__":
    main()
    