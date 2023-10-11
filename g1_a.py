# проверка чисел на соответсвие условию
def check_numbers(m, n):
    if m < 1:
        print("m должно быть >= 1")
    elif n > 10:
        print("n должно быть <= 10")
    else:
        chocolate(m, n)


# построим шоколадку
def chocolate(m, n):
    size = m * n  # размер шоколадки
    min_count_of_turns = size - 1  # минимальное кол-во ходов = (m * n) - 1
    if min_count_of_turns % 2 == 1:
        print("First")
    else:
        print("Second")


def main():
    m = int(input("Введите m >= 1: "))
    n = int(input("Введите n <= 10: "))
    check_numbers(m, n)


if __name__ == "__main__":
    main()