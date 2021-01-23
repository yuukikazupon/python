import random

cpu=random.randint(1,3)
# print(cpu)

# te={1:"グー",2:"チョキ",3:"パー"}
te=["グー","チョキ","パー"]


def shobu(input_te):
    hantei=((input_te-cpu)+3)%3
    if hantei == 0 :
        print("あいこ")
    elif hantei ==1 :
        print("負け")
    else :
        print("勝ち")

while True:
    print("ルール")
    for i,n in enumerate(te):
        print(str(i+1)+":"+n)

    try:
        input_te=int(input("番号を入力してください:"))

        if input_te < 1 or input_te > 3 :
            print("１から３までの番号を入力してください")
        else:
            print("あなたの手",te[input_te-1])
            print("コンピュータの手",te[cpu-1])

            shobu(input_te)

            input_line=input("続けますか？:y:はい n:いいえ:")

            if input_line == "y" or input_line=="Y" :
                pass
            else :
                print("終了")
                break
    except:
        print("入力し直してください")
        pass
