#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


## two tests

#simple test
bill = 150
#(12%)
tip = 1.12
num_people = 5

each_pays = (bill + tip) / num_people
#format '.2f' makes 2 decimal places
print(format(each_pays,'.2f'))

#more complex

print("Welcome to the tip calculator")

bill = float(input("What was the total bill "))
tip_percent = int(input("What percent would you like to tip? 10, 12, or 15 "))
num_people = int(input("How many people split the bill? "))

#turns the tip percent into a decimal
tip_num = (tip_percent) / 100
#total plus tip is 1.xx * bill
bill_total = (1 + tip_num) * bill
print(bill_total)

#how much does each person play
each_pays = bill_total / num_people
#format '.2f' makes 2 decimal places
final_amount = "{:.2f}".format(each_pays)

print(f"Each person pays: ${final_amount}")


