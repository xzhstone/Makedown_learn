### 变量
- - -
* 定义：用来储存数据的盒子
* 变量的使用：
 ```python
    a = 10      #定义规则 变量名 = 数据
                #a就是变量的名字，里面的数据就是10
    print(a)    #使用变量 必须先定义变量才能使用变量
                #变量是可以多次赋值的（程序执行过程中可以改变）
    b = '小王'
    print(b)    #变量可以不是数字，不需要指定数据类型
 ```
* Python基本数据类型
> 数字（num）
>> int(有符号整数)
>> long(长整型) ：python3取消 
>> float(浮点型)
>> complex(复数)
>> bool(布尔值)
>>> true
>>> false

> 字符串(str)

> 字典(dict)

> 元组(tuple)

> 列表(list)

* 数据类型的赋值（type函数可以快速查看数据类型）
```python
    a = 10
    b = '小王'
    c = 12.67
    d = True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
```
  
输出结果
```python
    <class'int'>#有符号整数
    <class'str'>#字符串
    <class'float'>#浮点型
    <class'bool'>#布尔型
```
* 高级数据类型
  ```python
    #高级数据类型
    a = ()#元组类型
    print(type(a))

    b = []#列表类型
    print(type(b))

    c = {}#字典类型
    print(type(c))
  ```
* 输出结果
  ```python
  <class'tuple'>
  <class'list'>
  <class'dict'>
  ```
* 变量命名规则
> * 变量必须以字母（a-z,A-Z）或下划线（_）开头
> * 其他字符可以是字母数字或_
> * 变量区分大小写
> * Python关键字不能用作变量名,比如type、class之类的。
> ```python
>       #22Name = '徐志豪'(这样会报错)
>       #必须不能以数字开头
>       Name = '徐志豪'
>       _age = 50
>       name = 'stone'
>       #True = 12.3(True是关键字，这样做会报错)
>       print(Name,_age,name)
> ```
> * 输出结果
> ```python
>       徐志豪
>       50
>       stone
> ```

* 命名规范
> * 见名知意：尽量使用有语义的单词命名。如使用password用作密码，username用户名。
> * 小驼峰式命名法：第一个单词首字母大小写，如userName
> * 大驼峰式命名法：全部单词首字母都用大写，如UserName
> * 下划线命名法：每个单词用_下划线链接，如user_name
> * 虽然可以用中文命名，但是最好不用使用中文，否则迟早会后悔