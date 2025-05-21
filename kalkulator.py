import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def multiply(a, b):
    logging.info(f"Działanie to {a:.2f} * {b:.2f}")
    return a * b

def divide(a, b):
    logging.info(f"Działanie to {b:.2f} : {a:.2f}")
    return a / b

def add(a, b):
    logging.info(f"Działanie to {a:.2f} + {b:.2f}")
    return a + b

def subtract(a, b):
    logging.info(f"Działanie to {a:.2f} - {b:.2f}")
    return a - b

def what_operation():
    print("Wybierz jaką operację chcesz wykonać:\n1 Mnożenie, 2 Dzielenie, 3 Dodawanie, 4 Odejmowanie:")
    return input()

def program():
    operation = what_operation()
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    if operation == '1':
        result = multiply(a, b)
    elif operation == '2':
        result = divide(a, b)
    elif operation == '3':
        result = add(a, b)
    elif operation == '4':
        result = subtract(a, b)
    else:
        print("Niepoprawny wybór operacji")
        exit()

    print(f"Wynik to {result:.2f}")
    
program()