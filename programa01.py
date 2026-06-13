name = "homem cavalo salamaleico"
surname = "da silva"
height = 1.77
age = 23
legal_age = bool
print(f"olá {name} {surname}, idade {age}, altura {height}")
print("primeira instancia de prints acima")
print("segunda instancia de prints abaixo")

age = int(input("insira a idade: "))

if age >= 18:
    legal_age = True
    print("Já pode ser preso kkkkkkkk")
if legal_age == True:
    print("você é maior de idade")