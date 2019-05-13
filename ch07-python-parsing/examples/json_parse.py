#!/usr/bin/env python3

import json

file = '578.json'
data = json.load(open(file))
print(json.dumps(data, indent=4))
