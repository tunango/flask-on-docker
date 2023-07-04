# flask-on-docker

 flaskを動かすコンテナです
 appをマウントしています

## コマンド

### ローカルにDL
$ git clone https://github.com/tunango/flask-on-docker.git

### 移動
$ cd flask-on-docker 

### コンテナを起動して入る
$ docker run --rm -it -v "$(pwd)"/app:/app tuto-on-d /bin/bash


### コンテナを起動してLocalhost:5000に表示 (debugmode)
$ docker run --rm -p 5000:5000 -v "$(pwd)"/app:/app tuto-on-d


※--rm はコンテナを終了したとき削除する⇒毎度起動が必要

