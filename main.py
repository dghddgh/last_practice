def first():
    print("Привет! Добро пожаловать")
    
def add_numbers(a, b):
    result = a + b
    print(f"Сумма {a} и {b} равна {result}")
    return result

def main():
    first()
    add_numbers(5,7)

if __name__ == "__main__":
    main()