import json
import pandas as pndas
#Reading the json file with json library
with open('assets/products.json') as json_file:
    data = json.load(json_file)
    print('Reading Json...')
    for p in data:
        print('Product: ' + p['product_name'])

#Reading json file with pandas
file = pndas.read_json('assets/products.json')
file.to_excel('output.xls', index=False)