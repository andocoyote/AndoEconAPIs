import sympy
import sys


def ValidateSymbols(symbols: str) -> list:
    if not symbols:
        print('Error: symbols string is null or empty.')
        return None
    
    symbols = symbols.split(' ')
    
    if len(symbols) < 1:
        print('Error: no valid symbols found in symbols string.')
        return None
    
    for symbol in symbols:
        if len(symbol) > 1:
            print('Error: symbol \'{0}\' is malformed.'.format(symbol))
            return None
        
    return symbols


def ParseEquation(symbols: str, fx: str) -> sympy.core.expr.Expr:
    fx = sympy.sympify(fx)
    
    return fx


def Derivative(symbols: str, fx: str) -> str:
    symbols = ValidateSymbols(symbols)
    
    # Declare an equation that we want to differentiate
    fx = ParseEquation(symbols, fx)
    
    # Create the variables for symbols we'll be using from the symbols param
    for symbol in symbols:
        locals()[symbol] = sympy.Symbol(symbol)
    
    # Differentiate it.  Should yield: 5*x**4 + 28*x**3
    derivative = sympy.diff(fx)
    
    return derivative
    

def PartialDerivative(symbols: str, fx: str, variable: str) -> str:
    symbols = ValidateSymbols(symbols)
    
    # Declare an equation that we want to differentiate
    fx = ParseEquation(symbols, fx)
    
    # Create the variables for symbols we'll be using from the symbols param
    for symbol in symbols:
        locals()[symbol] = sympy.Symbol(symbol)
    
    # Differentiate it.  Should yield: 5*x**4 + 28*x**3
    derivative = sympy.diff(fx, variable)
    
    return derivative


def Solve(symbols: str, fx: str, subs: dict) -> float:
    symbols = ValidateSymbols(symbols)
    
    # Declare an equation that we want to differentiate
    fx = ParseEquation(symbols, fx)
    
    # Create the variables for symbols we'll be using from the symbols param
    for symbol in symbols:
        locals()[symbol] = sympy.Symbol(symbol)
    
    result = fx.subs(subs).evalf()
    
    return result
    

def main() -> int:
    # Power Rule
    fx = 'x**5 + 7*x**4 + 3'
    
    # Differentiate it.  Should yield: 5*x**4 + 28*x**3
    derivative = Derivative('x', fx)
    print(derivative)
    
    # Product Rule
    fx = 'x**2 + 1'
    gx = 'cos(x)'
    
    # Differentiate it.  Should yield: 2*x*cos(x) - (x**2 + 1)*sin(x)
    derivative = Derivative('x', '(' + fx + ') * (' + gx + ')')
    print(derivative)
    
    # Chain Rule
    fx = '(x**2 - 3*x + 5)**3'
    
    # Differentiate it.  Should yield: (6*x - 9)*(x**2 - 3*x + 5)**2
    derivative = Derivative('x', fx)
    print(derivative)
    
    
    # Partial Derivatives
    
    # f(x) = x^2yz^5
    fx = 'x**2 * y * z**5'
    
    # Partial derivative with respect to x: 2*x*y*z**5
    derivative = PartialDerivative('x y z', fx, 'x')
    print(derivative)
    
    # Partial derivative with respect to y: x**2*z**5
    derivative = PartialDerivative('x y z', fx, 'y')
    print(derivative)
    
    # Partial derivative with respect to z: 5*x**2*y*z**4
    derivative = PartialDerivative('x y z', fx, 'z')
    print(derivative)
    
    # Utility function for pizza and cookies
    fx = 'sqrt(p * c)'
    
    # Differentiate f(x) with respect to p: sqrt(c*p)/(2*p)
    MUp = PartialDerivative('p c', fx, 'p')
    print(MUp)
    
    # Differentiate f(x) with respect to c: sqrt(c*p)/(2*c)
    MUc = PartialDerivative('p c', fx, 'c')
    print(MUc)
    
    # If c is 2 and p is 5:
    subs = {'c':2, 'p':5}
    
    result = Solve('p c', MUp, subs)
    print(result)
    
    result = Solve('p c', MUc, subs)
    print(result)
    
    return 0
    

if __name__ == '__main__':
    sys.exit(main())
