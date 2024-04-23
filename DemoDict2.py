# DemoDict2.py 
device = {"아이폰":5, "아이패드":10}
device["맥북"] = 15 
print(device)
device["아이폰"] = 6 
print(device)
del device["아이패드"]
for item in device.items():
    print(item)

#참조형식 연습
phone = {"kim":"111", "lee":"222", "park":"333"}
print("park" in phone)
print("kang" not in phone)
p = phone 
#정수기반의 주소 비슷한 값 리턴 
print( id(phone) )
print( id(p) )

p["kang"] = "123"
print(phone)
print(p)

