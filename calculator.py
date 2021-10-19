from art import logo

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
def calculator():
  print(logo)
  n1= float(input("What's the first number?: "))
  #with dict loops through keys
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:  
    operation_symbol = (input("\nWhat operation would you like? (see above) "))

    n2= float(input("What's the second number?: "))

    calc_function = operations[operation_symbol]
    answer = (calc_function(n1, n2))
    
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation ") == "y":
      n1 = answer
    else:  
      should_continue = False
      calculator()
calculator()      
