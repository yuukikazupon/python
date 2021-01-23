key="find"
with open("mt7_7.txt","r",encoding="utf-8") as tf:
    for i,line in enumerate(tf):
        if line.find(key) >=0:
            a=line.find(key)
            print(a)
            print(i+1, ":",line)
