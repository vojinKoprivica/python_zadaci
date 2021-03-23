# Napisati program koji učitava dva cela broja n i m (n <= m) i ispisuje sve cele brojeve iz intervala [n, m].

n = int(input("Prvi broj je: "))
m = int(input("Drugi broj je: "))

if n <= m :
# # for petlja:
#     for a in range(n,m+1):
#         print(a)


#while petlja:

    while n<m+1:
        print(n)
        n+=1

else:
    print("Neispravan unos, prvi broj mora biti manji od drugog")

