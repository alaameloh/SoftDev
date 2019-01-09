import sys
from socket import *
secret = '61aafe1c55b284a98f7637d7b4bbe140\n'

serverHost = 'localhost' # servername is localhost
serverPort = 9999 # use arbitrary port > 1024
s=socket(AF_INET, SOCK_STREAM) # create a TCP socket
s.connect((serverHost, serverPort)) # connect to server on the port

data = s.recv(1024) # receive up to 1K bytes
print data
# who are you ?
s.send('alameloh\n')
print '* alameloh'

data = s.recv(1024)
print data
# tell me your secret 
s.sendall(secret)
print secret

data = s.recv(1024)
print data
#guessing the number using binary search

seq = range(10000)
min = 0
max = len(seq) -1
while True : 
	m = (min + max) //2
	number = str(seq[m])+'\n'
	s.sendall (number)
	data = s.recv(1024)
	if data.split()[-1] == 'smaller' :
		max = m -1
	elif data.split()[-1] == 'bigger' :
		min = m + 1
	else :
		break  

print number
print data

data = s.recv(1024)
print "printing # number"
print data

def count_char(string):
	result = len(string) - string.count(' ')
	return result

def identify ( number) :
	#1 case
	if number[0] == 1 and number[-1] == 5 : return 1 
	#2 case
	if number[-1] == 7 : return 2
    	#4 case
    	if number[3] == 7 : return 4
    	#5 and 7 case
    	if number[0] == 7 :
        	if number[1] == 1 : return 5
        	else : return 7
    	#3,6,8 and 9 case
    	if number[-1]==5 :
        	if number[3]==6 :
            		if number[2]== 1 : return 6
            		else : return 9
        	else :
            		if number[2]==1 : return 3
            		else : return 8    
    	#0 case  
    	if number[0]==3 : return 0

lines = data.split("\n")[:-3]
for key, value in enumerate(lines):
	line = []
	line.append(value[:7])
	tmp = value[7:].lstrip()
	line.append(tmp[:7])
	tmp = tmp[7:].lstrip()
	line.append(tmp)
	lines[key] = line

numbers = []
for line in lines :
	numbers.append([count_char(elem) for elem in line] ) 

number1 = [x[0] for x in numbers]
number2 = [x[1] for x in numbers] 
number3 = [x[2] for x in numbers] 

answer = 100*identify(number1) + 10*identify(number2) + identify(number3)
print(answer)

s.send(str(answer)+'\n')
data = s.recv(1024)
print data
data = s.recv(1024)
print data
obj =  data.split('\n')[1:-3]

import pickle
import datetime

t1 = pickle.loads('\n'.join(obj))
ms = t1.strftime("%f")

s.send(ms + '\n')
data = s.recv(1024)
print data

data = s.recv(1024)
print data

import re
p = re.compile('[0-9]+ [a-zA-Z]{3} [0-9]+')
t0 =  p.search(data).group()
t0 = datetime.datetime.strptime(t0, '%d %b %y')
delta = (t1 - t0).days
print delta

s.send(str(delta)+'\n')
data = s.recv(1024)
print data
data = s.recv(1024)
print data

secret = data.split('\n')
print secret[1]

