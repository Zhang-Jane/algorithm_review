def radix_sort(li, bucket_num=10):
    max_num = max(li)
    i = 0
    while 10**i < max_num:
        buckets = [[] for _ in range(bucket_num+1)]
        for val in li:
            digit = val // (10**i) % 10
            buckets[digit].append(val)
        li.clear()
        for bucket in buckets:
            for val in bucket:
                li.append(val)
        i += 1

nums = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
radix_sort(nums)
print(nums)