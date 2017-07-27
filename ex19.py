def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %s cheeses!" %cheese_count
    print "You have %s boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or we can get the function numbers by asking user to input:"
cheese_count = raw_input("input the number of cheese:")
boxes_of_crackers = raw_input ("input the number of crackers:")
cheese_and_crackers(cheese_count,boxes_of_crackers)
