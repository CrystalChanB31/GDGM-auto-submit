# 今日校园自动填表广东工贸职业技术学院版
广东工贸今日校园自动填表 项目 <br>
本项目主要函数并非我原创，原作者地址为https://github.com/ZimoLoveShuang<br>
我将其进行优化，使得该项目可以专门面向广东工贸职业技术学院的同学使用<br>
目前，该函数API调用的服务器均为我个人的服务器。 <br>
本项目开源，根据作者要求：禁止他人进行付费代挂服务。<br>
更多消息请前往原作者的项目地址下进行查看https://github.com/ZimoLoveShuang/auto-submit <br>
欢迎有能力的同学一起参与 <br>
#2021年2月4日更新：<br>
增加了经纬度定位信息，修复了定位失败的BUG
<strong>执行原理：</strong><br>
1.通过将这些文件放在腾讯云函数上，每天23:30自动执行。<br>
2.通过index.py文件读取conifg.yml文件，获取到用户的数字工贸账号和密码后，模拟登录<br>
3.模拟登录完成后，读取用户待填写的表单，读取表单，与config.yml配置文件表单进行比对<br>
4.比对无误，则将配置文件的固定选项传送到数字工贸的表单内<br>
5.完成提交，并向维护者发送基于server酱的消息推送<br>
6.本项目的接口API使用了自己的服务器，减轻原作者服务器的负担。
