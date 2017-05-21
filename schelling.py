#!/usr/bin/python
import random
import copy

DEBUG = False

def create_grid(agents, size=5):
    list_joined = [' '] * (pow(size, 2))
    
    # List of lists
    grid = []
    for n in range(size):
        new_line = list_joined[(size*n):(size*n+size)]
        grid.append(new_line)
    
    return grid


def is_satisfied(coord, agents, size):
    is_sat = True
    
    x,y = coord
    
    neighbor_set = set()
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if (i,j) == (x,y):
                # Don't add yourself
                continue
            elif i < 0 or i > size-1 or j < 0 or j > size-1:
                # outsize of grid
                continue
            neighbor_set.add((i,j))
    
    free_neighborhood = neighbor_set - agents
    
    if ( len(free_neighborhood) < 5 ):
        is_sat = False
    
    if DEBUG: 
        print "Looking at:", coord
        print "neighbor_set:", neighbor_set
        print "agents:", agents
        print "free_neighborhood:", free_neighborhood
        print "is_sat:", is_sat
    
    return is_sat, free_neighborhood


def print_grid(agents, size):
    grid = create_grid(agents, size)
    for a in agents:
        i,j = a
        grid[i][j] = 'X'
    
    for line in grid:
        print line
    

def update(agents, size):
    #print "In update()"
    rand_agents = list(agents)
    random.shuffle(rand_agents)
    for a in rand_agents:
        is_sat, free_neighborhood = is_satisfied(a, agents, size)
        if not is_sat and len(free_neighborhood) > 0:
            #print a, "is not satisfied and can move"
            #print "agents:", agents
            agents.discard(a)
            #print "agents:", agents
            free_list = list(free_neighborhood)
            random.shuffle(free_list)
            agents.add(free_list.pop())
            #print "moving to new place:"
            #print "agents:", agents
            return agents
    
    return agents
            
    # randomly pick agent
    # check if
    # find a cell that's unoccupied
    # 

def init_agents(nbr_agents, size):
    super_set = list()
    for i in range(size):
        for j in range(size):
            super_set.append((i,j))
    
    return set(random.sample(super_set, nbr_agents))
    
    

num_rounds=2000
mysize=10
nbr_agents=40

# mygrid = create_grid(agents=myagents, size=mysize)
agents = init_agents(nbr_agents, mysize)

print_grid(agents, mysize)

for i in range(num_rounds):
    old_agents = copy.deepcopy(agents)
    agents = update(agents, mysize)

    set_diff = old_agents - agents
    if len(set_diff) == 0:
        break

print "=============="
print_grid(agents, mysize)

# print agents
# agents.discard((4,3))
# print agents
# agents.add((4,3))
# print agents
