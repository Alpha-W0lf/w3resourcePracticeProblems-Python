# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

# kilopascal to PSI: divide by 6.895
# kilospascal to mmHg: multiply by 7.501
# kilopascal to atmosphere pressure: divide by 101

kilopascal = float(input("Enter pressure in kilopascals: "))


PSI = kilopascal / 6.895
mmHg = kilopascal * 7.501
atm = kilopascal / 101

print(kilopascal, PSI, mmHg, atm)
print("%g kilopascals is equal to %s PSI, %g mmHg, and %f atm." % (kilopascal, PSI, mmHg, atm))