

with open('mj.txt', 'r') as  reader:
    content = reader.readlines()
    reversed(content)
    with open('mj.txt' , 'w') as writer:
        for line in reversed(content):
            writer.write(line)
