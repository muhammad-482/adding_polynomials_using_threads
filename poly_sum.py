from math import floor
from  threading import *
import threading


'''we reprsent the polynomial as a list of coefficient
 which the first index represent the coefficient
  of the  varaible of the power zero and the second index is the coefficient of the variable
  of power one and so forth'''


# INPUT POLYNOMIAL
degree_of_poly1 = int(input("enter the dgree of the first polynomial: "))
poly1 = []
for i in range(degree_of_poly1+1):
    x = int(input(f"enter the coefficient of x{i} = "))
    poly1.append(x)
print("first poly: ")
print(poly1)

degree_of_poly2 = int(input("enter the dgree of the second polynomial: "))
poly2 = []
for i in range(degree_of_poly2+1):
    x = int(input(f"enter the coefficient of x{i} = "))
    poly2.append(x)
print("second poly: ")
print(poly2)
print("----------------------------------")


# FINDING BIGGER POLYNOMIAL LENGTH 
def finding_bigger_polynomial(poly1,poly2):
    if len(poly1)>len(poly2):
        return poly1
    elif len(poly2)>len(poly1):
        return poly2
    else:
        return poly1

# FINDING SHORTER POLYNOMIAL LENGTH 
def finding_shorter_polynomial(poly1,poly2):
    if len(poly1)<len(poly2):
        return poly1
    elif len(poly2)<len(poly1):
        return poly2
    else:
        return poly2    

# MODIFICATION MAKING THE POLYNOMIALS HAVING THE SAME LENGTH
def do_same_length(poly1,poly2):
    bigger_polynomial = finding_bigger_polynomial(poly1,poly2)
    shorter_polynomial = finding_shorter_polynomial(poly1,poly2)
    for i in range(len(bigger_polynomial)-len(shorter_polynomial)):
        shorter_polynomial.append(0)
    return shorter_polynomial,bigger_polynomial

both_polynomial = do_same_length(poly1,poly2)

# SPLIT THE POLYNOMIALS INTO HALF
both_polynomial = do_same_length(poly1,poly2)
modified_poly1 = both_polynomial[0]
modified_poly2 = both_polynomial[1]
length_of_polynomial =  len(modified_poly1)
modified_poly1_part1 = modified_poly1[0:floor(length_of_polynomial/2)]
modified_poly1_part2 = modified_poly1[floor(length_of_polynomial/2):length_of_polynomial]
modified_poly2_part1 = modified_poly2[0:floor(length_of_polynomial/2)]
modified_poly2_part2 = modified_poly2[floor(length_of_polynomial/2):length_of_polynomial]


#CLASS TO GET THE RETURNED VALUE OF A THREAD
class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

#ADD THE FIRST PARTS THREAD
def part1():
    sum_of_the_polynomial_part1 = [] 
    for i in range(len(modified_poly1_part1)):
            sum_of_the_polynomial_part1.append(modified_poly1_part1[i] + modified_poly2_part1[i])
    return(sum_of_the_polynomial_part1)

#ADD THE SECOND PARTS THREAD
def part2():
    sum_of_the_polynomial_part2 = [] 
    for i in range(len(modified_poly1_part2)):
            sum_of_the_polynomial_part2.append(modified_poly1_part2[i] + modified_poly2_part2[i])
    return(sum_of_the_polynomial_part2)  

t1 = ThreadWithReturnValue(target=part1,)
t2 = ThreadWithReturnValue(target=part2,)

t1.start()
t2.start()

sum_of_both_poly = t1.join() + t2.join()
print("our first poly: ")
print(poly1)
print("our second poly: ")
print(poly2)
print("sum of poly : ")
print(sum_of_both_poly)
