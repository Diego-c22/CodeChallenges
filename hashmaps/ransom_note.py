#!/bin/python3
import time

def checkMagazine(magazine, note):
    # Write your code here
    words = {}
    for word in magazine:
        words[word] = words[word] + 1 if word in words else 1
    
    for word in note:
        if word not in words or words[word] < 1:
            print('No')
            return
        words[word] -= 1
    print('Yes')
        

if __name__ == '__main__':
    start_time = time.time()
    checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four'])
    print("--- %s seconds ---" % (time.time() - start_time))
