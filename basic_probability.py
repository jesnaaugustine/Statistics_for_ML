''' 
Here trying to do some experiment on probability
'''

#probability of rolling a dice
import random
def prob_dice(n):
    sample_space =[1,2,3,4,5,6]
    exp = 100000
    c=0
    for i in range(exp):
        ev = random.choice(sample_space)
        if ev ==n:
            c+=1
    return c/exp

if __name__=='__main__':
    print(prob_dice(6))