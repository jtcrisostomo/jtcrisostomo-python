try:
  hrs = float(input("Input Hours: "))
  rate = float(input("Input Rate: "))
  if hrs > 40:
    pay = 40*10 + (hrs-40)*1.5*rate
  else:
    pay = hrs * rate
  print("Pay: " + str(pay))
except:
  print("Error, please enter numeric input")