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

