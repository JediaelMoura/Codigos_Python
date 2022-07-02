def lernotas():
    n=float(input("Digite uma nota para o aluno(a): "))
    return n



def resultado(n1,n2,n3):
    media=(n1+n2+n3) / 2
    print("1ª Avaliação: ",n1)
    print("2ª Avaliação: ", n2)
    print("Recuperação: ", n3)
    print("Média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
c = lernotas()
resultado(a, b, c)