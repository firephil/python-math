import csv
import json

with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
f.close()

json_data = json.dumps(data,indent=4)

with open('sample.json', 'w') as f:
    f.write(json_data)