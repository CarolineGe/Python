the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print "This is count %r" % number

# same as above
# this "fruit" thing below can be anything like "xyz"
for fruit in fruits:
    print "A fruit of type: %s" % fruit
#in the line above, if we use %r then fruit names will show with quotes

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one:
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0,6):
    print "Adding %d to the list" %i
    #append i to the list
    elements.append(i)

#we can print them out

for i in elements:
    print "Element was:%d" %i
