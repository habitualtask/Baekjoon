list_n=0

for i in range(1,10):
    n=int(input())
    if list_n<n:
        list_n=n
        list_l=i
print(list_n)
print(list_l)