compra = int (input("Ingrese el valor de la compra:"))

if compra < 500:
    print ("El total a pagares:", compra)

elif 500 <= compra <= 1000:
    compra = compra * 0.90 # Descuento del 10%
    print ("El total a pagar, con su respectivo descuento es:", compra)

elif 1000 < compra <= 2000:
    compra = compra * 0.85 # Descuento del 15%
    print ("El total a pagar, con su respectivo descuento es:", compra)

else: 
    compra = compra * 0.80 # Descuento del 20%
    print ("El total a pagar, con su respectivo descuento es:", compra)
