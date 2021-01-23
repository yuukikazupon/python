value=100

def changevalue():
    # print(value)
    global value
    print(value)
    value=20
    print(value)

changevalue()
print("value=",value)
