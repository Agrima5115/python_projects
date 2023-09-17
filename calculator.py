def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

operations = {"+":add,"-":sub,"*":mul,"/":div}

def calculator():
  num1 = float(input("Enter first number: "))
  
  for op in operations:
     print(op)
  
  should_continue = True
  while should_continue:
    op_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("Enter second number: "))
  # if op_symbol == "+":
  #   answer = add(num1,num2)
  # elif op_symbol == "-":
  #   answer = sub(num1,num2)
  # elif op_symbol == "*":
  #   answer = mul(num1,num2)
  # elif op_symbol == "/":
  #   answer = div(num1,num2)
  # else:
  #   print("Invalid operator!")
  
    cal_func = operations[op_symbol]
    answer = cal_func(num1,num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")

    i = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'e' to exit: ")
    if i == "y":
      num1 = answer
    elif i == "e":
      print("Thank you for using the calculator!")
      exit()
    else:
      should_continue = False
      calculator()

calculator()