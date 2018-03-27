import pandas

# Reading the excel and creating an array
dl = pandas.read_excel('assets/hello_world.xlsx', sheet_name='Hello')
greetings = dl['Greetings']

# Printing the array
print('Hello World!')
for name in greetings:
    print("Hello, " + name)
