#challenge 206
#about recursion

num = raw_input('starting number\n')

term_num = int(raw_input('up to which term \n'))
while term_num == "0": #this is to prevent for term num to be zero
    print "please enter another number"
    term_num = int(raw_input('up to which term \n'))

formula = raw_input('enter the formula\n')
print formula


def mult(num, i):
    num = int(num) * int(i[1:])
    print num
    return num

def subs(num, i):
    num = int(num) - int(i[1:])
    print num
    return num

def add(a,b):
    a = int(a) + int(b[1:])
    print a
    return a

def divide(num, i):
    num = int(num) / int(i[1:])
    print num
    return num


def solve(num, formula):
    print "number is:", num
    formula = formula.split()
    print formula
    for i in formula:
        for j in i:
            if j == "*":
                mult(num, i)

            elif j == "/":
                divide(num, i)
            elif j == "+":
                add(num, i)

            elif j == "-":
                subs(num, i)




solve(num, formula)




'''
def my_func(num, term_num, formula):
    print "number is: ", num
    print "we are going to show until term number: ", term_num
    formula = formula.split(" ")
    for i in formula:
        for j in i:
            #print j

            if j == "*":
                mult(num, i)
            elif j == "/":
                divide(num, i)
            elif j == "+":
                add(num, i)
            elif j == "-":
                subs(num, i)
    #print term_num
    i = 0
    while i < term_num + 1:

        print "term", i, "is:", num
        i = i + 1
'''

#my_func(num, term_num, formula)



