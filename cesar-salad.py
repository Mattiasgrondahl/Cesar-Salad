
import operator
import base64
import os, random, string
import codecs
import sys

saved_string = ''

#

def main1(): #Menu goes here
    opt_list = [b64encode, b64decode, main]
    while(True):
        print "\nSELECT OPTION:"
        print "1\tBase 64 Encode"
        print "2\tBase 64 Decode"
        print "0\tBack"

        opt_choice = int(raw_input("SELECTION: "))
        opt_choice -= 1
        opt_list[opt_choice]()

    return


def b64encode():
    Base_string = str(raw_input("Enter String to encode: "))
    B = base64.b64encode(Base_string)
    print "\nPlaintext: " + Base_string
    print "Base 64 encoded: " + B 
    return

def b64decode():
    Base_string = str(raw_input("Enter String to encode: "))
    B = base64.b64decode(Base_string)
    print "Base 64 decoded: " + B
    return

def password():
    length = 26
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))

    print "\nPassword Generated:" + ''.join(random.choice(chars) for i in range(length))

def rot13():
    Base_string = str(raw_input("Enter String to encode: "))
    E =codecs.encode(Base_string, 'rot_13')
    print E

def cesar_enc():
	plaintext = raw_input('Enter plain text message: ')
        i = input('Enter number to shift: ')
        cipher = ''

        for each in plaintext:
		c = (ord(each)+i) % 126
		
		if c < 32: 
			c+=31
			
		cipher += chr(c)
        print 'Your encrypted message is: ' + cipher

def main(): #Menu goes here
    opt_list = [main1, password, rot13, cesar_enc]
    while(True):
        print "\nSELECT OPTION:"
        print "1\tBase 64 encode/decode"
        print "2\tGenerate Password"
        print "3\tRot 13"
        print "4\tCesar"
        opt_choice = int(raw_input("SELECTION: "))
        opt_choice -= 1
        opt_list[opt_choice]()

    return

main()

