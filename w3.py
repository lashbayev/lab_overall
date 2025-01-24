#Modules
import mymodule
import platform #built-in platform

mymodule.greeting('Khaby')

a = mymodule.person1["age"]
print(a)

x = platform.system()
print(x) #outputs windows

x = dir(platform)
print(x)

x = dir(mymodule)
print(x)

#'from' keyword
from mymodule import person1

print (person1["age"])
