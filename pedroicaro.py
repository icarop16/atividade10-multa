# Faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# Se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
velocidade = int(input("Insira a velocidade em Km/h de um veiculo:"))
print(f"A velocidade do veiculo é {velocidade}Km/h ")
Vpermitida = 60*7
if velocidade > 60:
    print (f"A velocidade ({velocidade}km/h) é maior que 60km/h, você recebeu uma multa de { Vpermitida}.")
elif velocidade == 60: 
    print (f"A velocidade ({velocidade}km/h) é igual a 60km/h, você recebeu uma multa de { Vpermitida}.")
else:
    print (f"A velocidade ({velocidade}km/h) é menor que 60km/h, você não recebeu uma multa.")