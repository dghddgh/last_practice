def first():
    print("Салют!")
    
def add_numbers(a, b):
    result = a + b
    print(f"Сумма {a} и {b} будет {result}")
    return result
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def reverse_string(s):
    reversed_s = s[::-1]
    print(f"Обратная строка для '{s}': '{reversed_s}'")
    return reversed_s
    
def main():
    first()
    add_numbers(5,7)
    print(f"Факториал числа 5: {factorial(5)}")
    reverse_string("Окак")
    


if __name__ == "__main__":
    main()