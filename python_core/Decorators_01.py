def div(a,b):
    print(a/b)
    

def smart_div(func):
    def inner_fn(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    
    return inner_fn

div = smart_div(div)

# div(4,2)
div(2,4)



