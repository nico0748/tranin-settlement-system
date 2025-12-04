#select_station関数

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
            if user_input == 99:
                print("駅の選択をキャンセルしました。")
                return 0
            elif user_input in [1, 2, 3]:
                destination = user_input - 1
                return destination
            else:
                print("正しい数値を入力してください")
        except ValueError:
            print("数値を入力してください。")
    
if __name__ == "__main__":
    select_station()