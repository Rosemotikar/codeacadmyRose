2-Print the distinguished greeting “Hello world!”
print("Hello world!")
--------------------------------------------------------
#3-1-Print your name using the print() command.

print("Elon musk")
-------------------------------------------------
#4-2-If your print statement uses double-quotes ", change them to single-quotes '. If it uses single-quotes ', change them to double-quotes ".
Try running your code again after switching the type of quote-marks. Is anything different about the output?
'''do correction in first code using single quotes'''

print('Elon musk')
------------------------------------------------------
#5-Update the variable meal to reflect each meal of the day before we print it
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "None, because we are steaming"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner:")
print(meal)
-------------------------------------------------------------
#6-You might encounter a SyntaxError if you open a string with a single quote and end it with double quotes. Update the string so that it starts and ends with the same punctuation.
You might encounter a NameError if you try to print a single word string but fail to put any quotes around it. Python expects the word of your string to be defined elsewhere but can’t find where it’s defined. Add quotes to either side of the string to squash this bug.
Update the malformed strings in the workspace to all be strings.

print("This message has mismatched quote marks!")
print("Abracadabra")
---------------------------------------------------------------------
#7-1-A recent movie-going experience has you excited to publish a review. You rush out of the cinema and hastily begin programming to create your movie-review website: The Big Screen’s Greatest Scenes Decided By A Machine.
Create the following variables and assign integer numbers to them: release_year and runtime?

# Define the release and runtime integer variables below:

release_year = 2002
runtime = 150

#5-2-.Now, create the variable rating_out_of_10 and assign it a float number between one and ten?

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 9.4

--------------------------------------------------------------------
#8-Print out the result of this equation: 25 * 68 + 13 / 28

print(25 * 68 + 13 / 28)

-----------------------------------------------------

#9-1-You’ve decided to get into quilting! To calculate the number of squares you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length. Let’s make this first quilt 8 squares wide and 12 squares long.
2.
Print out the number of squares you’ll need to create the quilt!
3.
It turns out that quilt required a little more material than you have on hand! Let’s only make the quilt 8 squares long. How many squares will you need for this quilt instead?

quilt_width = 8
quilt_length = 12
print(quilt_width*quilt_length)


quilt_length = 8
print(quilt_width*quilt_length)

-----------------------------------------------------------------

#10-1.
You really like how the square quilts from last exercise came out, and decide that all quilts that you make will be square from now on.
Using the exponent operator, print out how many squares you’ll need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.
2.
Your 6x6 quilts have taken off so well, 6 people have each requested 6 quilts. Print out how many tiles you would need to make 6 quilts apiece for 6 people.

# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)

# 7x7 quilt
print(7 ** 2)

# 8x8 quilt
print(8 ** 2)

# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 2 * 6 ** 2)

-----------------------------------------------------------------
#11-You’re trying to divide a group into four teams. All of you count off, and you get number 27.
Find out your team by computing 27 modulo 4. Save the value to my_team.
2.
Print out my_team. What number team are you on?
3.
Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)


print(29 % 5)
# it returns 4, why that? Because if you divide 29/5 you obtain 5 with the remaining of 4 
# example 
my_team=(27%4)
print(my_team)
#output is 3
 
# to find out the team in each groups 
person = 0
 
while(person < 28):
  person = person + 1
  print("Person ", str(person), "= Team ", str(person % 4))

---------------------------------------------------------------------------------------------------------
#12-Concatenate the strings and save the message they form in the variable message.
Now uncomment the print statement and run your code to see the result in the terminal!

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6


#print(message)
print(message)

-------------------------------------------------------------------------------------------------
#13-We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

The prices (also included in the workspace) are:

new_sneakers = 50.00
nice_sweater = 39.00
fun_books = 20.00
Checkpoint 


total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater
total_price += fun_books


print("The total price is", total_price)
--------------------------------------------------------------------
#14-Assign the string

Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
to the variable to_you.

# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""



print(to_you)

------------------------------------------------------------------------------------
#15-Create variables:

my_age
half_my_age
greeting
name
greeting_with_name
Assign values to each using your knowledge of division and concatenation!


my_age = 34
half_my_age = my_age / 2
greeting = "Hi "
name = "Floor"
greeting_with_name = greeting + name

print(greeting_with_name)

# --------------------- Project: Furniture Store --------------------- #

#descriptions & prices
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

lovely_loveseat_price = 254.00

stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = 0.088

#customer 1
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization = customer_one_itemization + "|| " + luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

#customer 2
customer_two_total = 0
customer_two_itemization = ""
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description
customer_two_total += luxurious_lamp_price
customer_two_itemization = customer_two_itemization + "|| " + luxurious_lamp_description
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("Customer 2 Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)

-----------------------------------------------------------------------
-----------------------------------------------------------------------
