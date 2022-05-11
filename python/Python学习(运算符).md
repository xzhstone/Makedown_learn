### 运算符
- - -
#### 算术运算符
定义两个变量：a = 7,b = 3
|算术运算符|作用描述|实例|
|:---:|:---:|:---:|
|+加法|加法运算|a+b=10|
|-减法|算术加法|a-b=4|
|*乘法|算数减法|a*b=21|
|**指数|左边的数是底数，右边的数是指数|a**b=343|
|%取余|x%y x除以y的余数|a%b=1|
|/除法|x/y 结果包含小数点后面的书|a/b=2.33333|
|//地板除|x/y 结果是忽略小数点后面的数，只保留整数位|a//b=2|

* 代码示例
  ```python
    a = 7
    b = 3     #定义ab变量
    print(a+b)
    print(a-b)
    print(a*b)
    print(a**b)
    print(a%b)
    print(a/b)
    print(a//b)
  ```
* 输出结果
  ```python
    10
    4
    21
    2.333333333
    1
    2
  ```
- - -
#### 比较运算符
|比较运算符|名称|实例|结果描述|
|:---:|:---:|:---:|:---:|
|==|等于|x==y|如果x恰好等于y，则为真|
|!=|不等于|x!=y|如果x恰好不等于y，则为真|
|>|大于|x>y|如果x大于y，则为真|
|<|小于|x<y|如果x小于y，则为真|
|>=|大于或等于|x>=y|如果x大于或等于y，则为真|
|<=|小于或等于|x<=y|如果x小于或等于y，则为真|

* 代码示例
  ```python
    a,d = 2,3
    print(a==b)
    print(a!=b)
    print(a>=b)
    print(a<=b>)
    print(a>b)
    print(a<b)#结果为bool类型的数据，只有True或False
  ```
* 输出结果
  ```python
    False
    True
    True
    False
    True
    False
  ```
- - -
#### 逻辑运算符
|逻辑运算符|示例|结果描述|
|:---:|:---:|:---:|
|and|x and y|x,y同为真，则结果为真，如果一个为假，则结果为假|
|or|x or y|x,y有一个为真，则结果为真，全部为假，则结果为假|
|not|x not y|取反，如果x为真，则结果为假，如果x为假，则结果为真|
* 代码示例
  ```python
    #逻辑运算符and or not
    #and  条件比较严格、
    #定义四个变量
    a,b,c,d = 23,18,10,3
    print(a+b>c and c<d) 
    print(c>d and a>b)#and两边必须都满足True否则为False
    #or 条件没有那么严格
    print(a<b or b>d)
    print(a<b or b<d)#or两边都不满足为False
    #not 取反的意思，真假切换，没有对与错
    print(not a>b)#a>b成立，加入not后结果为False
    
  ```

* 输出结果
  ```python
    False
    True
    True
    False
    False
  ```
* 逻辑运算优先级
> () > not > and > or
 * 代码示例
  ```python
    print(2>1 and 1<4 or 2<3 and 9<6 or 2<4 and 3<2)
    #相当于true or true or false
  ```
* 结果展示
  ```python
    True
  ```
- - -
#### 赋值运算符
|赋值运算符|作用描述|结果描述|
|:---:|:---:|:---:|
|=|赋值运算符|将等号右边的值赋给左边|
|+=|加法赋值运算符|c+=a等效于c=c+a|
|-=|减法赋值运算符|c-=a等效于c=c-a|
|*=|乘法赋值运算符|c*=a等效于c=c*a|
|/=|除法赋值运算符|c/=a等效于c=c/a|
|%=|取模赋值运算符|c%=a等效于c=c%a|
|**=|幂赋值运算符|c**=a等效于c=c**a|
|//=|取整赋值运算符|c//=a等效于c=c//a|
* 代码示例
  ```python
    #赋值运算 实际是算术运算的补充
    a,c = 2,3
    a+=c
    print(a)
    a-=c
    print(a)
    a*=c
    print(a)
    a/=c
    print(a)
    a%=c
    print(a)
    a**=c
    print(a)
    a//=c
    print(a)
  ```
* 结果展示
  ```python
    5
    2
    6
    2.0
    2.0
    8.0
    2.0
  ```
  

