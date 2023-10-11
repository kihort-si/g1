# проверка числа на соответсвие условию
def check_number(n):
    if n < 1 or n > 100:
        print(("n должно быть 1 <= n <= 100"))
    else:
        sweets(n)

def sweets(n):
    if n % 3 == 0: #если n делится на 3, выиграшная стратегия у First
        print("First")
    else:
        print("Second")

def main():
    n = int(input("Введите n (1 <= n <= 100): "))
    check_number(n)


if __name__ == "__main__":
    main()