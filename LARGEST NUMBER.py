a = float(input(f"Enter the First Number\n"))
b = float(input(f"Enter the Second Number\n"))
c = float(input(f"Enter the Third Number\n"))
if a >= b and a >= c:
  print(f"The First number {a} is the largest\n")
elif b >= a and b >= c:
  print(f"The Second number {b} is the largest\n")
else:
  print(f"The Third number {c} is the largest\n")