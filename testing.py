print("Hello World!")

x = 2
if x == 1:
        #indented four spacess
        print("X is 1.")
else:
        print("X is !=1.")

# testing floats ands inputting hard coded parameters.
myfloat = 7.0
print(myfloat)
myfloat = float(5)
print(myfloat)
# this will output 1e-08
myfloat = 0.00000001
print(myfloat)

# this is a neat setup for easier assignments.
a, b = 3, 4
print(a, b)

# # this won't work - cannot mix numbers & strings.
# two = 2
# hello = "hello"

# print(one + " " + two + " " + hello)

# change this code
mystring = "hello"
myfloat = 10
myint = 20

# testing code - use STRING INTERPOLATION
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d , %d" %(myint, myint))

# testing out lists
numberList = [1,2,3,4]
print(numberList)
numberList.append(11)
print(numberList)
numberList.remove(2)
print("Removed 2, new numberList = ", numberList)

# squared numbers
squaredExample = 7 ** 2
cubedExample = 2 ** 3
print("7 ** 2 = ", squaredExample)
print("2 ** 3 = ", cubedExample)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# this just connects them together, it does not change the sequence.
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# prints this 3 times.
print([1,2,3] * 3)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

