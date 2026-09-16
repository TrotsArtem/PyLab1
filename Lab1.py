import math

def task1():
    x = float(input("Enter a number: "))

    if x > 45:
        z = -math.sqrt(x)
    elif x <= 45:
        z = math.sin(math.radians(2*x))

    print(f"Значення z({x}) = ({z})")

def task2():
    p = float(input("Введіть число: "))
    a, b = 0, 1
    while b <= p:
        a, b = b, a+b

    print(f"Перше число Фібоначчі, яке більше за {p}: {b}")

def task3():
    arr = [12, -4, 7, -8, -15, 0, -2, 9, -6]

    max_element = max(arr)

    negative_elements = [x for x in arr if x < 0]

    if negative_elements:
        avg_negative = sum(negative_elements) / len(negative_elements)
    else:
        avg_negative = "Від'ємні елементи відсутні"

    even_negatives_reversed = [x for x in arr if x < 0 and x % 2 == 0][::-1]

    # Вивід результатів
    print(f"1. Максимальний елемент: {max_element}")
    print(f"2. Середнє арифметичне від'ємних елементів: {avg_negative}")
    print(f"3. Парні від'ємні елементи у зворотному порядку: {even_negatives_reversed}")

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