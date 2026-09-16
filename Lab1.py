import math

def task1():
    x = float(input("Введіть число: "))

    if x > 45:
        z = -math.sqrt(x)
    else:
        z = math.sin(math.radians(2*x))

    print(f"Значення z({x}) = ({z})")

def task2():
    p = float(input("Введіть число: "))
    a, b = 0, 1
    while b <= p:
        a, b = b, a+b

    print(f"Перше число Фібоначчі, яке більше за {p}: {b}")

def task3():
    n = int(input("Введіть кількість елементів масиву: "))

    print(f"Введіть {n} елементів через пробіл або по одному:")
    arr = []
    while len(arr) < n:
        items = input().split()
        for item in items:
            if len(arr) < n:
                arr.append(int(item))

    max_element = max(arr)

    neg_elements = [x for x in arr if x < 0]

    if neg_elements:
        avg_neg = sum(neg_elements) / len(neg_elements)
    else:
        avg_neg = "Від'ємні елементи відсутні"

    even_neg_rev = [x for x in arr if x < 0 and x % 2 == 0][::-1]

    print(f"1. Максимальний елемент: {max_element}")
    print(f"2. Середнє арифметичне від'ємних елементів: {avg_neg}")
    print(f"3. Парні від'ємні елементи у зворотному порядку: {even_neg_rev}")

def main_menu():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1 - Завдання 1")
        print("2 - Завдання 2")
        print("3 - Завдання 3")
        print("0 - Вихід")

        choice = input("Виберіть дію: ")

        match choice:
            case "1":
                task1()
            case "2":
                task2()
            case "3":
                task3()
            case "0":
                print("До побачення!")
                break  # Вихід з програми
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()