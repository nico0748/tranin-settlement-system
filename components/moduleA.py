# menu関数作成
def menu():
    i=0
    function =["乗車選択","チャージ機能"]
    print("【ウチダ電鉄 交通系ICカード検証システム】")
    for f in function:
        print(i+1,":",f)
        i=i+1
    print("使用する機能を入力してください(終了する場合は99を入力)")
    func_num=int(input())
    return func_num

menu()