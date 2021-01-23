num=3

masu_num=num*num
masu_list=[]
marubatu_list=["○","×"]

num_list=[i for i in range(1,masu_num+1)]

while True :
    if num_list==[] :
        break
    else:
        masu_list.append(num_list[:num])
        del num_list[:num]


def hyouji() :
    print("譜面")
    for n in range(num):
        fmt="{0:^3}|{1:^3}|{2:^3}"
        print( fmt.format(masu_list[n][0],masu_list[n][1],masu_list[n][2]))

def hyouji_maru() :
    print("○を入れる場所を選んでください")
    for p in range(num):
        for q in range(num):
            if masu_list[p][q] !=marubatu_list[0] and masu_list[p][q] != marubatu_list[1] :
                print(str(masu_list[p][q])+" ",end="")
    print()
    while True:
        try:
            input_line=int(input())
            if input_line == 0:
                print("もう一度入力してください")

            if input_line == 1 :
                if masu_list[0][0] != marubatu_list[0] and masu_list[0][0] != marubatu_list[1]:
                    masu_list[0][0] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")

            elif input_line == 2 :
                if masu_list[0][1] != marubatu_list[0] and masu_list[0][1] != marubatu_list[1]:
                    masu_list[0][1] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==3 :
                if masu_list[0][2] != marubatu_list[0] and masu_list[0][2] != marubatu_list[1]:
                    masu_list[0][2] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==4 :
                if masu_list[1][0] != marubatu_list[0] and masu_list[1][0] != marubatu_list[1]:
                    masu_list[1][0] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==5 :
                if masu_list[1][1] != marubatu_list[0] and masu_list[1][1] != marubatu_list[1]:
                    masu_list[1][1] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==6 :
                if masu_list[1][2] != marubatu_list[0] and masu_list[1][2] != marubatu_list[1]:
                    masu_list[1][2] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==7 :
                if masu_list[2][0] != marubatu_list[0] and masu_list[2][0] != marubatu_list[1]:
                    masu_list[2][0] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==8 :
                if masu_list[2][1] != marubatu_list[0] and masu_list[2][1] != marubatu_list[1]:
                    masu_list[2][1] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==9 :
                if masu_list[2][2] != marubatu_list[0] and masu_list[2][2] != marubatu_list[1]:
                    masu_list[2][2] = marubatu_list[0]
                    break
                else :
                    print("別の場所を選んでください")
        except:
            print("もう一度入力してください")





def hyouji_batu() :
    print("×を入れる場所を選んでください")
    for p in range(num):
        for q in range(num):
            if masu_list[p][q] !=marubatu_list[0] and masu_list[p][q] != marubatu_list[1] :
                print(str(masu_list[p][q])+" ",end="")
    print()
    while True:
        try:
            input_line=int(input())
            if input_line == 0:
                print("もう一度入力してください")
            if input_line == 1 :
                if masu_list[0][0] != marubatu_list[0] and masu_list[0][0] != marubatu_list[1]:
                    masu_list[0][0] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line == 2 :
                if masu_list[0][1] != marubatu_list[0] and masu_list[0][1] != marubatu_list[1]:
                    masu_list[0][1] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==3 :
                if masu_list[0][2] != marubatu_list[0] and masu_list[0][2] != marubatu_list[1]:
                    masu_list[0][2] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==4 :
                if masu_list[1][0] != marubatu_list[0] and masu_list[1][0] != marubatu_list[1]:
                    masu_list[1][0] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==5 :
                if masu_list[1][1] != marubatu_list[0] and masu_list[1][1] != marubatu_list[1]:
                    masu_list[1][1] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==6 :
                if masu_list[1][2] != marubatu_list[0] and masu_list[1][2] != marubatu_list[1]:
                    masu_list[1][2] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==7 :
                if masu_list[2][0] != marubatu_list[0] and masu_list[2][0] != marubatu_list[1]:
                    masu_list[2][0] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==8 :
                if masu_list[2][1] != marubatu_list[0] and masu_list[2][1] != marubatu_list[1]:
                    masu_list[2][1] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
            elif input_line ==9 :
                if masu_list[2][2] != marubatu_list[0] and masu_list[2][2] != marubatu_list[1]:
                    masu_list[2][2] = marubatu_list[1]
                    break
                else :
                    print("別の場所を選んでください")
        except:
            print("もう一度入力してください")


def hantei() :
    k=0
    for n in range(num):
        count_maru_yoko=0
        count_batu_yoko=0

        for m in range(num):
            if masu_list[n][m] == marubatu_list[0] :
                count_maru_yoko+=1
                if count_maru_yoko == num :
                    print("○の勝ち")
                    return 0
                else :
                    k+=1

            elif masu_list[n][m] == marubatu_list[1]:
                count_batu_yoko+=1
                if count_batu_yoko == num:
                    print("×の勝ち")
                    return 0
                else :
                    k+=1

    for n in range(num):
        count_maru_tate=0
        count_batu_tate=0
        for m in range(num):
            if masu_list[m][n] == marubatu_list[0] :
                count_maru_tate+=1
                if count_maru_tate == num :
                     print("○の勝ち")
                     return 0
                else :
                    k+=1

            elif masu_list[m][n] == marubatu_list[1]:
                count_batu_tate+=1
                if count_batu_tate == num:
                    print("×の勝ち")
                    return 0
                else :
                    k+=1

    count_maru2=0
    count_batu2=0

    for r in range(num) :
        if masu_list[r][r] == marubatu_list[0] :
            count_maru2+=1
            if count_maru2 == num :
                print("○の勝ち")
                return 0
            else :
                k+=1

        elif masu_list[r][r] == marubatu_list[1]:
            count_batu2+=1
            if count_batu2 == num:
                print("×の勝ち")
                return 0
            else :
                k+=1


    count_maru1=0
    count_batu1=0

    def gen():
        for p in range(num):
            yield p ;
    it=gen()

    for s in reversed(range(num)):
        for t in it:
            if masu_list[s][t] == marubatu_list[0]:
                count_maru1+=1
                if count_maru1 == num :
                     print("○の勝ち")
                     return 0
                else :
                    k+=1
                    break

            elif masu_list[s][t] == marubatu_list[1]:
                count_batu1+=1
                if count_batu1 == num:
                    print("×の勝ち")
                    return 0
                else :
                    k+=1
                    break
    if k==24 :
        print("あいこ")
        return 0


while True :

    hyouji()
    hyouji_maru()
    h=hantei()
    if h == 0:
        hyouji()
        break
    hyouji()
    hyouji_batu()
    h=hantei()
    if h == 0:
        hyouji()
        break
