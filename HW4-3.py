def count_ways(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    
    for i in range(3, n + 1):
        ways[i] = ways[i-1] + ways[i-2]
    
    return ways[n]


n = int(input())
print(count_ways(n))
