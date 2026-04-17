# Pico W MQTT Doorbell Sender

Raspberry Pi Pico W を使用して、  
押しボタンスイッチ入力を MQTT イベントとして送信する実機送信モジュールです。

本システムは、Pico W → MQTT → Node-RED → TV制御 の流れで構成されています。

---

## 概要

Pico W は入力装置として動作し、ボタン押下時に MQTT へイベント送信します。

```text
ボタン入力
↓
Pico W
↓
MQTT
↓
Node-RED
↓
TV制御 / 表示

送信イベントは以下です。

{"type":"doorbell"}
実機確認済み

以下の動作を確認済みです。

Pico W ボタン押下
Wi-Fi接続
MQTT送信
Node-RED受信
doorbell判定
TV制御
ファイル構成
picow/
├─ README.md
├─ main.py
├─ secrets_example.py
└─ nodered/
   ├─ README.md
   └─ genkan-event-receiver.json
使用方法
1. secrets.py を作成

secrets_example.py をコピーして secrets.py を作成してください。

WIFI_SSID = "YOUR_SSID"
WIFI_PASSWORD = "YOUR_PASSWORD"

BROKER = "192.168.0.140"
PORT = 1883
TOPIC = "genkan/event"
CLIENT_ID = "picow-doorbell"
2. Pico W に保存

以下の2ファイルを Pico W に保存します。

main.py
secrets.py
3. 配線
GPIO15 ---- ボタン ---- GND

内部プルアップを使用します。

4. 起動

Pico W を再起動すると自動実行されます。

シリアル出力例
Wi-Fi接続完了
MQTT接続完了
ボタン監視開始
doorbell送信
Node-RED 側

受信フローは nodered/genkan-event-receiver.json を参照してください。

受信 Topic:

genkan/event
テストボタンの利点

ボタンスイッチを取り付けることで、
実機センサーが無くても疑似信号テストが可能です。

押せば即確認できる
MQTT送信確認できる
Node-RED受信確認できる
トラブル切り分けに便利
注意事項
secrets.py は公開しない
Topic 名は送受信で一致させる
本番環境では既存Node-REDフローとの重複に注意
完成状態
Pico W
↓
MQTT
↓
Node-RED
↓
TV ON/OFF

本構成は実機動作確認済みです。


---

# 4. nodered/README.md（最新版）

```markdown
# Node-RED Flow for Pico W MQTT Doorbell

本ディレクトリは、Pico W から送信された MQTT イベントを受信し、  
TV制御や表示処理を行う Node-RED フローです。

---

## 実機確認済み

以下の流れを確認済みです。

```text
Pico W ボタン押下
↓
MQTT送信
↓
Node-RED受信
↓
doorbell 判定
↓
TV制御
ファイル
genkan-event-receiver.json
読み込み方法
Node-RED を開く
右上メニュー
読み込み（Import）
JSONファイル選択
Deploy
基本フロー
mqtt in
↓
json
↓
switch（doorbell判定）
↓
TV制御
Topic
genkan/event
受信データ
{"type":"doorbell"}
switch条件
msg.payload.type == doorbell
用途
インターホン押下通知
TV自動起動
HDMI切替
表示制御
注意事項

既存の同一 Topic フローがある場合、
二重動作防止のため既存フローを無効化してテストしてください。

推奨手順
既存フロー無効化
↓
テストフロー読込
↓
Deploy
↓
確認
↓
削除
↓
元へ戻す
完成状態

本フローは Pico W 実機との接続確認済みです。


---

# あなたが今やること

GitHubでこの2つを更新してください。

```text
README.md
nodered/README.md
# Pico W MQTT Doorbell Sender

本ディレクトリは、Raspberry Pi Pico W を使用して  
ボタンスイッチ入力を MQTT イベントとして送信するスクリプトを提供します。

本書「JB Net（爺婆Net）」に対応した実機送信モジュールです。

---

## ■ 概要

Pico W は、センサーやスイッチ入力を取得し、  
その情報を MQTT を通じて送信する役割を持ちます。

```text
ボタン入力
↓
Pico W
↓
MQTT
↓
Node-RED
↓
表示 / 制御
