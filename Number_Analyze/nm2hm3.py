import sympy
import random
import numpy as np
import matplotlib.pyplot as plt
import math

x=sympy.symbols('x')

def cubicSpline(x_val,y):
    h=[x_val[i+1]-x_val[i] for i in range(len(x_val)-1)]
    M = sympy.symbols(" ".join(f"M_{x_val+1}" for x_val in range(len(x_val))), real=True)    
    x=sympy.symbols('x')
    ans=[]
    for i in range(len(x_val)-2):
        ans.append(sympy.Eq(h[i]*M[i]+2*(h[i]+h[i+1])*M[i+1]+h[i+1]*M[i+2],3*((y[i+2]-y[i+1])/h[i+1]-(y[i+1]-y[i])/h[i])))
    ans.append(sympy.Eq(sympy.integrate(M[1],x,x),y[1]))
    ans.append(sympy.Eq(sympy.integrate(M[-2],x,x),y[-2]))
    sol=sympy.solve(ans)[0]
    final=[]
    for i in range(len(x_val)-1):
        a=((M[i+1]-M[i])/(3*h[i])).subs(sol)
        b=M[i].subs(sol)
        c=((y[i+1]-y[i])/h[i]-h[i]*(M[i+1]+2*M[i])/3).subs(sol)
        x=sympy.symbols('x')
        Pn=sympy.simplify(a*(x-x_val[i])**3+b*(x-x_val[i])**2+c*(x-x_val[i])+y[i])
        final.append((Pn,(x_val[i],x_val[i+1])))
    return(final)

def naturalCubicSpline(x_val, y):
    h = [x_val[i+1] - x_val[i] for i in range(len(x_val) - 1)]
    b = [(y[i+1] - y[i]) / h[i] for i in range(len(x_val) - 1)]
    bi = [6 * (b[i+1] - b[i])for i in range(len(b) - 1)]
    li = [[h[i], 2 * (h[i] + h[i+1]), h[i+1]] for i in range(len(h)-1)]
    S = sympy.symbols(" ".join(f"S_{x_val+1}" for x_val in range(len(x_val))), real=True)
    finals = [sympy.Eq(sum([li[i][j] * S[i+j] for j in range(3)]), bi[i]) for i in range(len(bi))]
    sol = {S[0]: 0, S[-1]: 0}
    sol.update(sympy.solve([f.subs(sol) for f in finals]))
    final = []
    for i in range(len(x_val) - 1):
        a = ((S[i+1] - S[i]) / (6 * h[i])).subs(sol)
        b = (S[i] / 2).subs(sol)
        c = ((y[i+1] - y[i]) / h[i] - (2 * h[i] * S[i] + h[i] * S[i+1]) / 6).subs(sol)
        d = y[i]
        x=sympy.symbols('x')
        Pn = (sympy.simplify(a * (x - x_val[i]) ** 3 + b * (x - x_val[i]) ** 2 + c * (x - x_val[i]) + d)).subs(sol)
        final.append((Pn, (x_val[i], x_val[i+1])))
    return(final)
    
def column(matrix, i):
    return [row[i] for row in matrix if i<len(row)]

def divided_difference(x, y):
    n = len(x)
    table = [[0] * (n - i) for i in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    return table

def newtonInterpolation(x_val):
    table=(divided_difference(x_values,y_values))
    matrix=[]   
    for i in range(len(table)):
        matrix.append(column(table,i))
    x=sympy.symbols('x')
    ksi=1
    Pn=[matrix[0][0]]
    for i in range(0,len(x_val)-1):
        ksi*=(x-x_val[i])
        ans=Pn[i]+matrix[i+1][0]*ksi
        Pn.append(ans)
    return[(Pn[-1],(x_val[0],x_val[-1]))]

def newtonInterpolationlog(x_val):
    y_values=[0,0,math.log(2),math.log(6),math.log(24)]
    table=(divided_difference(x_values,y_values))
    matrix=[]   
    for i in range(len(table)):
        matrix.append(column(table,i))
    x=sympy.symbols('x')
    ksi=1
    Pn=[matrix[0][0]]
    for i in range(0,len(x_val)-1):
        ksi*=(x-x_val[i])
        ans=Pn[i]+matrix[i+1][0]*ksi
        Pn.append(ans)
    return[(sympy.exp(Pn[-1]),(x_val[0],x_val[-1]))]



def plotFunc(source,color,name,show):
    for func, (xmin, xmax) in source:
        x=sympy.symbols('x')
        xs = np.linspace(xmin, xmax, 100)
        
        y = [func.subs(x,i) for i in xs]
        plt.plot(xs, y,color)
    plt.plot(source[0][1][0],source[0][1][0],color,label=name)
    if show:
        plt.show()
def plotGamma(y_val,color,name,show):
    plt.plot(x_values,y_val,color,label=name)
    if show:
        plt.show()

def gammaF(x_val):
    y=[math.gamma(x) for x in x_val]
    
    return y

def startPlot(indexes):    
    for i in range(len(indexes)):
        print("\n",labels[indexes[i]],"=")
        print(li[indexes[i]])
        if indexes[i]==len(labels)-1:
            plotGamma(li[-1],colors[-1],labels[-1],False)
            colors.pop(-1)
        else:
            plotFunc(li[indexes[i]],colors[0],labels[indexes[i]],False)
            colors.pop(0)
    plt.scatter(x_values,y_values,label="Given Function Values")

x_values = [1,2,3,4,5]
y_values = [1,1,2,6,24]

labels=["Newton Interpolation P(x)","Newton Interpolation Log Q(x)","Cubic Spline","Natural Cubic Spline S(x)",f"Gamma \u0393(x)"]
colors=[]
for i in range(6):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    colors.append(hex_color)
li=[
    newtonInterpolation(x_values),
    newtonInterpolationlog(x_values),
    cubicSpline(x_values,y_values),
    naturalCubicSpline(x_values,y_values),
    gammaF(x_values)
]

startPlot([0,1,2,3])

Gamma=1
for i in range(len(x_values)):
    Gamma*=(x-x_values[i]) 
t=sympy.symbols('t')
gamma=sympy.sqrt(2*sympy.pi*(x-1))*((x-1)/sympy.exp(1)**(x-1))
maxPsi=sympy.maximum(Gamma,x,sympy.Interval(0,5)).evalf()
maxDerKsi=sympy.maximum(sympy.diff(gamma,x,len(x_values)),x,sympy.Interval(0,5)).evalf()
print("Normal Error",maxPsi*maxDerKsi/math.factorial(len(x_values)))
h=(x_values[-1]-x_values[0])/(len(x_values)-1)
print("Spline:",5/384*h**2)
print("Log ",maxPsi*maxDerKsi/math.factorial(len(x_values)))


plt.legend(loc='upper left')
plt.show()