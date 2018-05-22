import random as rnd
from Towers import Tower
#This file contains functions that help place towers for coverage

def generate_tower(coverage_width, coverage_height):
	"""Creates and returns a new tower within the coverage constraints
	Arguments:
		coverage_width {int} -- Width of how much coverage wanted
		coverage_height {int} -- Height of how much coverage wanted
	"""
	assert isinstance(coverage_height,int) and coverage_height > 0, "Height must be an integer greater than 0"
	assert isinstance(coverage_width,int) and coverage_width > 0, "Width must be an integer greater than 0"

	# Generates a valid starting coordinate within coverage area
	rand_height = rnd.randint(1, coverage_height)
	rand_width = rnd.randint(1, coverage_width)
	x_coord = rnd.randint(0, coverage_width - rand_width)
	y_coord = rnd.randint(0, coverage_height - rand_height)
	start = (x_coord, y_coord)
	return Tower(start, rand_width, rand_height)

	
def get_possible_trims(new_tower, existing_tower):
	"""Gets a list of possible ways to trim the new tower based on current coverage
	Arguments:
		new_tower {Tower} -- tower that will be trimmed
		existing_tower {Tower} -- tower coverage that will be used to determine trims
	"""
	assert isinstance(new_tower, Tower), "new_tower must be a Tower"
	assert isinstance(existing_tower, Tower), "existing_tower must be a Tower"

	trims = []
	# If the towers intersect, determine trims. Otherwise, just use the new tower
	if new_tower.intersects(existing_tower): # true if intersects
		if new_tower < existing_tower: # checks if new covers anything to the left of existing
			temp = Tower(new_tower.start, existing_tower.start[0]-new_tower.start[0], new_tower.height)
			trims.append(temp)
		if new_tower > existing_tower: # checks if new covers anything to the right of existing
			new_start = (existing_tower.right_edge, new_tower.start[1])
			temp = Tower(new_start, new_tower.right_edge-existing_tower.right_edge, new_tower.height)
			trims.append(temp)
		if new_tower <= existing_tower: # checks if new covers anything below existing
			temp = Tower(new_tower.start, new_tower.width, existing_tower.start[1]-new_tower.start[1])
			trims.append(temp)
		if new_tower >= existing_tower: # checks if new covers anything above existing
			new_start = (new_tower.start[0], existing_tower.top_edge)
			temp = Tower(new_start, new_tower.width, new_tower.top_edge - existing_tower.top_edge)
			trims.append(temp)
		return trims
	else:
		return [new_tower]
		
	
def generate_max_tower(new_tower, existing_towers):
	"""maximizes coverage of a tower that should be trimmed, if possible
	Arguments:
		new_tower {Tower} -- tower that will be trimmed
		existing_towers {list} -- towers that have already been put down in the region
	"""
	assert isinstance(new_tower, Tower), "new_tower must be a Tower"
	assert isinstance(existing_towers, list), "existing_towers must be a list"
	assert all(isinstance(t, Tower) for t in existing_towers), "existing towers must only contain Towers"
	
	temp_towers = [new_tower]
	# Creates all possible trims by trimming repeatedly by all existing towers
	for t in existing_towers:
		temp = []
		for d in temp_towers:
			temp = temp + get_possible_trims(d, t) 
		if not temp:
			return None
		else:
			temp_towers = temp
			
	highest_area = 0
	biggest_tower = None
	for t in temp_towers:
		assert isinstance(t, Tower), "Element in list is not a Tower"
		if t.width*t.height > highest_area:
			highest_area = t.width*t.height
			biggest_tower = t
	return biggest_tower


