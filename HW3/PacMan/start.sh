# python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python2 pacman.py -l mediumCorners -p SearchAgent -a \
fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic
