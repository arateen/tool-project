
# tool.py - ミニ便利ツール
import random


def number_guess_game():
    print("\n=== 数あてゲーム ===")
    print("1〜100の数字を当ててください！")

    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("数字を入力してください: "))
        except ValueError:
            print("数字を入力してください！")
            continue

        if guess < 1 or guess > 100:
            print("1〜100の範囲で入力してください！")
            continue

        attempts += 1

        if guess < answer:
            print("もっと大きい数字です！")
        elif guess > answer:
            print("もっと小さい数字です！")
        else:
            print(f"正解！{attempts}回で当たりました！")
            break


print("=== ミニ便利ツール ===")
print("1: あいさつ")
print("2: 整数の足し算")
print("3: 文字数カウント")
print("4: 数あてゲーム")
print("5: じゃんけん")
print("9: 終了")

choice = input("メニュー番号を入力してください: ")

if choice == "1":
    print("こんにちは！Gitチーム開発演習中です。")

elif choice == "2":
    num1 = int(input("1つ目の数: "))
    num2 = int(input("2つ目の数: "))
    print("計算結果:", num1 + num2)

elif choice == "3":
    text = input("文字列を入力してください: ")
    print("文字数:", len(text))

elif choice == "4":
    number_guess_game()

elif choice == "5":
    print("\n--- じゃんけん ---")
    print("1: グー / 2: チョキ / 3: パー")

    hands = {"1": "グー", "2": "チョキ", "3": "パー"}
    user_hand = input("あなたの手を選んでください: ")

    if user_hand not in hands:
        print("1〜3の番号で選んでください。")
    else:
        cpu_hand = random.choice(["1", "2", "3"])
        print(f"あなた: {hands[user_hand]} vs 相手: {hands[cpu_hand]}")

        if user_hand == cpu_hand:
            print("結果: あいこです！")
        elif (
            (user_hand == "1" and cpu_hand == "2")
            or (user_hand == "2" and cpu_hand == "3")
            or (user_hand == "3" and cpu_hand == "1")
        ):
            print("結果: あなたの勝ちです！🎉")
        else:
            print("結果: あなたの負けです...😢")

elif choice == "9":
    print("終了します。")

else:
    print("未対応のメニューです。")