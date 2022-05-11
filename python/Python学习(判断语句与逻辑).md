#### 流程与控制
- - -
* 流程定义：计算机执行代码的顺序
* 流程控制定义：对计算机代码执行的顺序进行有效的管理只有流程控制才能实现在开发中的业务逻辑
* **流程控制的分类**
  > 1. 顺序流程：代码一种自上而下的执行结构，也是python默认的流程
  > 2. 选择流程：根据在某一步的判断有选择地执行相应的逻辑的一种结构
  >> 2.1 单分支：
  >> ```python
  >> if 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> ```
  >> 2.2 双分支
  >> ```python
  >> if 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> else:
  >>    一条条的python代码
  >>    ......
  >>```
  >> 2.3 多分支
  >> ```python
  >> if 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> elseif 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> elseif 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> elseif 条件表达式:
  >>    一条条的python代码
  >>    ......
  >> else:
  >>    一条条的python代码
  >>    ......
  >> ```
  >> 条件表达式：可以是比较运算符/逻辑运算符/复合运算符
  > 3. 循环流程：在满足一定的条件下一直重复的执行某段代码的逻辑【事情】
  > ```python
  > while 条件表达式
  >     一条条python代码
  >     ......
  > for ... in ....#...处为一个变量、....处为一个可迭代的集合对象
  >     一条条python代码
  >     ......
  > ```




- - -
### if-else语句
```python
#单分支的用法
# score=int(input('请输入你的成绩:'))
# if score<=60 and score>=0:
#     print('成绩不是太理想，要继续加油哦')
#     pass#空语句
# elif score>60 and score<=80:
#     print('你的成绩合格了！！！')
#     pass
# elif score>80 and score<=100:
#     print('你学的太好了')
#     pass
# else:
#     print('乱输入成绩是吧')
#     pass
# print('语句运行结束')


#猜拳游戏
#0石头1剪刀2布
from ast import Return
import random
num=0
num_computer=0
num_people=0
while num<5 or num_computer==num_people:
    computer=random.randint(0,2)
    people=int(input('请出拳[0:石头 1:剪刀 2:布]:'))
    if computer==people:
        print('你们这局是平局')
        num+=1
        pass
    elif computer==0 and people==1 or computer==1 and people==2 or computer==2 and people==0:
        print('这局是计算机赢了')
        num_computer+=1
        num+=1
        pass
    else:
        print('恭喜你赢了计算机') 
        num_people+=1
        num+=1
        pass
if num_computer<num_people:
    print('你获得了最终胜利局,一共进行了%s局，你赢了%s局，平局了%s局'%(num,num_people,num-5))
    pass
else:
    print('你连计算机都比不过,一共进行了%s局，计算机赢了%s局，平局了%s局'%(num,num_computer,num-5))
    pass


```
- - -
#### while
* 语法特点：
* 1. 有初始值
* 2. 有条件表达式
* 3. 变量【循环体内计数变量】的自增自减，否则会造成死循环
* 使用条件：循环的次数不确定，是依靠循环条件来结束
* 目的：为了将相似或者相同的代码操作变得更加简洁，使代码可以重复利用 
```python
num=1
while num<=100:
    print(num)
    num+=1
    pass
```
* 上方if代码中包含了while语句
```python
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
```
- - -
#### for
