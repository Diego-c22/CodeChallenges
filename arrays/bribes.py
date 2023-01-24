def swap(q, index1, index2):
    temp = q[index1]
    q[index1] = q[index2]
    q[index2] = temp
    return q

def minimumBribes(q):
    # Write your code here
    total_bribes = 0
    for i in range(len(q) -1, -1, -1):
        print(q)
        if q[i] == i + 1: continue
        if i - 1 >= 0 and q[i - 1] == i + 1:
          total_bribes += 1
          q = swap(q, i, i - 1)
          continue
        if i - 2 >= 0 and q[i - 2] == i + 1:
          total_bribes += 2
          q = swap(q, i - 1, i - 2)
          q = swap(q, i, i - 1)
          continue
        
        print('Too chaotic')
        return
            
    print(total_bribes)


def minimumBribes2(q):
    # Write your code here

    total_bribes = 0
    for i in range(len(q) -1, -1, -1):
        if q[i] == i + 1: continue
        if i - 1 >= 0 and q[i - 1] == i + 1:
          total_bribes += 1
          continue
        if i - 2 >= 0 and q[i - 2] == i + 1:
          total_bribes += 2
          continue
        
        print('Too chaotic')
        return
            
    print(total_bribes)

if __name__ == '__main__':
        minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
