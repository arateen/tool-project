import random
from rich.console import Console
from rich.panel import Panel

console = Console()

# tool.py - ミニ便利ツール
print("=== ミニ便利ツール ===")
print("1: あいさつ")
print("2: 整数の足し算")
print("3: 文字数カウント")
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
elif choice == "5":
    console.print(Panel.fit("[bold cyan]🎮 じゃんけん勝負 🎮[/bold cyan]", border_style="cyan"))
    console.print("[yellow]1: グー ✊[/yellow] / [green]2: チョキ ✌[/green] / [blue]3: パー 🖐[/blue]")
    
    hands = {"1": "グー ✊", "2": "チョキ ✌", "3": "パー 🖐"}
    user_hand = input("あなたの手を選んでください: ")

    if user_hand not in hands:
        console.print("[bold red]⚠ 1〜3の番号で選んでください。[/bold red]")
    else:
        cpu_hand = random.choice(["1", "2", "3"])
        console.print(f"\nあなた: [bold]{hands[user_hand]}[/bold]  vs  相手: [bold]{hands[cpu_hand]}[/bold]\n")

        if user_hand == cpu_hand:
            console.print(Panel("[bold yellow]結果: あいこです！🤝 もう一回！[/bold yellow]", border_style="yellow"))
        elif (user_hand == "1" and cpu_hand == "2") or \
             (user_hand == "2" and cpu_hand == "3") or \
             (user_hand == "3" and cpu_hand == "1"):
            console.print(Panel("[bold green]結果: あなたの勝ちです！🎉 お見事！[/bold green]", border_style="green"))
        else:
            console.print(Panel("[bold red]結果: あなたの負けです...😢 ドンマイ！[/bold red]", border_style="red"))
elif choice == "9":
    print("終了します。")
else:
    print("未対応のメニューです。")