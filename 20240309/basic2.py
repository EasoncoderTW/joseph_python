# list / tuple / set / dict

# list [] : 串列 最多功能
a = list() # empty # declare
x = [1,2,3] # declare
print(a)
print(x)
# append
x.append(4) # rear
print(x)
# sort
unsort_list = [20,51,30,62,20,30] # declare
unsort_list.sort() #　排序(正向小到大)
print(unsort_list)
unsort_list.sort(reverse=True) #　排序(反向大到小)
print(unsort_list)
# extend
list_1 = ["Eason", "Billy", "Mark"]
list_2 = ["Joseph", "John"]
list_concat = list_1 + list_2 # declare
print("list_concat",list_concat)
list_1.extend(list_2) # 吃進去
print("list_1",list_1)
list_1.append(list_2) # 囫圇吞棗(NOTE!!!)
print("list_1",list_1)
#-------------------------------------------------------
# tuple () : 元組(打包)
b = tuple() # empty
tuple_1 = (5,6,4) # declare

x,y,z = tuple_1 # extract: 數量要剛好
tuple_1 = (x,8,z) # 重新更改

print(x)
print(y)
print(z)
#-------------------------------------------------------
# set {} : 集合(不重複)
c = set() # empty

c.add(1)
print("SET = ",c)
c.add(2)
c.add(3)
print("SET = ",c)
c.add(3) # ignore
c.add(4)
print("SET = ",c)

#-------------------------------------------------------
# dict {:} : 字典(查表)
d = dict() # empty

dict_1 = {
    "Eason":80,
    "Billy":90
}

# { key1:value1 ,key2:value2 ,... } 定義
# d[key]->value 使用

print("dict_1",dict_1["Eason"])
print("dict_1",dict_1["Billy"]) # force
print("dict_1",dict_1.get("Mark",0)) # try to get value using key

print(dict_1.keys())
print(dict_1.values())

#-----------------------
# list/ tuple -> slice 切片(從...切到...)
# list[from:to], from(encluded), to(excluded)

list_data = ["Eason","Amy","Jack","Tom","Billy","Mark","Cindy"]
print("list_data[0:3]",list_data[0:3])
print("list_data[3:6]",list_data[3:6]) # 6可寫:限制範圍

# list[0:a] -> list[:a]
# list[b:最後一項] -> list[b:]list_data
print("list_data top three",list_data[:3])
print("list_data last tow",list_data[4:]) # 4受限於總數為6

# 倒數index
print("list_data[-1]",list_data[-1])
print("list_data[-2]",list_data[-2])
print("list_data[-3]",list_data[-3])

# 倒數slice
print("list_data last tow",list_data[-2:]) #總數不限，只取最後兩個
