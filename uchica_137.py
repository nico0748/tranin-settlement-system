def menu():
    i=0
    function =["乗車選択","チャージ機能"]
    option_num = int(len(function))

    print("【ウチダ電鉄 交通系ICカード検証システム】")
    for i in range(option_num):
        print(str(i+1) + ":" + function[i])
        i=i+1
    print("使用する機能を入力してください(終了する場合は99を入力)")
    func_num=int(input())
    return func_num


def select_station():
    i = 0
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]

    print("--- 【乗車駅選択】 ---")
    for i in range(len(stations)):
        #i: [staions]まで[fares]円
        print(str(i+1) + ":" + stations[i] + "まで" + str(fares[i]) + "円")
    
    while True:
        try:
            user_input = int(input("乗車した駅を入力してください（キャンセルする場合には99を入力）"))
            if user_input in [1, 2, 3]:
                destination = user_input - 1
                return destination
            elif user_input == 99:
                print("駅の選択をキャンセルしました。")
                return 0
            else:
                print("正しい数値を入力してください")
        except ValueError:
            print("数値を入力してください。")


def pay(charge_balance, destination):
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]

    print("チャージ残高は"+str(charge_balance)+"円です")

    if charge_balance < 500:
        print("残高が500 円未満のため3000 円自動チャージします。")
        charge_balance += 3000
        print("チャージ残高は"+str(charge_balance)+"円です。")
    
    if fares[destination] > charge_balance:
        while charge_balance <= fares[destination]:
            print("残高不足です")
            print("3000円自動チャージします。")
            charge_balance += 3000
    
    charge_balance -= fares[destination]
    print("精算後のチャージ残高は"+str(charge_balance)+"円です。")
    
    return charge_balance

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
    


def main():
    # チャージ金額の初期値は500
    charge_balance = 500

    while True:
        try:
            menu_num = menu()
            
            if menu_num == 1:
                destination = select_station()
                if destination != -1:
                    charge_balance = pay(charge_balance, destination)
            elif menu_num == 2:
                charge_balance = charge(charge_balance)
            elif menu_num == 99:
                print("プログラムを終了します。")
                break  # ループを抜けて終了する
            else:
                print("1, 2, 99 のいずれかを入力してください。")

        except ValueError:
            print("正しい数値を入力してください。")
            continue
            


if __name__ == "__main__":
    main()