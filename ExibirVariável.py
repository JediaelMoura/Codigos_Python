codigo = input("Digite o código do funcionário: ")
nome = input("Digite o nome do funcionário: ")
salario = float(input("Informe o salário: "))
ativo = True
tiposaguineo = input("Digite aqui seu tipo sanguíneo: ")

print("\nAs informações estão corretas?\n")
print("Código: %s "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f "% salario)
print("Ativo: %r "% ativo)
print("Sangue: %s "% tiposaguineo)