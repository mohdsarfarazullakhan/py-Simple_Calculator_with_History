history_file="history,txt"

def show_history():
  file=open(history_file,'r')
  lines=file.readlines()
  if len(lines)==0:
    print("No History Found!!")
  else:
    for line in reversed(lines):
      print(line.strip())
  file.close()

def clear_history():
  file=open(history_file,'w')
  file.close()
  print("History cleared.")

def save_to_history(equation,result):
  file=open(history_file,'a')
  file.write(f"{equation} = {result}\n")
  file.close()
def calculator(user_input):
  parts=user_input.split()
  if len(parts) !=3:
    print("invalid input. use format: num op num ( e.g 9 + 9)")
    return

  num1=float(parts[0])
  op=parts[1]
  num2=float(parts[2])

  if op == '+':
    result=num1+num2
  elif op == '-':
    result=num1-num2
  elif op == '*':
    result=num1*num2
  elif op == '/':
    if num2 !=0:
      result=num1/num2
    else:
      print("Error: Division by zero")
  else:
    print("Inavalid operator. use only + _ * / ")
    return

  if int(result)==result:
    result=int(result)
  print(f"Result: {result}")
  save_to_history(user_input,result)


def main():
  print("-----WELCOME TO SIMPLE CALCULATOR--------")
  while True:
    user_input=input("Enter calcuation (+ _ * / ) or command (history , clear or exit) =  ")
    if user_input.lower()=='exit':
      print("Exiting the calculator. Goodbye!")
      break
    elif user_input.lower()=='history':
      show_history()
    elif user_input.lower()=='clear':
      clear_history()
    else:
      calculator(user_input)
    

if __name__=="__main__":
  main()

