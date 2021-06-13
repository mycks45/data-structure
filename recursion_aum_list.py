
def greet(amount):
    if len(amount)==1:
        return amount[0]
    else:
        return amount[0] + greet(amount[1:])
    

amounts = [1,2,3,4,5]
result = greet(amounts)
print(result)