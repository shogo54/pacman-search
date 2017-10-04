import pacman

'''
metarun.py runs things that look like command-line arguments
for Berkeley Python. You can leave the 'python pacman.py' part
at the beginning, or remove it, since we are not really running
from the command line.

You should comment out all lines in the file except one!
'''

# example
#pacman.main('--layout tinyMaze --pacman GoWestAgent')
#pacman.main('-l tinyMaze -p SearchAgent -a fn=tinyMazeSearch')

# dfs, bfs
#pacman.main('python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs')
#pacman.main('python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs')

# ucs
#pacman.main('python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs')
#pacman.main('python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs')
#pacman.main('python pacman.py -l mediumDottedMaze -p StayEastSearchAgent')
#pacman.main('python pacman.py -l mediumScaryMaze -p StayWestSearchAgent')

# aster
#pacman.main('python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic')

# corner problem with bfs
#pacman.main('python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem')
#pacman.main('python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem')

# corner problem with aster
#pacman.main('python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5')

# all food problem with ucs
#pacman.main('python pacman.py -l trickySearch -p SearchAgent -a fn=ucs,prob=FoodSearchProblem')

# all food problem with aster
#pacman.main('python pacman.py -l testSearch -p AStarFoodSearchAgent')
#pacman.main('python pacman.py -l trickySearch -p AStarFoodSearchAgent')

# all food problem with greedy
pacman.main('python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5')

