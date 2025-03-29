A,B,C = list(map(float,input().split()))

if (A < B):
    temp = A
    B = A
    B = temp
if (B < C):
    temp = B
    B = C
    C = temp
if (A < C):
    temp = C
    A = C
    C = temp
if (A >= (A + B)):
    print ("NAO FORMA TRIANGULO")
if (A*A == (B*B + C*C)):
    print ("TRIANGULO RETANGULO")
if (A*A > (B*B + C*C)):
    print ("TRIANGULO OBTUSANGULO")
if (A*A < (B*B + C*C)):
    print ("TRIANGULO ACUTANGULO")
if (A == B == C):
    print ("TRIANGULO EQUILATERO")
if (A == B or B == C or C == A):
    print ("TRIANGULO ISOSCELES")





















