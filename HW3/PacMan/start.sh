python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python2 pacman.py -l mediumCorners -p SearchAgent -a \
fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic
python2 pacman.py -l trickySearch -p SearchAgent \
-a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
python2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
