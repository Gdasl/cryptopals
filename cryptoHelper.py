import itertools
import string

def ready(fi):
    li = []
    fi = open(fi,'r')
    for i in fi.readlines():
        li.append(i.rstrip())
    return li

def htb(s):
    return s.decode("hex").encode("base64")

def isECB(s):
    biggo = []
    flag = 0
    i = 16
    biggo.append(breakblock(s,i))
    for j in biggo:
        combos = itertools.combinations(j,2)
        for k in combos:
                if k[0] == k[1]:
                        flag = 1
    if flag:
        print "Probably ECB"
    else:
        print ":("
                     
def xor(a,b):
    s = ''
    a_ = checkhex(a)
    
    if len(a) == len(b):
        b_ = checkhex(b)
        for i,j in zip(a_,b_):
            s += chr(ord(i)^ord(j))
        
    
    elif len(b) == 1:
        b_ = b
        for i in a_:
            s += chr(ord(i)^ord(b_))
    return s.encode('hex')
        

def check(it,lis):
    a = 0
    for i in it:
        if i in lis:
            a+=1
    return a

def xorfind(s):
    for i in range(255):
        temp = xor(s,chr(i)).decode('hex')
        if len(temp.split(' ')) > 1:
            if check(temp.split(' '),words)>2:
                print temp
                print s
                return temp

def xorarr(arr,ch):
    tmp = []
    for c in arr:
        tmp.append(chr(ord(c)^ord(ch)))

    return tmp

def checkhex(s):
    try:
        s_ = s.decode('hex')
    except Exception as e:
        s_ = s
    return s_

def repxor(a,KEY):
    a_ = checkhex(a)
    KEY_ = checkhex(KEY)
    s = ''
    fl = 0
    for i in a_:
        s += chr(ord(i)^ord(KEY_[fl]))
        fl +=1
        if fl == len(KEY_):
            fl = 0
    return s

def distance(a,b):
    a = checkhex(a)
    b = checkhex(b)
    a_ = bin(int(a.encode('hex'),16))
    b_ = bin(int(b.encode('hex'),16))
    flag = 0
    if len(a_) == len(b_):
        tmp = len(a_)
    else:
        tmp = min(len(a_),len(b_))
        flag = abs(len(a_)-len(b_))
    count = 0
    
    for i in range(tmp):
        if a_[i] != b_[i]:
            count +=1
    if flag:
        count += flag
    return count

def breaky(a,maxi):
    a = checkhex(a)
    temp = []
    ay = {}
    for i in range(2,maxi):
        print distanceKey(a,i), i
        temp.append(distanceKey(a,i))
        ay[distanceKey(a,i)] = i
    return min(temp),ay[min(temp)]
                
def pad(stri,KEYSIZE):
    if len(stri)%KEYSIZE:
        tmp = KEYSIZE - (len(stri)%KEYSIZE)
        stri += chr(tmp)*tmp
    else:
        pass
    return stri
def distanceKey(a,KEYSIZE):
    jj = breakblock(a,KEYSIZE)[:8]
    norm_dists = [distance(pair[0],pair[1]) for pair in itertools.combinations(jj,2)]
    normal_dist = sum(norm_dists)/((float(KEYSIZE) * len(norm_dists)))
    return normal_dist

def breakKeyLen(s,maxL):
    tmp = []
    ay = {}
    for i in range(1,maxL):
        tmp.append(distanceKey(s,i))
        ay[distanceKey(s,i)] = i

    winner = min(tmp)
    return winner, ay[winner]
        
def breakblock(bl,KEYSIZE):
    tmp = []
    for i in range(0,len(bl),KEYSIZE):
        tmp.append(bl[i:KEYSIZE+i])

    std_len = len(tmp[0])
    last_len = len(tmp[len(tmp)-1])
    if last_len != std_len:
        tmparr = tmp[len(tmp)-1]
        lastchar = tmparr[len(tmparr)-1]
        for i in range(0, std_len-last_len):
            tmparr+="\n"
        tmp[len(tmp)-1] = tmparr
        
    return tmp

def inverse(arr):
    return zip(*arr)


def checkprintable(arr):
    ok = [10,32,33]
    bu = True
    for i in arr:
        if (ord(i) < 39 or ord(i) >125) and (ord(i) not in ok):
            bu =  False
            break
            
    return bu

allowedList = [ord('<'),ord('>'),ord('@'),61,93,94,95,96,13]
def checkprintableXtreme(arr):
    bu = True
    for i in arr:
        if i not in string.printable:
            bu =  False
            break
            
    return bu

def constri(arr):
    stri = ""
    for i in arr:
        stri+=i
    return stri
