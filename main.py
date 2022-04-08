"""
Given a string representing a number in binary convert it into a decimal number.
Input-> 10000
Output-> 16
"""

def bin_to_dec(bin):
  dec = 0
  i = 0
  while(bin != 0):
    d = bin % 10
    dec = dec + d * pow(2,i)
    bin = bin // 10
    i += 1
  print(dec)

bin_to_dec(10000)
