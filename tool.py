
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

# tool.py - ミニ便利ツール
print("=== ミニ便利ツール ===")
print("1: あいさつ")
print("2: 整数の足し算")
print("3: 文字数カウント")
print("4: 数あてゲーム")
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
elif choice == "9":
    print("終了します。")
else:
    print("未対応のメニューです。")