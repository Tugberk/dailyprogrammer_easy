#challenge 210

#first we need to convert every int into 32-bit binary.
#then we compare them; and look for the same bits in the same index
#0001 and 0000 has 3 elements in common -- 3/4 is the percentage we will give

#we should also give the inverse; and say
#x should avoid (the opp)
#y should avoid (the opp)

#todo
#find 32 bit
#find inverse
#find the common elements

print "please enter two numbers"
one = int(raw_input("first number: "))
two = int(raw_input("second number: "))


binary_numbers = ['','']
converted_numbers=['','']

#we change to binary here
binary_numbers[0] = "{0:b}".format(one)
binary_numbers[1] = "{0:b}".format(two)


new = ""

for i in range(len(binary_numbers[0]), 32):
               new = new + "0"
new = new + binary_numbers[0]
converted_numbers[0] = new

#we delete new so that we can use it again - we can also name it differently
new = ""

for i in range(len(binary_numbers[1]), 32):
               new = new + "0"
new = new + binary_numbers[1]
converted_numbers[1] = new

print converted_numbers


##now lets find the inverse of these numbers
##if the char is 1, we make it 0; if it is 0 we make it 1.

#here i am going to use replace function

replaced_converted = ['','']


#here we are creating the avoided numbers in 32bit

for i in range(0,2):
    replaced_converted[i] = binary_numbers[i].replace("1","i")
    replaced_converted[i] = replaced_converted[i].replace("0","1")
    replaced_converted[i] = replaced_converted[i].replace("i","0")

print "avoided:" , replaced_converted

#we also need to get this back to decimal numbers
#TODO


#now lets compare two numbers here.
#converted 0 with converted 1

common = 0

#lets split them both
converted_numbers[0] = str(converted_numbers[0])
converted_numbers[1] = str(converted_numbers[1])

#how to compare these two

list_one = []
list_two = []

for char in converted_numbers[0]:
    list_one.append(char)
for char in converted_numbers[1]:
    list_two.append(char)


for i in range(0,32):
    if list_one[i] == list_two[i]:
        common = common + 1

#print common
common = int(common)
perc = float(common) / float(32)
print perc*100,"% compatibility"

#now we should go back to decimals.

#print replaced_converted[0]
print one, "should avoid", int(replaced_converted[0], 2)
print two, "should avoid",int(replaced_converted[1], 2)
