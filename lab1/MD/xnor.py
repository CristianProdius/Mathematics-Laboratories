def xnor(a,b):

    return ((a and b) or ((not a) and (not b)))

inp1 = input()
inp2 = input()

if inp1.lower() == "false" or inp1 == "0":
    inp1 = ""

if inp2.lower() == "false" or inp2 == "0":
    inp2 = ""

print(xnor(inp1,inp2))