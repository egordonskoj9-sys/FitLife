ML_PER_KG = 30       # Норма воды: 30 мл на 1 кг веса
ML_IN_LITER = 1000   # В одном литре 1000 миллилитр

print("Привет, я твой фитнес-бот!")
user_name = input("Как тебя зовут? ").strip()
print(f"Приятно познакомиться, {user_name}!")
while True:
    try:
        age_input = input("Введите ваш возраст (только число): ")
        age = int(age_input)
        break
    except ValueError:
        print("Ошибка: возраст должен быть числом! Попробуйте ещё раз.")
while True:
    try:
        weight_input = input("Введите ваш вес в кг (например, 67.67): ")
        user_weight = float(weight_input)
        break
    except ValueError:
        print("Ошибка: вес должен быть числом! Попробуйте ещё раз.")
while True:
    try:
        height_input = input("Введите ваш рост в метрах (например, 1.67): ")
        user_height = float(height_input)
        break
    except ValueError:
        print("Ошибка: рост должен быть числом! Попробуйте ещё раз.")
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)
water_l = (user_weight * ML_PER_KG) / ML_IN_LITER
print("\n--- Твой фитнес-отчёт ---")
print(f"Пользователь: {user_name} ({age} лет)")
print(f"Индекс массы тела (ИМТ): {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.2f} л в день")
print("--------------------------")
print("Вот твой отчет. Молодец, что интересуешься и думаешь о здоровье!")
