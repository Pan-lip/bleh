Velocidade= float(input("Digite velocidade do carro em km/h:"))
if Velocidade > 80:
    excesso = Velocidade - 80
    multa = excesso * 5
    print (" Você foi multado! O valor é  R$ {multa: .2f")

