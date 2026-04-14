def main():
    m = int(input("m: "))
    print(f"E: {calculator(m)}")

def calculator(m):
    c = 300000000
    return m * c**2 # El doble ** es el operador de potencia en Python, por lo que c**2 calcula el cuadrado de la velocidad de la luz.

main()