x = 0
sum = 0
n = 0
while str(x).lower() != "done":
  x = input("Enter a number: ")
  if x.lower() == "done":
    break
  try:
    x = int(x)
    sum += x
    n += 1
  except:
    print("Invalid input")
print(sum, n, sum/n)