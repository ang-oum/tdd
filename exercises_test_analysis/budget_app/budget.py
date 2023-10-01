

class Category:
  
  def __init__(self, category): #object instance
    self.category = category
    self.ledger = []            #instance variable

  def __str__(self):
    # When the budget object is printed it should display: #
    s = self.category.center(30, "*") + "\n"
    #A title line of 30 characters where the 
    #name of the category is centered in a line of * characters.
    for item in self.ledger:
      # A list of the items in the ledger.
      # The first 23 characters of the description should be displayed, then the amount.
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      # Each line should show the description and amount. 
      s += temp + "\n"
    s += "Total: " + str(self.get_balance())
    return s
    

    

    # The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    # A line displaying the category total.

  def deposit(self, amount, description=""):
    dict = {}
    dict["amount"] = amount      
    dict["description"] = description
    self.ledger.append(dict)
    # append an object to the ledger list in the form: 
    # {"amount": amount, "description": description}.
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      
      dict = {}
      dict["amount"] = 0 - amount
      dict["description"] = description
      self.ledger.append(dict)
      return True
    return False
    #  amount passed in should be stored in the ledger as a negative number. 
    # If there are not enough funds, nothing should be added to the ledger. 
    # if the withdrawal took place
    # This method should return True if the withdrawal took place, and False otherwise.
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      
      balance += item["amount"]
      
    return balance
    # returns the current balance of the budget category 
    # based on the deposits and withdrawals that have occurred.    
  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False
    # method should add a withdrawal
    # with the amount and the description:
    # "Transfer to [Destination Budget Category]". 
    # method should  add a deposit to the other budget category 
    # with the amount and the description "Transfer from [Source Budget Category]". 
    # If there are not enough funds, nothing should be added to either ledgers. 
    # This method should return True if the transfer took place, and False otherwise.
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True
    # It returns False if the amount is greater than the balance of the budget category 
    # and returns True otherwise.




def create_spend_chart(categories): #categories = list 
  # return a string that is a bar chart.
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "

  return s 
  

