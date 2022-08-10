''' Условие: найти все простые числа от 2 до n.
В решении использовался алгоритм "Решето Эратосфена" '''

n=int(input())
prime = [2,3,5,7,11]
if n>11:
    d=sorted(prime+[i for i in range(1,n,2) if i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0])[1:]
    print(*d)
else:
    prime.append(n)
    prime.sort()
    print(*prime[:prime.index(n)])
