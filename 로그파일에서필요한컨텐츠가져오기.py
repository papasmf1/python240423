#정규표현식 사용 
import re 

#원본 로그 파일 
source=open('c:\\work\\PV3.txt','rt')
#복사본 생성 
mycopy=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = source.readline()
while (line != ''):
    if (re.search(r"error", line)):
        mycopy.write(line + "\n")
    line = source.readline()

source.close() 
mycopy.close()








