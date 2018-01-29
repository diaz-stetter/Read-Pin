import os
import requests
import json
import paho.mqtt.client as mqtt
import time

headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}
response = requests.post(os.environ['FARMWARE_URL'] + '/api/v1/bot/state',
              headers=headers)
bot_state = response.json()

position_x = response.json()['location_data']['position']['x']
pin_13_value = response.json()['pins']['13']['value']
value = {
  "pin_value": pin_13_value
}
# Encode it as JSON...
json_payload = json.dumps(value)
"""
headers = {
  'Authorization': 'bearer {}'.format(API_TOKEN),
  'content-type': "application/json"}
response = requests.post(FARMWARE_URL + '/api/v1/bot/state',
              headers=headers)
bot_state = response.json()

position_x = response.json()['location_data']['position']['x']
pin_13_value = response.json()['pins']['13']['value']
print(pin_13_value)"""
############
device_id = "device_1544"
def on_connect(client, userdata, flags, rc):
    print("Connected flags ",str(flags),"result code ",str(rc))
########################################
broker_address="brisk-bear.rmq.cloudamqp.com"
port = 1883
client = mqtt.Client()
# ...using credentials from `token_generation_example.py`
client.username_pw_set(device_id, API_TOKEN)
#broker_address="iot.eclipse.org"
def on_connect(client, userdata, flags, rc):
    print("CONNECTED! Sending data now...")
    # "bot/device_18/from_device" contains all of FarmBot's responses to
    # commands. It's JSON, like everything else. If FarmBot is running, we will
    # see a response from this channel.
    client.subscribe("bot/" + device_id + "/from_device")

    # Publish that payload as soon as we connect:
    client.publish("bot/" + device_id + "/from_clients", json_payload)


def on_message(client, userdata, msg):
    print("Got a message: ")
    print(msg.topic + " " + str(msg.payload))


# Attach event handler:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect("brisk-bear.rmq.cloudamqp.com", 1883, 60)
print("Here we go...")
client.loop_forever()
