def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time - 1)

principal = 1000
rate = 5
time = 2
print("Compound Interest:", compound_interest(principal, rate, time))