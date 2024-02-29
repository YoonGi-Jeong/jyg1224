import random


def updown_game():
    while True:
        random_number = random.randint(1, 100)
        attempts = 0

        print("1~100까지의 숫자 중 정답을 맞춰 보세요.")

        while True:
            user_input = input("숫자를 입력해주세요.: ")

            if user_input.lower() == 'n':
                print("게임을 종료합니다.")
                break

            try:
                guess = int(user_input)
            except ValueError:
                print("숫자가 아닙니다.")
                continue

            attempts += 1

            if guess == random_number:
                print(f"정답입니다!!!. 시도 횟수: {attempts}\n")
                break
            elif guess < random_number:
                print("UP!")
            else:
                print("DOWN!")

        play_again = input("계속하시겠습니까? (Y/N): ").lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 입력이 아닙니다. 'Y' 또는 'N'을 입력하세요.")


if __name__ == "__main__":
    updown_game()
