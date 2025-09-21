nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota"))
média = (nota1 + nota2 + nota3) / 3
frequencia = int(input("digite a frequencia (%):"))

if média < 6:
    print("ALUNO REPROVOU POR NOTA")
else:
    print("ALUNO PASSOU EM NOTA")
if frequencia < 50:
    print("ALUNO REPROVOU POR FALTA")
else:
    print("ALUNO PASSOU EM PRESENÇA")