class person:
    def __init__(self,name,occupation):
        print ("hello!")
        self.name = name
        self.occ = occupation
        print(f"{self.name} is a {self.occ}")
      
a = person("Prakriti","DS")


class info:
    nam = "prakriti"
    age = 17

    def info(self):
        print(f"{self.nam} is {self.age} years old.")

c = info()
c.info()