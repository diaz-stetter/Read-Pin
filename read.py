import os
import requests
import json

headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}
response = requests.post(os.environ['FARMWARE_URL'] + '/api/v1/bot/state',
              headers=headers)
bot_state = response.json()

position_x = response.json()['location_data']['position']['x']
pin_13_value = response.json()['pins']['13']['value']

send_message = {
  "kind": "send_message",
  "args": {
    "message": "Value of pin 13 is: " + str(pin_13_value),
    "message_type": "success"
  },
  "body": [
    {
      "kind": "channel",
      "args": {
        "channel_name": "toast"
      }
    }
  ]
}
headers = {
  'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
  'content-type': "application/json"}
payload = json.dumps(send_message)
requests.post(os.environ['FARMWARE_URL'] + '/api/v1/celery_script',
              data=payload, headers=headers)
