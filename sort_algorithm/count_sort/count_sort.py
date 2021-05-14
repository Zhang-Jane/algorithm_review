def count_sort(li, max=100):
    count_li = [0 for _ in range(max+1)]
    for val in li:
        count_li[val] += 1
    print(count_li)
    li.clear()
    for i, v in enumerate(count_li):
        for _ in range(v):
            li.append(i)

li = [2,3,4,5,1,10]
count_sort(li)
print(li)