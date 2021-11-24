# pixiv-save
save pixiv user illusts

## install 

`pip install pixiv-save`

## usage

`pixivsave.py {args}`

```shell
usage: pixivsave.py [-h] [-u USERID] [-t TOKEN] [-p PROXY] [-d DOWNLOADTO] [-s] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -u USERID, --userid USERID
                        pixiv userid which you want to download pictures from.
  -t TOKEN, --token TOKEN
                        your pixiv refresh token.
  -p PROXY, --proxy PROXY
                        proxy like 127.0.0.1:7890.
  -d DOWNLOADTO, --downloadto DOWNLOADTO
                        download path.
  -s, --separate        if make directory for every illusts.
  -c, --config          load config.json file
```

## 效果
![](https://cdn.jsdelivr.net/gh/hibian/MyStaticResources@main/1637781102239-Snipaste_2021-11-25_03-11-12.png)