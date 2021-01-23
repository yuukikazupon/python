
def calcvalue(who,hour,count,value):
    info="割引なし"
    if (hour==15) and (count>=5):
        value=value*0.8
        info="2割引"
    elif (hour==14) and (count>=3):
        value=value*0.9
        info="1割引"
    value=int(value)
    print("{0}さんは{1},{2}円".format(who,info,value))

calcvalue("A",15,3,1200)
calcvalue("B",14,5,2000)
calcvalue("C",15,8,5400)
