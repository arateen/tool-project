
# tool.py - ミニ便利ツール
import random
import random

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def number_guess_game():
    console.print(
        Panel(
            "[bold cyan]1〜100の数字を当ててください！[/bold cyan]\n"
            "正解するまでヒントを出します。",
            title="[bold white]数あてゲーム[/bold white]",
            border_style="cyan",
        )
    )

    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(
                Prompt.ask("[bold yellow]数字を入力してください[/bold yellow]")
            )
        except ValueError:
            console.print(
                "[bold red]数字を入力してください！[/bold red]"
            )
            continue

        if guess < 1 or guess > 100:
            console.print(
                "[bold red]1〜100の範囲で入力してください！[/bold red]"
            )
            continue

        attempts += 1

        if guess < answer:
            console.print(
                "[yellow]もっと大きい数字です！[/yellow]"
            )
        elif guess > answer:
            console.print(
                "[yellow]もっと小さい数字です！[/yellow]"
            )
        else:
            console.print(
                Panel(
                    f"[bold green]正解！[/bold green]\n"
                    f"{attempts}回で当たりました！",
                    title="[bold green]CLEAR![/bold green]",
                    border_style="green",
                )
            )
            break



menu = Table(
    title="ミニ便利ツール",
    border_style="bright_blue",
    show_header=True,
    header_style="bold cyan",
)

menu.add_column("番号", justify="center", style="bold yellow")
menu.add_column("機能", style="white")

menu.add_row("1", "あいさつ")
menu.add_row("2", "整数の足し算")
menu.add_row("3", "文字数カウント")
menu.add_row("4", "数あてゲーム")
menu.add_row("5", "じゃんけん")
menu.add_row("9", "終了")

console.print(menu)

choice = Prompt.ask(
    "[bold cyan]メニュー番号を入力してください[/bold cyan]"
)

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