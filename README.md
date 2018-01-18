# djwechat
django实现微信公众号开发


```
git clone https://github.com/stornado/djwechat.git
cd djwechat/djwechat
./managy.py makemigrations
./managy.py migrate
./managy.py collectstatic
./managy.py runserver --insecure # 带上--insecure解决static目录404问题
···
