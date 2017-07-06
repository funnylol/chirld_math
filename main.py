# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:48:28 2017

@author: funnylol
"""

import random

def create_math(count,start1,stop1,start2,stop2,math):
    if isinstance(count and start1 and stop1 and start2 and stop2,int):
        if math=='+':
            for x in range(count):
                i = random.randint(start1,stop1)
                h = random.randint(start2,stop2)
                print(str(i) + ' ' + math + ' ' + str(h) + ' =____')
        if math=='-':
            for x in range(count):
                i = random.randint(start1,stop1)
                h = random.randint(start2,stop2)
                print(str(i) + ' ' + math + ' ' + str(h) + ' =____')
        if math=='×':
            for x in range(count):
                i = random.randint(start1,stop1)
                h = random.randint(start2,stop2)
                print(str(i) + ' ' + math + ' ' + str(h) + ' =____')
        if math=='÷':
            while True:
                if count < 0:
                    break
                else:
                    i = random.randint(start1,stop1)
                    h = random.randint(start2,stop2)
                    if i > h and i != 0:
                        r = i % h
                        if r == 0:
                            count -= 1
                            print(str(i) + ' ' + math + ' ' + str(h) + ' =____')
                

if __name__ == '__main__':
    create_math(100,10,99,2,10,'÷')
