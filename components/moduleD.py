# charge関数

def charge(charge_balance):
    charges = []
    for i in range(10):
        charges.append((i + 1) * 1000)
    print("【チャージ機能】")
    print(f"チャージ残高は{charge_balance}円です。")
    for i in range(len(charges)):
        print(f"{i + 1}：{charges[i]}円")
    print("チャージする金額を選択してください。(キャンセルする場合には 99 を入力)")
    choice = int(input())
    if 1 <= choice <= 10:
        charge_amount = choice * 1000
        print(f"{charge_amount}円チャージします。")
        charge_balance += charge_amount
    elif choice == 99:
        print("チャージをキャンセルしました。")
    print(f"チャージ残高は{charge_balance}円です。")
    return charge_balance