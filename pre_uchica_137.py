from components import moduleA as ma
from components import moduleB as mb
from components import moduleC as mc
from components import moduleD as md

def main():
    # チャージ金額の初期値は500
    charge_balance = 500
    user_input = "0"

    while True:
        try:
            if user_input == "q":
                print("プログラムを終了します。")
                break # ループを抜けて終了する

            menu_num = ma.menu()
            if menu_num == 1 :
                destination = mb.select_station()
                mc.pay(charge_balance, destination)
            elif menu_num ==2 :
                charge_balance = md.charge(charge_balance)
            elif menu_num == 99:
                continue
        except:
            print("正しい数値を入力してください。")
            continue
            


if __name__ == "__main__":
    main()