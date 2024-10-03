x = 300

def myfunc():
  # x = 200
  global x
  x = 500
  print(x)

myfunc()

print(x)