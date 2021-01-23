# animal_list=[("ライオン",58),("チーター",110),("シマウマ",60),("トナカイ",80)]
# faster_list=sorted(animal_list,key=lambda ani :ani[0])
# for i in faster_list:print(i)
# # print(animal_list[0][1])


animal_dict={"ライオン":58,"チーター":110,"シマウマ":60,"トナカイ":80}
faster_list=sorted(animal_dict.items(),key=lambda ani :ani[1])
print(faster_list)
dict={}
for i ,n in faster_list:

    dict[i]=n
print(dict)
# print(animal_list[0][1])
# a=list(animal_dict.items())
# print(a)
