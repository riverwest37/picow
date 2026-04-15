import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

# secrets.py から読み込む
import secrets

# 設定読み込み
WIFI_SSID = secrets.WIFI_SSID
WIFI_PASSWORD = secrets.WIFI_PASSWORD

BROKER = secrets.BROKER
PORT = secrets.PORT
TOPIC = secrets.TOPIC
CLIENT_ID = secrets.CLIENT_ID

BUTTON_PIN = 15
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    print("Wi-Fi接続中...")
    while not wlan.isconnected():
        time.sleep(1)

    print("Wi-Fi接続完了:", wlan.ifconfig())

def connect_mqtt():
    client = MQTTClient(CLIENT_ID, BROKER, port=PORT)
    client.connect()
    print("MQTT接続完了")
    return client

def main():
    connect_wifi()
    client = connect_mqtt()

    last_state = 1

    while True:
        current_state = button.value()

        if last_state == 1 and current_state == 0:
            payload = '{"type":"doorbell"}'
            client.publish(TOPIC, payload)
            print("doorbell送信")
            time.sleep(0.5)

        last_state = current_state
        time.sleep(0.05)

main()