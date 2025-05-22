# Decorators

def log_funcation_call(func):
   def wrapper():
      print("function is being called")
      return func()
   return wrapper




@log_funcation_call
def say_hello():
    print("hello Tanzeel")

say_hello()
      


