# menu関数作成
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

if __name__ == "__main__":
    menu()
    