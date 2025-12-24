
lower1 = 2
upper1 = 5
lower2 = 6
upper2 = 20

n = int(input().strip())

if n % 2!=0:
    print(f'Weird')
elif lower1 <= n <= upper1:
    print(f'Not Weird')
elif lower2 <= n <= upper2:
    print(f'Weird')
elif n > 20:
     print(f'Not Weird')



        