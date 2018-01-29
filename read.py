import os
import requests
import json

send_message = {
  "kind": "send_message",
  "args": {
    "message": "Bot is at position {{ x }}, {{ y }}, {{ z }}.",
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
