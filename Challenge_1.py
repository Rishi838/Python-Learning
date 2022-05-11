import random
def Random_item(a,b,c):
    po=[]
    if c==2:
        po= random.choices(a, k=b)
    elif c==1:

        po= random.sample(a,b)
    return po


numbers = ['1', '2', '3', '4', '5', '6']
print(Random_item(numbers,2,1))
print(Random_item(numbers,2,2))
