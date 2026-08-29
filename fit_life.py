print("Привет, я твой фитнес-бот!")
user_name = input("Как тебя зовут? ")
print(f"Приятно познакомиться, {user_name}!")
user_age = int(input("Сколько тебе лет? "))
print(f"Отлично! Тебе {user_age} лет. Скоро будем считать калории!")
user_weight = float(input("Твой вес в кг (например: 67.67): "))
user_height = float(input("Твой рост в метрах (например: 1.67): "))
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi,1)
water_l = (user_weight * 30)/1000
print("\n--- Твой фитнес-отчёт ---")
print(f"Пользователь: {user_name} ({user_age} лет)")
print(f"Индекс массы тела (ИМТ): {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.2f} л в день")
print("--------------------------")
print("Вот твой отчет. Молодец, что интересуешься и думаешь о здоровье!")


