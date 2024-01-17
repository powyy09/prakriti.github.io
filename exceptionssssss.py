a = input("enyer a number:")
print (f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print (f"{int(a)} x {i} = {int(a)*i}")
except exception as e:
    print("An error occured")

print("hieeeee")    