#this defines the main function, it has two variable it can take in the parentheses
#Below prints few lines with the variable. \n ensures there is an empty line between
#next print statement
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Here we are calling the chese and crackers function, directly stating what
#chese_count and boxes_of_crackers should be
cheese_and_crackers(20,30)

#Here we call the funcion but use variables which we define
print("OR, We can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calling function but doing math inside the parenthesis
print("We can even
 do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#calling function and using a mix of math and the above defined variables to
#determine what cheese_count and boxes_of_crackers should be.
print("And we can combine thw two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
