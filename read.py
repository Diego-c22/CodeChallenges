f = open("./data.txt", "r")
x =[x.replace('\n', '').split(' ') for x in f]

f = open("/Users/diegocortes/Documents/projects/CodeChallenges/data.txt", "r")
    queries = [x.replace('\n', '').split(' ') for x in f]
    queries = [[int(i) for i in q] for q in queries]