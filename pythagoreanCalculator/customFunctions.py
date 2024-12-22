def isFloat(element: any):
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
def listContains(lst, item, amount):
    if lst.count(item) == amount:
        return True
    else:
        return False