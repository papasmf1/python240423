# DemoIndexing.py 
strA = "파이썬은 강력해"
strB = "python is very powerful"

print( len(strA) )
print( len(strB) )
print("abc" + "def")
print( "py" * 3 )

#실행: ctrl + f5 
print(strA[0])
print(strA[1])
print(strA[0:2])
print(strA[:2])
print(strA[-1])
print(strA[-2])
print(strA[-2:])


print("---리스트형식---")
colors = ["red", "blue", "green"]
print( type(colors) )
print( colors )
colors.append("yellow")
print( colors )
colors.insert(1, "pink")
print( colors )
print( len(colors) )
print( colors.index("red") )
colors.remove("red")
print( colors )
colors.sort()
print( colors )
colors.reverse()
print( colors )


