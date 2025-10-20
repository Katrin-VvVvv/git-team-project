
def guess_the_number():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    print(f"Я загадал число от {lower_bound} до {upper_bound}. Попробуйте угадать!")
    attempts = 0

    while True:
        try:
            user_guess = int(input("Ваше число: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
                break
            elif user_guess < secret_number:
                print("Слишком мало! Попробуйте больше.")
            else:
                print("Слишком много! Попробуйте меньше.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

guess_the_number()

