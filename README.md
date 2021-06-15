# store-remo-to-dynamodb

## 設定項目

事前に設定しておくべき項目を以下に示す。

## AWS Lambda

AWS Lambda に以下の値を設定しておくこと。

### 一般設定

![general](README.assets/general.png)

- タイムアウト:30 秒

### 環境変数

![env](README.assets/env.png)

- REMO_SECRET_NAME
  - 意味：nature remo cloud API の API KEY などを格納したシークレットの名前
  - 例：`secrets/remo`
- LOG_LEVEL
  - 意味：ログレベル `CRITICAL, ERROR, WARNING, INFO, DEBUG` から選択
  - 例：`DEBUG`

### Secrets

### Remo

- access_token
  - 意味：nature remo cloud API のアクセストークン
  - 例：`21afjlij4224`
- remo_device_id
  - 意味：Remo デバイス ID
  - 例：`hoge`
- aircon_appliance_id
  - 意味：エアコンの ID
  - 例：`hoge.hatenablog.com`

## 使い方

### ソースコードのアップロード

まず、aws-cli を事前に設定しておくこと。

```bash
aws configure
```

次に、アップロードスクリプトを実行すること。

```bash
./upload.sh
```
