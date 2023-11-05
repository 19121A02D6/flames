import time
def about_us():
    print("PYTHON PROJECT\nEEE--B\nROLLNO        NAME     \n19121A02A2    M.SRI CHARITHA\n19121A0277    K.RAKESH\n19121A02B6    N.NIKHILA\n19121A0296    K.VENKATAGANESH\n19121A02D6    P.KARUNAKAR RAO    ")

def split_to_list(NAME_A,NAME_B):
    a=[]
    b=[]
    for i in NAME_A:
        if i.isalpha():
            a.append(i)
        else:
                continue
    for j in NAME_B:
        if j.isalpha():
            b.append(j)
        else:
                continue
    return a,b

NAME_A=input('enter the boy name=').lower()
NAME_B =input('enter the girl name=').lower()
def remove_common_words(a,b):
    for k in a:
        for l in b:
            if k==l:
                if k in a:
                    a.remove(k)
                else:
                     continue
                if l in b:
                    b.remove(l)
                else:
                     continue
            else:
                 continue
        return a,b

def result(List,rem):
    while len(List)>1:
        num=rem%len(List)
        if num>0:
            m=List[num::1]
            n=List[0:num-1:1]
            List.clear()
            List=m+n
        elif num==0:
             List.pop()

    return List
List =  ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
Z,Y=split_to_list(NAME_A,NAME_B)
a,b=remove_common_words(Z,Y)
rem=len(a)+len(b)
print(NAME_A,' ',result(List,rem),' ',NAME_B)
time.sleep(10)
result(List,rem)
