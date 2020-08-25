import random
heads=1
tails=2
tosses=20
total_h=0
total_t=0

def main():
    global  total_h
    global  total_t
    global  tosses
    for toss in range(tosses):
        if random.randint(heads,tails)==heads:
           total_h=total_h + 1
        else:
            total_t=total_t + 1
    print('total',total_h )
    print('total',total_t )
    print('total',tosses)
main()                