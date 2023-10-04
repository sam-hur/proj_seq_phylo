with open('input.txt', 'r') as f:
    contents = f.read().split('\n')

header = contents[0]
body = "".join(str(line) for line in contents[1:])
out = header + '\n' + body

# print(out)

with open('output.txt', 'w') as f:
    f.write(out)