# python program to calculate simple intrest

princ_amount = float(input("please enter the principal amount:"))
rate_of_int = float(input("please enter the rate of intrest:"))
time_period = float(input("please enter time period in year:"))

simple_interest = (princ_amount * rate_of_int * time_period)/100

# print("\nsimple interest for principal amount {0} = {1}". format (princ_amount,simple_interest,))
print(simple_interest)

