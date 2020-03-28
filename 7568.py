num = int(input())
people = list()
for row in range(num) :
    x, y = map(int, input().split())
    #x = int(input())
    #y = int(input())
    people.append((x, y))
    #print(people)

    for i in people :
rank = 1
for j in people :
if (i[0] != j[0])&(i[1] != j[1]) :
    if (i[0] < j[0]) &(i[1] < j[1]) :
        rank += 1
        print(rank)