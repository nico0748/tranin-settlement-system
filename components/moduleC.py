# pay関数
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
            

