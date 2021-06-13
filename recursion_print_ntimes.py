
def greet(k):
    if k>0:
        print('hello')
        greet(k-1)

greet(8)