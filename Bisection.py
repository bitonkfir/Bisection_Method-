from math import *
from sympy import *
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys

def f(symbolic_fuction):

    return lambdify(x, symbolic_fuction)

def Bisection_Method(a, b, function, epsilon):

    try:
        i=0
        if(isinstance(function(a),complex) == True or isinstance(function(b),complex) == True):
            return "none"
        else:
            if function(a) * function(b) <= 0 :
                c = (a + b) / 2
                while(abs(b - a) > epsilon ) :
                    print("Iteration number : ", i)
                    if(function(a) == 0):
                        return a
                    if(function(b) == 0):
                        return b
                    if(function(c) == 0):
                        return c
                    elif(function(a) * function(c) > 0):
                        a = c
                        print("Next a =", c)
                    elif(function(c) * function(b) > 0):
                        b = c
                        print("Next b =", c)

                    c = (a + b) / 2
                    print("(a, b) -> (", a,",", b, ")",'\n')
                    #print("(", a, "+", b, ") / 2 =", c)
                    if abs(b - a) <= epsilon :
                        print("Approximated root is :", c)
                    i += 1
                return c
            else:
                return "none"
    except ValueError:
            return "none"
    except ZeroDivisionError:
            return "none"
    except DomainError:
        return "none"

def derivative(symbolic_fuction):

    f_tag = diff(symbolic_fuction)
    x = Symbol('x')
    return lambdify(x, f_tag)

def roots(ranging, function, epsilon):

    count = 0
    j = 0
    rootList = []
    for k in ranging:
        if( j == len(ranging) - 1):#if j gets to the end of the list - 1
            return rootList

        tmp = Bisection_Method(ranging[j], ranging[j + 1], function, epsilon)
        if (not(tmp == "none")):
            if(len(rootList) > 0):
                if(tmp + 2 * epsilon >= rootList[count - 1]  or tmp - 2 * epsilon<= rootList[count - 1] ):
                    count = count + 1
                    rootList.append(tmp)
            else:
                count = count + 1
                rootList.append(tmp)
        j = j + 1
    print("")
    return rootList

def all_roots(ranging, fx, fx_tag, epsilon):
    fx_list = []
    fx_tag_list = []
    root_list = []
    merged_list = []

    print("***********************************************")
    print("** Bisection Formula is: root = (a + b) / 2  **")
    print("***********************************************")

    fx_list = roots(ranging, fx,  epsilon)
    fx_tag_list = roots(ranging, fx_tag, epsilon)
    print("****************************************")
    print("**The final steps for the last result:**")
    print("****************************************", '\n')
    print("1) Root list of f(x) before the comparison with f'(x) root list: ",fx_list,'\n')
    print("2) Roots of f'(x) are:", fx_tag_list,'\n')
    almostE = 0.00001

    for i in fx_tag_list:
        if(fx(i) <= almostE and fx(i) >= -almostE):
            root_list.append(i)

    for i in root_list:
        for j in fx_list:
            if (j <=  i + almostE and j >= i - almostE):
                continue
            else:
                 merged_list.append(i)

    for i in merged_list:

        fx_list.append(i)
    print("3) The final root list of f(x) is: ", fx_list)
    return fx_list

def intervals(Start_Domain, End_Domain, interval_jump):
    domains = []
    parameter = Start_Domain

    tmp = (End_Domain - Start_Domain) / interval_jump
    for i in range(interval_jump):
        domains.append(parameter)
        parameter += tmp

    domains.append(End_Domain)
    return domains

def plot_it(start, end, function, methodName):

    # Data for plotting
    t = np.arange(start, end, 0.001)
    s = function(t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='X', ylabel='Y',
        title = methodName)
    ax.grid()

    fig.savefig("test.png")
    plt.show()

def input_datas(ranging, fx, fx_tag, epsilon):
    rootList = all_roots(ranging, fx, fx_tag, epsilon)
    print("")
    rootList = set(rootList)
    rootList = list(rootList)
    rootList.sort()
    return rootList


if __name__ == '__main__':
# question 1:
#     x = Symbol('x')
#     epsilon = 0.0001
#     fx = input("enter an polynom:(example:x**3-3*(x**2)")
#     Start_Domain = float(input("enter the domain start:"))
#     End_Domain = float(input("enter the domain end:"))
#     assginment_func = f(fx)
#     fx_tag = derivative(fx)
#     fx = assginment_func
#     print(Bisection_Method(Start_Domain, End_Domain,fx, 0.0001))

#question 2:
    # x = Symbol('x')
    # epsilon = 0.0001
    # fx = input("enter an polynom:(example:x**3-3*(x**2)):")
    # Start_Domain = float(input("enter the domain start:"))
    # End_Domain = float(input("enter the domain end:"))
    # interval_jump=int(input("enter number of interval:"))
    # assginment_func = f(fx)
    # fx_tag = derivative(fx)
    # fx = assginment_func
    #
    # rootList = []
    # ranging = intervals(Start_Domain, End_Domain, interval_jump )
    #
    #
    # #List of roots
    # input_datas(ranging, fx, fx_tag,epsilon)
    # plot_it(0, 1, fx, "Bisection")
    pass