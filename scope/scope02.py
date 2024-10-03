y = 1
def myfunc():
  x = 300
  print(y)
  def myinnerfunc():
    print(x)
    print(y)
  myinnerfunc()

myfunc()