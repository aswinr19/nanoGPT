

with open('state.txt','r', newline='') as f:
    attrs = f.read()


values = attrs.split(',')

for val in values:
    print(val.strip())
