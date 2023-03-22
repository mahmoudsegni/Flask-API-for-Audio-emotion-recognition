import requests as requests
import json
from argparse import ArgumentParser

parser = ArgumentParser(add_help=True)

parser.add_argument('--fileUrl', type=str, default='https://d358byuyocunuy.cloudfront.net/5a93bea5-3e2a-4ad7-926b-37eee1e493f2/ff10ae7d-fef1-4990-ae71-c9c1c61ebaa6-recording-2021-03-28--18-27-34.wav')
parser.add_argument('--host_port', type=str, default='5000')

hparams = parser.parse_args()
data = hparams.fileUrl
# The request url
url = 'http://localhost:'+hparams.host_port+'/'

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# Send the request
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)