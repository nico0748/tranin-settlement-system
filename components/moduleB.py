#select_station関数

def select_station():
    i = 0
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]

    print("--- 【乗車駅選択】 ---")
    for i in range(len(stations)):
        #i: [staions]まで[fares]円
        print(str(i+1) + ":" + stations[i] + "まで" + str(fares[i]) + "円")
    destination = int(input("乗車した駅を入力してください（キャンセルする場合には99を入力）"))-1
    if destination == 99-1:
        print("駅の選択をキャンセルしました。")
        return 0
    return destination
    
if __name__ == "__main__":
    select_station()