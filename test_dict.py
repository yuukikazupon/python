records={
    'tanaka':72,'yamada':65,'Hirata':100,
    'akai':56,'fukuda':66,'sakai':80}

sum_v=0
for v in records.values() :
    sum_v+=v
ave_v=sum_v/len(records)
print("合計点:",sum_v)
print("平均点:",ave_v)

fmt="|{0:<7}|{1:>4}|{2:>5}"
print("|名前   |点数|差")

for name,v in records.items():
    diff_v=v-ave_v
    diff_v=round(diff_v,1)
    print(fmt.format(name,v,diff_v))
