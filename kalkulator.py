import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

print("Wybierz jaką operację chcesz wykonać: 1 Mnożenie, 2 Dzielenie, 3 Dodawanie, 4 Odejmowanie:")
operation = input()

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
if operation == '1':
    logging.info(f"Działanie to {a:.2f} * {b:.2f}")
    result = a * b
elif operation == '2':
    logging.info(f"Działanie to {b:.2f} : {a:.2f}")
    result = a / b
elif operation == '3':
    logging.info(f"Działanie to {a:.2f} + {b:.2f}")
    result = a + b
elif operation == '4':
    logging.info(f"Działanie to {a:.2f} - {b:.2f}")
    result = a - b
else:
    print("Niepoprawny wybór")
    exit()

print(f"Wynik to {result:.2f}")