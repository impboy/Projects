def sales_tax(cost, tax):
  if tax > 1:
    tax = tax/100
    cost = round(cost*(tax+1), 2)
    answer = "The sales tax is " + str(tax) + "%, and the new cost is $" + str(cost) + "."
    return answer  
  else:
    cost = round(cost*(tax+1), 2)
    answer = "The sales tax is " + str(tax) + "%, and the new cost is $" + str(cost) + "."
    return answer
