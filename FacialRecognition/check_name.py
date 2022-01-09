import pandas as pd

name_find = input("input name to search")
print(name_find)

data = pd.read_csv('records.csv', header=0)
col_name = list(data.Name)
#print(col_name)

for i in range(0, len(col_name)):
    if name_find == col_name[i]:
        found = 1
        break
    else:
        found = 0

if found == 1:
    print('found')
else:
    print('not found')