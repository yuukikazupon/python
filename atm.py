# システム
#疑似暗証番号：1234
passcord = '1234'


#メニュー選択
print("メニューを選んでください")
print("1: 引き出し 2:預け入れ 3:残高照会")
menu = input("メニュー番号入力>")

def passcordinput():
    print("暗証番号を入力してください")
    global user_pass
    user_pass=input("暗証番号>")
    return user_pass

#引き出し機能の時
if menu == '1':

    #暗証番号機能
#     print("暗証番号を入力してください")
#     user_pass = input("暗証番号>")
    passcordinput()
    if user_pass == passcord:

        #引き出し処理
        print("引き出す金額を入力してください")
        withdraw = int(input("引き出し金額>"))
        if withdraw < cash:

            #引き出し完了処理
            cash -= withdraw
            print("現金を受け取りください")
            print("残高は"+ str(cash) +"円となります")
            print("ご利用ありがとうございました")

        else:
            print("引き出し金額が超過しています")
            print("最初からやり直してください")

    else:
        print("暗証番号が違います")
        print("最初からやり直してください")

#預入機能の時
elif menu == '2':

    #暗証番号機能
#     print("暗証番号を入力してください")
#     user_pass = input("暗証番号>")
    passcordinput()
    if user_pass == passcord:

        #預入処理
        print("現金をお入れください")
        savings = int(input("預入金額>"))
        cash += savings
        print("残高は"+ str(cash) +"円となります")
        print("ご利用ありがとうございました")

    else:
        print("暗証番号が違います")
        print("最初からやり直してください")

#残高照会機能の時
elif menu == '3':

    #暗証番号機能
#     print("暗証番号を入力してください")
#     user_pass = input("暗証番号>")
    passcordinput()
    if user_pass == passcord:

        #残高照会処理
        print("残高は"+ str(cash) +"円となります")
        print("ご利用ありがとうございました")

    else:
        print("暗証番号が違います")
        print("最初からやり直してください")
