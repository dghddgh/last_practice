def first():
    print("Привет! Добро пожаловать")
    
def add_numbers(a, b):
    result = a + b
    print(f"Сумма {a} и {b} равна {result}")
    return result
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    first()
    add_numbers(5,7)
    print(f"Факториал числа 5: {factorial(5)}")
    


if __name__ == "__main__":
    main()