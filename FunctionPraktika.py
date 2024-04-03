#1
# def a1(a=int(input("Kvadratning tomonini kirit "))):
#     P=a*4
#     return(f"{P}cm")
# print(a1())

#2
# def a2(a=int(input("Kvadratning tomonini kirit "))):
#     S=a**2
#     return(f"{S} cm")
# print(a2())


#3
# def a3(a=int(input("Kvadratning a tominini kirit ")), b=int(input("Kvadratning b tomonini kirit "))):
#     S=a*b
#     P=2*(a+b)
#     Y=f"yuzasi {S}, peremetri {P}"
#     return( Y)
# print(a3())


#4
# def a4(d=int(input("aylananing diametrini kirit "))):
#     p=3.14
#     L=p*d
#     return(L)
# print(a4())


#5
# def a5(a=int(input("Kubning yon tomonini kirit "))):
#     V=a**3
#     s=6*a**2
#     Y=f" hajmi {V} to'la sirti {s}"
#     return(Y)
# print(a5())


#6
# def a6(a=6,b=7,c=5):
#     V=a*b*c
#     S=2*(a*b+b*c+a*c)
#     c=f"hajmi {V}, to'la sirti {S}"
#     return(c)
# print(a6())


#7
# def a7(r=int(input("Doiraning radiusini kirit "))):
#     p=3.14
#     L=2*p*r
#     S=p*r**2
#     Y=f"uznligi {L} yuazi {S}"
#     return(Y)
# print(a7())


#8
# def a8(a=5,b=5):
#     f=(a+b)/2
#     print(f)
# a8()


# def a10(a=-5,b=-7):
#     y=a+b
#     k=a*b
#     kv=a**2
#     kv2=b**2
#     print(y,k,kv,kv2)
# a10()


# def a11(a=-5,b=-7):
#     y=a+b
#     k=a*b
#     m=abs(a)
#     m2=abs(b)
#     print(y,k,m,m2)
# a11()



# def a13(R1=5,R2=3):
#     p=3.14
#     S1=p*R1
#     S2=p*R2
#     S3=p*(R1-R2)
#     print(S1,S2,S3)
# a13()



# def a14(L=int(input("Aylananing uzunligini kirit "))):
#     p=3.14
#     R=2*p*L
#     S=p*R**2
#     y=f"radiusi {R} yuzasi {S}"
#     return(y)
# print(a14())


# def a15(s=56):
#     p=3.14
#     R=2*p*s
#     S=p*R**2
#     y=f"diametri {R} yuzasi {S}"
#     return (y)
# print(a15())



#Shart operatorlari 

# def b1(a=int(input("butun son kirit "))):
#     if a>0:
#         a+=1
#         print(a)
#     else:
#         print(a)
# b1()



# def b2(a=float(input("butun son kirit "))):
#     if a>0:
#         a+=1
#         print(a)
#     else:
#         a-=2
#         print(a)
# b2()



# def b3(a=float(input("Butun son kirit "))):
#     if a>0:
#         a+=1
#         print(a)
#     elif a<0:
#         a-=2
#         print(a)
#     else:
#         a+=10
#         print(a)
# b3()


# def b4(a=int(input("a son kirit ")), b=int(input("b son kirit ")), c=int(input("c son kirit "))):
#     if a>0 and b>0 and c>0:
#         print("a,b,c sonlari musbat")
#     elif a>0 and b<0 and c>0:
#         print("a va c soni musbat")
#     elif a>0 and b<0 and c<0:
#         print("a va b sonlari musbat")
#     elif a<0 and b>0 and c>0:
#         print("b va c sonlari musbat")

# b4()


# def b5(a=int(input("a son kirit ")), b=int(input("b son kirit ")), c=int(input("c son kirit "))):
#     if a>0 and b>0 and c>0:
#         print("a,b,c sonlari musbat")
#     elif a>0 and b<0 and c>0:
#         print("a va c soni musbat b soni manfiy")
#     elif a>0 and b<0 and c<0:
#         print("a va b sonlari musbat c soni manfiy")
#     elif a<0 and b>0 and c>0:
#         print("b va c sonlari musbat a soni manfiy")

