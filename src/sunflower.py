def create_list(n):
	grid = []
	for i in range(0,n+1,+1):
		grid.append([])
	return grid
	
def sunflower_measure():
	world_size = get_world_size()
	seeds = power(world_size,2)
	grid = create_list(15)
	move_to(0,0)
	if num_items(Items.Sunflower_Seed) < seeds :
		trade_item(Items.Power,seeds)
	while not on_board_end():
		till_()
		plant(Entities.Sunflower)
		mes = measure()
		if mes != None:
			grid[mes].append((get_pos_x(),get_pos_y()))
		move_()
	till_()
	plant(Entities.Sunflower)
	grid[measure()].append((get_pos_x(),get_pos_y()))
	move_()
	i = find_index(grid)
	#while len(grid) >
	while i > 11 and num_items(Items.Sunflower_Seed) > 0: 
		data = grid[i]
		while len(grid[i]) > 0:
			pos = grid[i][0]
			move_to(pos[0], pos[1])
			grid[i].remove(pos)
			while not can_harvest():
				if num_items(Items.Fertilizer) > 0:
					fertilize()
				else:
					water()
			harvest()
			plant(Entities.Sunflower)
			index = measure()
			if index == None:
				break
			if index > i:
				i = index
			grid[index].append((get_pos_x(),get_pos_y()))	
		i -=1
	for i in grid:
		if len(i) > 0:
			pos = i[0]
			move_to(pos[0],pos[1])
			harvest()
			
def find_index(grid):
	for i in range(15,0,-1):
		row = grid[i]
		if len(grid[i]) > 0:
			return i 	

def clear_grid():
	move_to(0,0)
	while not on_board_end():
		harvest()
		move_()
	harvest()
	move_()