input = open('input.txt', 'r')
lines = input.readlines()
highest_total = 0
current_total = 0

top_three_calories = [0,0,0]

def top_three_check(num):
    for i in range(0, 3): 
        if num > top_three_calories[i]:
            top_three_calories[i] = num
            break
            
for line in lines:
    if line != '\n':
        current_total = current_total + int(line.split()[0])
    else:
        top_three_check(current_total)
        current_total = 0

print(sum(top_three_calories))
