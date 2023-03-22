import requests as requests
import json
import numpy as np


from argparse import ArgumentParser
from utils import *

parser = ArgumentParser(add_help=True)

parser.add_argument('--filepath', type=str)
parser.add_argument('--host_port', type=str, default='5000')

hparams = parser.parse_args()
path = hparams.filepath
feature = get_features(path).tolist()
#print(feature.dtype)
data=json.dumps(feature)
#operation = json.dumps(feature)


# The request url
url = 'http://localhost:'+hparams.host_port+'/'



#j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# Send the request
r = requests.post(url, data=data, headers=headers)
print(r, r.text)