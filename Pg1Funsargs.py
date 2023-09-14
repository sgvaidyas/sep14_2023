master = []
def myfun(*args):
    #print(*args)
    master.append(args)
    print(type(args))
    for x in args:
        print(x)
myfun("aaaa",999,True)
myfun("aaaa",999,True,"gjhghjgjj","hgfhfhfhfghfh")