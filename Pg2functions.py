#demonstration of function calling another function
# createrec is calling myfun
def myfun(**kwargs):
    for k,v in kwargs.items():
        print(k , " = " , v)
    print("------------------")
def createrec(id):
    print("Creating student rec = ")
    d = {}
    while True:
        prop = input("property name = ")
        val = input("property value = ")
        d[prop] = val
        ch = input("Press Yes to continue")
        if ch != "Yes":
            break
    print(d)
    myfun(student1=id,properties =d)

for id in (1,3):
    createrec(id)
