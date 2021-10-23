a=float(input())
b=float(input())
c=input('+,-,*,/')
if c!='+,-,*,/':
    print('error')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    if b==0:
        print('error')
    print(a/b)
elif c!='+'or c!='-'or c!='*'or c!='/':
    print ('error operation')



