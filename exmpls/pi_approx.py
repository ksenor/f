# http://pyevolve.sourceforge.net/wordpress/?p=618
# Approximating Pi number using Genetic Programming

from __future__ import division
from pyevolve import *
import math
 
def gp_add(a, b): return a+b
def gp_sub(a, b): return a-b
def gp_div(a, b): return 1 if b==0 else a/b
def gp_mul(a, b): return a*b
def gp_sqrt(a):   return math.sqrt(abs(a))
 
def eval_func(chromosome):
   code_comp = chromosome.getCompiledCode()
   ret = eval(code_comp)
   return abs(math.pi - ret)
 
def step_callback(engine):
   gen = engine.getCurrentGeneration()
   if gen % 10 == 0:
      best = engine.bestIndividual()
      best_pi = eval(best.getCompiledCode())
      print "Best (%d): %.10f" % (gen, best_pi)
      print "\tError: %.10f" % (abs(math.pi - best_pi))
 
   return False
 
def main_run():
   genome = GTree.GTreeGP()
 
   genome.setParams(max_depth=8, method="ramped")
   genome.evaluator += eval_func
 
   ga = GSimpleGA.GSimpleGA(genome)
   ga.setParams(gp_terminals       = ['ephemeral:random.randint(1, 50)'],
                gp_function_prefix = "gp")
 
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(50000)
   ga.setCrossoverRate(1.0)
   ga.setMutationRate(0.09)
   ga.setPopulationSize(1000)
   ga.stepCallback.set(step_callback)
 
   ga.evolve()
   best = ga.bestIndividual()
   best.writeDotImage("tree_pi.png")
 
   print best
 
if __name__ == "__main__":
   main_run()
