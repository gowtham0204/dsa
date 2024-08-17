


def floorSqrt(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans

n = 82
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)

