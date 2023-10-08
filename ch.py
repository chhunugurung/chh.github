def computepay(hours,rate):
    if hours < 40:
        pay=hours*rate
    else:
        regular_salary= 40*rate
        overtime_hours=hours-40
        overtime_salary=overtime_hours * (rate*1.5)
        pay=regular_salary + overtime_salary
    return pay

try:
    hours=float(input("enter the worked hours: "))
    rate=float(input("enter the rate: "))

    if hours<0 or rate<0 :
        print("hours and rate must be non-negative numbers: ")
    else:
        salary=computepay(hours,rate)
        print(f"total salary={salary}")  
except:
       print("invalid input,please enter valid input.")  
            