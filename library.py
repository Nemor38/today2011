def cm_to_inches(length_in_cm):
    # Перевірка на негативне значення
    if length_in_cm < 0:
        return -1 * cm_to_inches(abs(length_in_cm))

    # Коефіцієнт перетворення
    inches_per_cm = 0.393701

    # Розрахунок довжини в дюймах
    length_in_inches = length_in_cm * inches_per_cm

    # Округлення довжини до двох знаків після коми
    length_in_inches = round(length_in_inches, 2)

    return length_in_inches


# Введення довжини в сантиметрах від користувача
user_input = float(input("Введіть довжину в сантиметрах: "))

# Виклик функції та виведення результату
result = cm_to_inches(user_input)
print(f'{user_input} см = {result} дюймів')
