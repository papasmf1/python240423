# DemoFile.py 

#쓰기(유니코드 글자를 읽기,쓰기) 
#raw string notation: r
#f = open(r"c:\work\test2.txt", "wt", encoding="utf-8")
f = open("c:/work/test2.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#읽기 
#f = open(r"c:\work\test2.txt", "rt", encoding="utf-8")
f = open("c:/work/test2.txt", "rt", encoding="utf-8")
result = f.read() 
print(result)

print("---readline()---")
#다시 처음으로 돌아가서 읽기 
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

#전체를 읽어서 리스트 리턴 
print("---readlines()---")
f.seek(0)
result = f.readlines()
print(result)

f.close() 

#기존 파일에 첨부: append + read + write 
f = open(r"c:\work\test2.txt", "a+", encoding="utf-8")
f.write("추가 데이터\n")
f.close() 


