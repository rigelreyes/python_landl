import json
import pandas as pndas

with open('assets/products.json') as json_file:
    data = json.load(json_file)
    print('Reading Json...')
    for p in data:
        print('Product: ' + p['product_name'])


file = pndas.read_json('assets/products.json')
file.to_excel('output.xls', index=False)