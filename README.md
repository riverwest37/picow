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
