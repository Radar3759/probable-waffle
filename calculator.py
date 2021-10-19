def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2    

operations = {
  "+": add,
  "-": subtract, 
  "*": multiply, 
  "/": divide
  }  

n1= int(input("What's the first number?: \n"))
#dict loops through keys
for symbol in operations:
  print(symbol)
operation_symbol = (input("\n What operation would you like? (see above) "))

n2= int(input("What's the second number?: \n"))
calc_function = operations[operation_symbol]
answer = (calc_function(n1, n2))
print(f"{n1} {operation_symbol} {n2} = {answer}")

operation_symbol = (input("\n Pick another operation (see above) "))
n3 = int(input("What's the next nubmer? \n"))
calc_function = operations[operation_symbol]
second_answer = calc_function(answer, n3)
print(f"{answer} {operation_symbol} {n3} = {second_answer}")
