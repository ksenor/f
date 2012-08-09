# http://pyevolve.sourceforge.net/wordpress/?p=549
# Genetic Programming meets Python

from pyevolve import *
import math
 
error_accum = Util.ErrorAccumulator()
 
# This is the functions used by the GP core,
# Pyevolve will automatically detect them
# and the they number of arguments
def gp_add(a, b): return a+b
def gp_sub(a, b): return a-b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))
 
def eval_func(chromosome):
   global error_accum
   error_accum.reset()
   code_comp = chromosome.getCompiledCode()
 
   for a in xrange(0, 5):
      for b in xrange(0, 5):
         # The eval will execute a pre-compiled syntax tree
         # as a Python expression, and will automatically use
         # the "a" and "b" variables (the terminals defined)
         evaluated     = eval(code_comp)
         target        = math.sqrt((a*a)+(b*b))
         error_accum += (target, evaluated)
   return error_accum.getRMSE()
 
def main_run():
   genome = GTree.GTreeGP()
   genome.setParams(max_depth=5, method="ramped")
   genome.evaluator.set(eval_func)
 
   ga = GSimpleGA.GSimpleGA(genome)
   # This method will catch and use every function that
   # begins with "gp", but you can also add them manually.
   # The terminals are Python variables, you can use the
   # ephemeral random consts too, using ephemeral:random.randint(0,2)
   # for example.
   ga.setParams(gp_terminals       = ['a', 'b'],
                gp_function_prefix = "gp")
   # You can even use a function call as terminal, like "func()"
   # and Pyevolve will use the result of the call as terminal
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(1000)
   ga.setMutationRate(0.08)
   ga.setCrossoverRate(1.0)
   ga.setPopulationSize(2000)
   ga.evolve(freq_stats=5)
 
   print ga.bestIndividual()
 
if __name__ == "__main__":
   main_run()
