# DemoDict.py 
colors = {"apple":"red", "banana":"yellow"}

print(colors)
print(len(colors))
print(colors["apple"])

#입력 
colors["kiwi"] = "green"
print(colors)

#반복
for item in colors.items():
    print(item)

print("---변수 2개로 받기---")
for k,v in colors.items():
    print(k, v)




