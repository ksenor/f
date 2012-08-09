# http://pyevolve.sourceforge.net/wordpress/?p=780
# n-queens problem using Pyevolve

from pyevolve import *
from random import shuffle
 
BOARD_SIZE = 64
 
def queens_eval(genome):
   collisions = 0
   for i in xrange(0, BOARD_SIZE):
      if i not in genome: return 0
   for i in xrange(0, BOARD_SIZE):
      col = False
      for j in xrange(0, BOARD_SIZE):
         if (i != j) and (abs(i-j) == abs(genome[j]-genome[i])):
            col = True
      if col == True: collisions +=1
   return BOARD_SIZE-collisions
 
def queens_init(genome, **args):
   genome.genomeList = range(0, BOARD_SIZE)
   shuffle(genome.genomeList)
 
def run_main():
   genome = G1DList.G1DList(BOARD_SIZE)
   genome.setParams(bestrawscore=BOARD_SIZE, rounddecimal=2)
   genome.initializator.set(queens_init)
   genome.mutator.set(Mutators.G1DListMutatorSwap)
   genome.crossover.set(Crossovers.G1DListCrossoverCutCrossfill)
   genome.evaluator.set(queens_eval)
 
   ga = GSimpleGA.GSimpleGA(genome)
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
   ga.setMinimax(Consts.minimaxType["maximize"])
 
   ga.setPopulationSize(100)
   ga.setGenerations(5000)
   ga.setMutationRate(0.02)
   ga.setCrossoverRate(1.0)
 
   # This DBAdapter is to create graphs later, it'll store statistics in
   # a SQLite db file
   sqlite_adapter = DBAdapters.DBSQLite(identify="queens")
   ga.setDBAdapter(sqlite_adapter)
 
   ga.evolve(freq_stats=10)
 
   best = ga.bestIndividual()
   print best
   print "\nBest individual score: %.2f\n" % (best.score,)
 
if __name__ == "__main__":
   run_main()
