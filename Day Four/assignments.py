file = open("Day Four/input.txt", "r")
lines = file.readlines()

pairs = []
for line_num in range(0, len(lines)):
    split_pair = lines[line_num].split(',')
    print(split_pair)
