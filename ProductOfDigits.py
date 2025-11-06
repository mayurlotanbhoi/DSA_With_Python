n = 81000
ans = ''

for div in range(9, 1, -1):
    while(n % div == 0):
        n //= div
        ans = str(div) + ans

print(ans)








    