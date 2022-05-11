# num=1
# while num<=100:
#     print(num)
#     num+=1
#     pass
#打印99乘法表
#倒三角乘法表
# row=9
# while row>=1:
#     col=1
#     while col<=row:
#         print('%d*%d=%d'%(col,row,row*col),end=' ')
#         col+=1
#         pass
#     print( )
#     row-=1
#     pass
#打印直角三角形
# row=1
# while row<=7:
#     j=1#控制每一行上的数量
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row+=1


#打印等腰三角形
row=1
while row<=10:
    j=1
    while j<=10-row:#控制打印空格个数
        print(' ',end=' ')
        j+=1
        pass
    i=1
    while i<=2*row-1:#控制打印*号
        print('*',end=' ')
        i+=1
        pass
    print()
    row+=1