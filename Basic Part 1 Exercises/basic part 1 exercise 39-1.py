# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the
# editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def fut_val(princ, rate, time):
    answer = (princ)*(((rate/100) + 1) ** time)
    print(answer)

fut_val(100, 3.5, 7)