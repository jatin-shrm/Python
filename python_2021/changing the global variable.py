x=43
def function(n):
    #here this global l function grants the permission for changing in glabal variable
    global x
    w=5
    x=x+11
    print(w,"\nAfter changing the global variable",x)
function(x)
