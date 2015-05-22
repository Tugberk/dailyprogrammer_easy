#challenge 207
#dna replace

input = raw_input('enter as such a-g-t-d-c\n')
input = input.split('-')
print input

#lets create a dict
my_dict = {"a":"t",
           "t":"a",
           "g":"c",
           "c":"g"}

new_series = []
for char in input:
    char = my_dict[char]
    new_series.append(char)

print new_series


