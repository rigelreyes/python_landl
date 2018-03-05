import pandas

dl = pandas.read_excel('hello_world.xlsx', sheet_name='Hello')
greetings = dl['Greetings']

print('Hello World!')
for name in greetings:
    print("Hello, " + name)
