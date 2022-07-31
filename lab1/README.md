
小组成员
--------
房柯彤 202000460013 functom0v0


完成项目
--------
1 implement the naïve birthday attack of reduced SM3  
2 implement the Rho method of reduced SM3  
4 do your best to optimize SM3 implementation (software)  

未完成项目
---------
3、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20


1 implement the naïve birthday attack of reduced SM3
----------------------------------------------------

实现SM3的生日攻击   
结果如下:  
![运行结果](https://github.com/functom0v0/IEP/blob/main/lab1/1.png)

2 implement the Rho method of reduced SM3  
-------------------------------------------
实现SM3的Rho攻击:  
SM3_Rho:  
strtint_l:  将大小为64的十六进制字符串列表更新为十进制整型列表  

结果如下  
![运行结果](https://github.com/functom0v0/IEP/blob/main/lab1/3.png)

4 实现并优化SM3算法
------------------
CSL1:实现循环移位  
pad:进行原文填充并按512bit进行信息分组  
cpr:压缩函数  
ext:消息扩展  
SM3：算法主体部分，进行填充后对每个分组分别进行扩展与压缩并迭代更新IV。  
十六进制信息 abc 加密结果如下:    
![运行结果](https://github.com/functom0v0/IEP/blob/main/lab1/2.png)
