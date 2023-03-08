def addthis(x,y):
    import pdb;pdb.set_trace()
    print("x:",x," ",type(x),", y:",y," ",type(y))
    try:
        result=x+y
    except TypeError as exception:
        print("Wrong input:",exception)
        result=int(x)+int(y)
    return result

print(addthis("1",2))