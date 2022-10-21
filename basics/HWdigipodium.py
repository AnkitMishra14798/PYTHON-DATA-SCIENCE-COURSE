
# WAP to calculate the final salary of emp based on these rules ====>>>

sal = int(input('enter the amount of salary'))

if sal > 100000:
    da = 0.35 * sal 
    hra = 0.91 * sal
    total = ((.035*sal) + (.091*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 80000:
    total = ((.032*sal) + (.090*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 60000:
    total = ((.028*sal) + (.090*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 50000:
    total = ((.025*sal) + (.080*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 40000:
    total = ((.025*sal) + (.077*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 30000:
    total = ((.022*sal) + (.080*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 20000:
    total = ((.022*sal) + (.070*sal) + sal)
    print("the actual salary is : ",total)

elif sal > 10000:
    total = ((.022*sal) + (.060*sal) + sal)
    print("the actual salary is : ",total)

else:
    print("Sorry It's Worng Choice")