import matplotlib.pyplot as plt  
import numexpr as ne
import numpy as np  
import sympy as sp


from sympy.parsing.sympy_parser import (
  parse_expr, # converts string to sympy expression
  standard_transformations, # eg. 5! = 5*4*3*2*1
  implicit_multiplication_application, # e.g. 2x = 2*x
  convert_xor # e.g. 2^x = 2**x
)



# <----------------[PARSE EXPRESSION]----------------> #

def parseExpression(eq):

  transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
  equation = parse_expr(eq.replace('y=', ''), transformations=transformations)

  return equation



# <-------------------[PLOT GRAPH]-------------------> #

def plotGraph(equation, lower, upper):

  eq = parseExpression(equation)

  ax = plt.gca()

  x = np.linspace(lower, upper, 100)
  y = ne.evaluate(str(eq))

  ax.plot(
    x, y, 
    label = f"$y={sp.latex(eq)}$", 
    alpha = 0.5 # 50% transparent
  )
  
  ax.legend()
  ax.grid(True, linestyle=':')
  ax.spines['left'].set_position('zero')
  ax.spines['right'].set_color('none')
  ax.spines['bottom'].set_position('zero')
  ax.spines['top'].set_color('none')

  plt.xlim(lower, upper)
  plt.savefig('graph.png', dpi=300)
  plt.close()

  return