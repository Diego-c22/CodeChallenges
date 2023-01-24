#!/bin/python3

import functools
import time

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    list_results = [0 for i in range(n)]
    for query in queries:
        for i in range(query[0] - 1, query[1]):
            list_results[i] += query[2]

    return functools.reduce(lambda x, y: x if x > y else y, list_results)


def arrayManipulation2(n, queries):
    list_results=[0]*(n+1)
    for query in queries :
        a, b, k = query
        list_results[a-1]=list_results[a-1]+k
        list_results[b] = list_results[b] - k

    for i in range(1,n):
        list_results[i]+=list_results[i-1]
    return max(list_results)


def arrayManipulation3(n, queries):
    # Write your code here
    list_results=[0]*(n+1)
    for query in queries :
        a, b, k = query
        list_results[a-1]=list_results[a-1]+k
        list_results[b] = list_results[b] - k

    for i in range(1,n):
        list_results[i]+=list_results[i-1]
    return max(list_results)


if __name__ == '__main__':
    start_time = time.time()
    f = open("/Users/diegocortes/Documents/projects/CodeChallenges/data2.txt", "r")
    queries = [x.replace('\n', '').split(' ') for x in f]
    queries = [[int(i) for i in q] for q in queries]

    # queries = [
    #   [1, 7, 100],
    #   [4, 8, 500],
    #   [19, 20, 1000],
    #   [5, 5, 5000],
    #   [20, 20, 10000]
    # ]

    result = arrayManipulation3(10000000, queries)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
