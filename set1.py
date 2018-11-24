from cryptoHelper import *
from Crypto.Cipher import AES
from Crypto import Random
import itertools

chall = ready('4.txt')

testsentence = "go big or go home!"
testcode = repxor(testsentence,'ice')
words = ready('wordlist.txt')

a = 'this is a test'
b ='wokka wokka!!!'    
#Challenge 8

eight = open('8.txt')
aline = [line.rstrip() for line in eight]
biggo = []
for i in aline:
    biggo.append(breakblock(i.decode('hex'),16))
found = []


for i in biggo:
    combos = itertools.combinations(i,2)
    for k in combos:
	    if k[0] == k[1]:
		    print "found"
		    found.append(i)

    
#Challenge 7
seven = open('7.txt').read().decode('base64')
KEY = "YELLOW SUBMARINE"

cipher = AES.new(KEY, AES.MODE_ECB)
cipher.decrypt(seven)




#Challenge 6
six = open('6.txt').read()
six = six.decode('base64')
def go():
    actual = breakblock(six,29)
    jiji = inverse(actual)
    stri = ''
    loss = []
    tempi = []
    for j in jiji:
        flag = 1
        for i in range(255):
            
            if checkprintable(xorarr(j,chr(i))):
##                    print xorarr(j,chr(i))
                    tempi.append(xorarr(j,chr(i)))
##                    print "key: " +str(i)
                    stri+=chr(i)
                    flag = 0
        if flag:
             loss.append(j)

    if len(stri) != len(jiji):
        print "Warning, string not complete"
    return stri, tempi,loss
    

