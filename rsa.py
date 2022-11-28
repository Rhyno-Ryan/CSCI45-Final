from math import *
from random import *

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


def Miller_R:




def prime_gen():






def main():
    print(f'THE START OF A NEW PROJECT \n')











if (__name__ == '__main__'):
    main()
