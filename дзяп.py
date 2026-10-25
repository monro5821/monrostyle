import random
import time

def roll_dice(num=6):
    """Бросает заданное количество кубиков."""
    return sorted([random.randint(1, 6) for _ in range(num)])

def print_slow(text, delay=1.0):
    """Выводит текст с небольшой задержкой."""
    print(text)
    time.sleep(delay)

def main():
    print_slow("Добро пожаловать в игру 'Перудо'.", 1)
    print_slow("У каждого игрока по 6 кубиков. Всего на столе их 12.", 1.5)
    print_slow("Бросок кубиков...", 1.5)

    player_dice = roll_dice()
    pc_dice = roll_dice()

    print_slow(f"\nВаши кубики: {player_dice}")
    print_slow("Кубики компьютера скрыты.\n", 1)

    current_n = 0
    current_m = 0
    last_bidder = None
    caller = None

    while True:
        # Ход игрока
        if current_n > 0:
            print(f"Текущая ставка: {current_n} кубиков номиналом {current_m}.")
        else:
            print("Ваш ход первый.")
            
        action = input("Введите ставку (количество и номинал через пробел, например '3 4') или 'не верю': ").strip().lower()

        if action == 'не верю':
            if current_n == 0:
                print("Ставок еще не было. Сделайте первую ставку.\n")
                continue
            print_slow("\nИгрок говорит: не верю.", 1)
            caller = 'Игрок'
            break

        try:
            parts = action.split()
            if len(parts) != 2:
                raise ValueError
            
            n, m = int(parts[0]), int(parts[1])

            if not (1 <= m <= 6):
                print("Номинал должен быть от 1 до 6.\n")
                continue
            if n < 1:
                print("Количество должно быть больше 0.\n")
                continue

            # Правила повышения ставки:
            # Требуется либо увеличить количество кубиков, либо оставить количество прежним, но увеличить номинал.
            if n > current_n or (n == current_n and m > current_m):
                current_n, current_m = n, m
                last_bidder = 'Игрок'
            else:
                print("Ставка должна быть выше предыдущей.\n")
                continue
        except ValueError:
            print("Некорректный ввод. Ожидается два числа через пробел или фраза 'не верю'.\n")
            continue

        # Ход компьютера
        print_slow("\nХод компьютера...", 1.5)

        # Подсчет кубиков текущего номинала у компьютера
        pc_has_m = pc_dice.count(current_m)
        
        # Условие недоверия: ставка значительно превышает количество известных компьютеру кубиков
        if current_n > 0 and (current_n - pc_has_m >= 4 or current_n >= 7):
            # Вероятность случайного недоверия для вариативности игры
            if random.random() > 0.2:
                print_slow("Компьютер говорит: не верю.", 1)
                caller = 'Компьютер'
                break

        # Логика повышения ставки компьютером
        if current_m < 6 and random.choice([True, False]):
            # Поднимает номинал при том же количестве
            current_m += 1
        else:
            # Поднимает количество, номинал выбирается случайно от 1 до 6
            current_n += 1
            current_m = random.randint(1, 6)

        print_slow(f"Компьютер ставит: {current_n} шт. номиналом {current_m}\n", 1)
        last_bidder = 'Компьютер'


    # Финал и подсчет результатов
    print_slow("\n=== Вскрытие кубиков ===", 1)
    print_slow(f"Ваши кубики: {player_dice}", 1)
    print_slow(f"Кубики компьютера: {pc_dice}", 1.5)

    total_dice = player_dice + pc_dice
    actual_count = total_dice.count(current_m)

    print_slow(f"\nВсего кубиков номиналом '{current_m}' на столе: {actual_count}")
    print_slow(f"Последняя ставка была: {current_n}", 1.5)

    # Определение победителя:
    # Если фактическое количество больше или равно ставке, побеждает сделавший ставку.
    # Если фактическое количество меньше ставки, побеждает сказавший "не верю".
    if actual_count >= current_n:
        print_slow("\nСтавка сыграла.", 1)
        if last_bidder == 'Игрок':
            print("Победил игрок: ставка оказалась верной.")
        else:
            print("Победил компьютер: кубиков оказалось достаточно.")
    else:
        print_slow("\nСтавка не сыграла.", 1)
        if caller == 'Игрок':
            print("Победил игрок: блеф компьютера раскрыт.")
        else:
            print("Победил компьютер: ваш блеф раскрыт.")

if __name__ == "__main__":
    main()