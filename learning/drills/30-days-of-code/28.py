
import sys

def solve():
    N = int(input().strip())
    names_to_print = []

    for _ in range(N):
        first_name, email_id = input().strip().split()
        
        if email_id.endswith("@gmail.com"):
            names_to_print.append(first_name)

    names_to_print.sort()

    for name in names_to_print:
        print(name)

if __name__ == '__main__':
    solve()
