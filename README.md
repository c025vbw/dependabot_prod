# Docker イメージをビルド

```
docker build -t numpy-test .
```

# Docker コンテナをバックグラウンドで実行し、カレントディレクトリをマウント

```
docker run -d --name numpy-container -v $(pwd):/app numpy-test tail -f /dev/null
```

# コンテナを再起動

```
docker start numpy-container
```

# 実行中のコンテナに接続

```
docker exec -it numpy-container /bin/bash
```

# docker を停止する

```
docker stop numpy-container
```

# コンテナ内で Python スクリプトを実行

```
python script.py
```

# テスト

```
 pytest test_script.py
```
