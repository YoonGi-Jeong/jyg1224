import random


def get_user_choice():
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
    while user_choice not in ["가위", "바위", "보"]:
        print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 다시 선택하세요.")
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(["가위", "바위", "보"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "비겼다!"
    elif ((user_choice == "가위" and computer_choice == "보") or
          (user_choice == "바위" and computer_choice == "가위") or
            (user_choice == "보" and computer_choice == "바위")):
        return "이겼다!"
    else:
        return "졌다!"


def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"유저: {user_choice}, 컴퓨터: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"결과: {result}\n")

        if result == "이겼다!":
            user_wins += 1
        elif result == "졌다!":
            computer_wins += 1
        else:
            draws += 1

        play_again = input("계속하시겠습니까? (Y/N): ").lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 입력이 아닙니다. 'Y' 또는 'N'을 입력하세요.")

    print("\n게임 종료")
    print(f"이겼다!: {user_wins}, 졌다!: {computer_wins}, 비겼다!: {draws}")


if __name__ == "__main__":
    play_game()
