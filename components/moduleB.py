#select_station関数

def select_station():
    i = 0
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]

    print("--- 【乗車駅選択】 ---")
    for i in range(len(stations)):
        #i: [staions]まで[fares]円
        print(str(i) + ":" + stations[i] + "まで" + str(fares[i]) + "円")
    st_num = int(input("乗車した駅を入力してください（キャンセルする場合には99を入力）"))
    print(st_num)
    return st_num
    
if __name__ == "__main__":
    select_station()