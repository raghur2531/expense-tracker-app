from function import sort_amount,add_data,delete_data_date,search_transaction,amount_add
Transaction=[
    {"date":"2024-08-21","amount":"200","description":"fruits"},
    {"date":"2024-08-22","amount":"100","description":"petrol"},
    {"date":"2024-08-23","amount":"500","description":"snacks"},
    {"date":"2024-o8-24","amount":"2000","description":"grocary"},
]
flag=True
while flag:
  print("Expense Tracker App")
  print("1.Adding")
  print("2.Searching")
  print("3.Sorting")
  print("4.Deleting")
  print("5. Display")
  print("6.Add amount")
  print("7. Exit")
  Choice=int(input("Enter a choice: "))
  if Choice == 1:
    Transaction=add_data(Transaction)
  elif Choice == 2:
    date = input("Enter the date to search for: ")
    Transaction= search_transaction(date)
  elif Choice == 3:
    Transaction= sorting_transaction(Transaction)
  elif Choice == 4:
    Transaction= delete_data(Transaction)
  elif Choice == 5:
    print(Transaction)
  elif Choice ==6:
    print(amount_add(Transaction))
  elif Choice == 7:
    print("Exited")
    flag=False
  else:
    print("Enter right number")
