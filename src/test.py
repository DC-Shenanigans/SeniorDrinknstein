message = "this message is way longer than twenty characters and needs to be broken up in to different lines"
line_index = [1,2,3,4]
count = 0

print_output = ""
for idx,letter in enumerate(message):
    if count > 3:
        print("message too long for screen")
        break
    print_output = print_output + letter

    if len(print_output) == 20 or idx == len(message) - 1:
        print(f"{print_output} on line index {idx}, line {line_index[count]}")
        print_output = ""
        count += 1