# b5()



# def b6(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit "))):
#     if a>b:
#         print("a soni katta")
#     else:
#         print("B soni katta")
# b6()


# def b7(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit "))):
#     if a>b:
#         print(f" a soni 2-tartibda")
#     elif a<b:
#         print(f"a soni 1-tartibda")
#     else:
#         print(f"b soni 1-tartibda")
    
# b7()


# def b8(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit "))):
#     if a>b:
#         print(a)
#         print(b)
#     else:
#         print(b)
#         print(a)
# b8()



# def b10(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit "))):
#     if a<b or b<a:
#         y=a+b
#         print(y)
#     elif a==b:
#         s=a-b
#         print(s)
# b10()


# def b11(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit "))):
#     if a>b:
#         print(a)
#     elif a>b:
#         print(b)
#     elif a==b:
#         y=a-b
#         print(y)
# b11()



# def b12(a=int(input("a sonini kirit ")), b=int(input("b sonini kirit ")), c=int(input("c sonini kirit "))):
#     if a<b and a<c:
#         print("a soni kichkina")
#     elif a>b and b<c:
#         print("b soni kichkina")
#     elif c<a and c<b:
#         print("c soni kichkina")
#     else:
#         print("Sonlar teng bulmasin !!")
# b12()



# def b13(a=int(input('1-sonni kirit ')), b=int(input("2-sonni kirit ")), c=int(input("3-sonni kirit "))):
#     if a<b and a>c or a>b and a<c:
#         print("1-son  o'rtacha")
#     elif b<a and b>c or b>a and b<c:
#         print("2-son o'rtacha")
#     elif c>a and c<b or c<a and c>b:
#         print("3-son o'rtacha")
#     else:
#         print("404")
# b13()


#for sikl

# def c1(k = 3, n = 10):
#     for i in range(1,n+1):
#         print(k)
# c1()


# def c2(a=6,b=10):
#     for i in range(a,b+1):
#         print(i, b-a)

# c2()


# def c3(a=3,b=11):
#     for i in range(b-1, a, -1):
#         print(i, b-a-1)
# c3()


# def c4( konfet = 20000):
#     for i in range(1,11):
#         konfet_narxi = i * konfet
#         print(f"{i+1}kg konfet narxi {konfet_narxi}")
# c4()


# def c7(a=3,b=9):
#     o=0
#     for i in range(a,b):
#         o+=i
#         print(o)
# c7()



# def c8(a=3,b=13):
#     o=1
#     for i in range(a,b):
#         o*=i
#         print(o)
# c8()


# def c9(a=2,b=11):
#     for i in range(a,b):
#         i**=2
#         print(i)
# c9()

# def c10(n=10):
#     for i in range(1,n+1):
#         S=1+i/n
#         print(S)
# c10()

# def c11(n=10):
#     for i in range(1,n+1):
#         S=n**2+(n+i)**2+(2*n)**2
#         print(S)
# c11()

# def c12(n=10):
#     for i in range(1,n+1):
#         S=i*n
#         print(S)
# c12()



"Rekursiyaga kirish"

# ism = 'dilshod'
# def name():
#     ism = "otash"
#     print(ism)

# print(ism)
# name()

# def full():
#     print("Hello")
#     def name():



# def china():
#     print("Hello")
#     def byd():
#         print("BYD powerbanks")
#     byd()
# china()



# def add():
#     a=4
#     b=5
#     print(a+b)

# def a():
#     add()
#     print("A klass haqida ma'lumot")

# def b():
#     add()
#     print("B klass haqida malu'mot")

# a()
# b()



"rekursiya"


# def chiled(n):
#     if n==1:
#         return 1
#     else:
#         return n*chiled(n-1)
# print(chiled(10))