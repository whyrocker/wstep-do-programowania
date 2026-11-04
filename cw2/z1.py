wzrost=float(input("podaj wzrost w metrach:"))
waga=float(input("podaj wage w kg:"))
bmi=waga/(wzrost**2)
print("twoje bmi wynosi:")
if  bmi < 18.5:
    print("niedowaga")
elif bmi<25 :
    print("waga prawidlowa")
elif bmi < 30:
    print("nadwaga")
else :
    print("otylosc")