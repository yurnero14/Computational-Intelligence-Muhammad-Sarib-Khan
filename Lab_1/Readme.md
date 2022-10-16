<h1> Computational Intelligence Lab 1 </h1>

<h2> Sources </h2>
Puzzle problem from the course 
https://github.com/squillero/computational-intelligence/blob/master/2022-23/8-puzzle.ipynb

<h2> Solution Methodologies </h2>

<h3> Breadth First Search </h3>
Starting from the empty set, every element of the starting set is add to the frontier of which it is not the subset where it is going to be added. A cost is assigned to them.
The cost of new node will be evaluated as how many elements are duplicated when a new set is adding to an already existing set.
Frontier is a priority queue with a priority function where length of state is returned.

<h3> Depth First</h3>
The approach is similar to BFS, but in priority function length of the state has a negative sign 

<h2> Results </h2>
<h3>DFS</h3>
N = 5
Found a solution in 3 steps; The number of visited states: 16 
N = 10
Found a solution in 5 steps; The number of visited states: 96 
N = 20
Found a solution in 7 steps; The number of visited states: 129 
N = 100
Found a solution in 10 steps; The number of visited states: 3,072 
N = 500
Found a solution in 14 steps; The number of visited states: 21,311 
N = 1000
Solution not found for 1000

<h3>BFS</h3>
N = 5
Found a solution in 3 steps; The number of visited states: 32
N = 10
Found a solution in 3 steps; The number of visited states: 706
N = 20
Found a solution in 4 steps; The number of visited states: 15,790
N = 100
SOlution not found for 100 above
