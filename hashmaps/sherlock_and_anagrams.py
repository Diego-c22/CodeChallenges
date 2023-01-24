#!/bin/python3
import time

def sherlockAndAnagrams(s):
    # Write your code here
    patterns = {}
    total_repeated_patterns = 0
    for l in range(0, len(s)):
        for i in range(l, -1, -1):
            patterns[s[i:l]] = 1

    for l in range(0, len(s)):
        for i in range(l, -1, -1):
          if s[i:l][::-1] in patterns:
            total_repeated_patterns += 1
            print(s[i:l][::-1])

    return total_repeated_patterns
        

if __name__ == '__main__':
    start_time = time.time()
    result = sherlockAndAnagrams('abcd')
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
