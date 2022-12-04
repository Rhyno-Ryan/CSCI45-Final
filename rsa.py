import math
from random import *
from sympy import mod_inverse
die = SystemRandom() #A dice to pick random #'s 





#How does Miller Rabbin's Prime test work?
#   In search for primes Miller Rabbin's test works as follows
#   Assume, we pick a number, n, that is prime
#   We can input this number in to a function g(x)

#   Where inside of g(x), we will use Fermat's Little Theorem
#       This states that if 'n' is prime, then 
#       a^n = a mod(n) 
#       -> a^(n-1) = 1 mod(n) 
#       -> a^(n-1) - 1 = 0 mod(n) 
#   Although, not completely true, what can be said is
#   if we have a non-zero mod(n) value, for a^(n-1) - 1...
#   n is guaranteed to be composite (not prime)
#   Therefore, in essence we can not guarantee primality, BUT,
#   INCREASE THE LIKELYHOOD OF PRIMALITY

#   Picking a number, a, where 1 < a < n - 1
#   We can expand the given formula using a diff of two squares
#   a^(n-1) - 1 = 0 mod(n)
#   ->[a^(n-1/(2^k)) - 1][a^(n-1/(2^k)) +1] ... [a^(n-1)/2 + 1] = 0 mod(n)
#       ... the k'th iterations assumes the power is now odd

#   after going through the test with a single 'a' we have the probality of 
#   3/4 that n is prime, 1/4 n is composite
#   Now if the test is done multiple times the probablity of being compsite is now
#   1/16
#   again...
#   1/64
#   then so forth

#   MY PROGRAM FOLDS AT 2^7 BITS



#Encryption
#   convert a text to a number(s) - b
#   pair of numbers as a public key (e, N)
#   b^e(mod N) -> gives cypher text B
#   convert B to a number -> B'

#Decryption
#   Given a key (d,N)
#   B'^d(mod N) -> this is spit out the orignal text





#How does it work?
#   pick two prime numbers (p,q)
#   Get a product of p,q called "N"

#   Euler toitient function - phi(N) 
#   phi(N) = (p - 1)(q - 1)... tells you how many coprime numbers there are
#       Co-prime - means numbers that do not have any shared factors with another

#   pick a number "e"
#   1 < e < phi(N)
#       then, given the list of numbers from, 1 < e < phi(N), find numbers coprime with N AND phi(N)

#   Now we have the lock (e, N)

#   pick "d" - decryption key
#   find d such that, (d*e)mod( phi(N) ) = 1
#       in other words find it such that a mutiple called "d," gives d*e(mod 6) = 1
#       i.e) if e = 5, the list of number could be 5,10,15,20,25,30
#           then d = 5 will give d*e(mod 6) = 1


def Fermat_LT(n, a):

    exp = n - 1

    while (not(exp & 1)): #if the exp is even, div by 2
        exp >>= 1
    

    #Now the exp is odd
    #pow(a, exp,n) == (a^exp) mod(n)... werid right?


    if( pow(a,exp,n) == 1 ): #LOOK ABOVE this is what we are trying to show (first of the expandsion)
        return 1 #Return true


    while ( exp < (n - 1) ): #Checks the rest of the expandsion
        if( pow(a,exp,n) == n-1):
            return 1 #Return true

        exp <<= 1 #to move right of the expandsion, mult exp by 2


    return 0


def Miller_R(n):
    k = 30
    for i in range(k):
        a = die.randrange(2,n-1)
        if not Fermat_LT(n,a):
            return False
    
    return True





def prime_gen(bits):
    while True:
        #Guarantee that a is odd
        a = (die.randrange(1 << bits - 2, 1 << bits - 1) << 1) + 1
        if(Miller_R(a)):
            return a
        
        #Funny thing here is that I found a mistake in the code
        #I was referencing
        #They did ...
        #a = (die.randrange(1 << bits - 1, 1 << bits) << 1) + 1
        #Which shift it to +1 more bit than you want




class RSA_key:
    #def __init__(self, p, q, N, e, d, bits = 10):
    def __init__(self, bits = 10):
        self.msg = 0
        self.bits = bits
        self.p = prime_gen(bits)
        self.q = prime_gen(bits)
        self.N = self.p*self.q
        self.e = 2
        self.ENC = []
        self.DCP = []

        self.msg_arr = [] #The thing we will encry and decryp from

        Noise = 2

        self.phi = (self.p-1)*(self.q-1)
    
        #Creates a number that is co-prime with N, phi
        while(self.e < self.phi):
            if((math.gcd(self.e,self.phi) == 1) and (math.gcd(self.e,self.N) == 1)):
                break
            self.e = self.e + 1
            continue

        #(e, N) are the lock
   
        END = 15
        
        while(True):
            try:
                d = mod_inverse(self.e, self.phi*Noise)
                break
            except(ValueError):
                RAND = die.randrange(2,END)
                END = END + 1
                continue
    
        self.d = int(d)
    
    def encryp(self, msg):
        self.msg = msg

        for c in msg: #Converts the msg to an arr
            char_to_num = ord(c)
            self.msg_arr.append(char_to_num)
        for n in range(len(self.msg_arr)): #Encrpts arr
            self.ENC.append(pow(self.msg_arr[n],self.e,self.N))
        return self.ENC


    def decryp(self, encryp_msg):
        for n in range(len(encryp_msg)):
            self.DCP.append(pow(encryp_msg[n],self.d,self.N))
        return self.DCP

    def debugg1(self):
        print(f'p = {self.p}')
        print(f'q = {self.q}')
        print(f'N = {self.N}')
        print(f'phi = {self.phi}')
        print(f'e = {self.e}')
        print(f'd = {self.d}')
        print(f'e*dmod(n) must = 1 ->')
        print(f'{(self.e*self.d)%self.phi}')
    
    def debugg2(self):
        print(f'MSG = {self.msg}')

        if(self.bits < 16):
            for n in range(len(self.ENC)):
                print(f'{self.ENC[n]} : {chr(self.ENC[n])}')
        else:
            for n in range(len(self.ENC)):
                print(f'{self.ENC[n]}')
        for n in range(len(self.DCP)):
            print(f'{self.DCP[n]} : {chr(self.DCP[n])}')



    def DEBUGG_msg_arr(msg):
        for n in range(len(msg_arr)):
            print(f'{msg_arr[n]} : {chr(msg_arr[n])}')




def main():
    
    INPUT_MSG = input("Input a msg to encrpyt!!!\n")

    A = RSA_key(10)
    E = A.encryp(INPUT_MSG)
    A.decryp(E)
    A.debugg1()
    A.debugg2()


def main1():
    A = RSA_key(1024)
    E = A.encryp("Hello")
    A.decryp(E)
    A.debugg1()
    A.debugg2()


def main2(): #testing encryping 1 val
    A = RSA_key(1024)
    E = A.encryp(2)
    A.decryp(E)
    A.debugg()

def main3(): #testing prime generation for 512,1024,2048 bits
    print(prime_gen(1024))

def main4(): #Testing Miller_R to my heart's content
    while(True):
        print(f'Input for Miller-R test')
        var = int(input())
        if(var == 0): 
            break
        print(Miller_R(var))
        continue


def main5(): #Testing Miller_R for one num
    print(Miller_R(97))


if (__name__ == '__main__'):
    main()
