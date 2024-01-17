def func1():
    try:
        lst=[1,2,3,6,9]
        i = int(input("enter the index:"))
        print(lst[i])
        return 1
    except:
        print("Error occurued!")
        return 0
    finally:
        print("always excuted")

print (func1())