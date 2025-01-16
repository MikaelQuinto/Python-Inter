n = int(input("Ingrese un número entero positivo: ").strip())

if n % 2 != 0:  # Si es impar
    print("Weird")
else:  # Si es par
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# .strip() = elimina espacios en blanco