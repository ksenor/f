# http://pyevolve.sourceforge.net/wordpress/?p=604
# Genetic Programming and Flex layouts

import random
from pyevolve import *
 
def gp_hbox(x, y):
   return "%s %s" % (x,y)
 
def gp_vbox(x, y):
   return "%s %s" % (x,y)
 
def gp_panel(x, y):
   return "%s %s" % (x,y)
 
def eval_func(chromosome):
   code_comp = chromosome.getCompiledCode()
 
   for a in xrange(0, 5):
      for b in xrange(0, 5):
         evaluated     = eval(code_comp)
   return random.randint(1,100)
 
def main_run():
   genome = GTree.GTreeGP()
   genome.setParams(max_depth=5, method="ramped")
   genome.evaluator += eval_func
 
   ga = GSimpleGA.GSimpleGA(genome)
 
   button     = repr("<mx:Button label='Button'/>")
   label      = repr("<mx:Label text='Label'/>")
   text_input = repr("<mx:TextInput width='50'/>")
 
   ga.setParams(gp_terminals       = [button, label, text_input],
                gp_function_prefix = "gp")
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.evolve(freq_stats=5)
   print ga.bestIndividual()
 
if __name__ == "__main__":
   main_run()
