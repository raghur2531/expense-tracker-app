def sort_amount(transaction):
  for i in range(len(transaction)):
    for j in range(0,len(transaction)-1):
      if transaction[j]["amount"]>transaction[j+1]["amount"]:
        transaction[j],transaction[j+1]=transaction[j+1],transaction[j]
  return transaction
def add_data(transaction):
  date=input("enter the date: ")
  amount=input("enter the amount: ")
  description=input("enter the description: ")
  return transaction
def delete_data_date(transaction,date):
  for transaction in transactions:
    if transaction["date"] == date:
      transaction.remove(transaction)
  return transaction
def search_transaction(date):
    for transaction in Transaction:
        if transaction["date"]==date:
            return transaction
    return None
def amount_add(Transaction):
  total_amount=0
  year=input("Enter the year:")
  for transaction in Transaction:
    if transaction['date'][0:4]==year:
      total_amount+=int(transaction["amount"])
  return total_amount
