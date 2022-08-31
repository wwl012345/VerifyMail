# VerifyMail
**检测各种类型的邮箱是否存在**

### 一、项目说明
使用该脚本可以批量对生成的邮箱进行校验，查看该邮箱是否存在。这样当我们在做钓鱼邮件时可以快速定位目标用户，避免对不存在的邮箱发送钓鱼邮件，消耗服务器资源。

### 二、利用方法
`python3 VerifyMail.py target.txt`

<img width="1758" alt="image" src="https://user-images.githubusercontent.com/53456907/187672140-b5a0f303-5888-4f28-af1a-1f215b3a3ee1.png">

### 三、结果展示
会在当前目录下生成一个exist.txt文件，这个文件中会存放存在的邮箱，如下图所示:

<img width="592" alt="image" src="https://user-images.githubusercontent.com/53456907/187673002-9afa78f7-f664-4259-823d-5be192af3adc.png">

同时也会在命令行中以字典的形式展示所有邮件是否存在。如下所示:

<img width="1754" alt="image" src="https://user-images.githubusercontent.com/53456907/187672869-bd555241-77ec-43ca-ba2f-a923c312c972.png">
