file = open('Day Three/input.txt', 'r')
lines = file.readlines()

#setup priorities
priorities_dict = {}
priority = 1
for char in range(ord('a'), ord('z')+1):
    priorities_dict[chr(char)] = priority
    priority+=1
for char in range(ord('A'), ord('Z')+1):
    priorities_dict[chr(char)] = priority
    priority+=1
def original_question(): 
    total = 0
    for line in lines:
        line = str(line)
        recurring_item = ""

        compartment_one = line[0:int(len(line)/2)]
        compartment_two = line[int(len(line)/2):-1]

        for item in compartment_one:
            for item2 in compartment_two:
                if item == item2:
                    recurring_item = item
                    break

        print(f"recurring item was: {recurring_item}")
        total = total + priorities_dict[recurring_item]


total = 0
current_line_num = 0

while current_line_num <= len(lines)-3:
    backpacks_array = ["", "", ""]    

    for x in range(0, 3):
       backpacks_array[x] = lines[current_line_num+x]
    
    for char in backpacks_array[0]:
        if char in backpacks_array[1] and char in backpacks_array[2]:
            print("found badge, is: ", char)
            total += priorities_dict[char]
            break

    current_line_num+=3

print(total)
