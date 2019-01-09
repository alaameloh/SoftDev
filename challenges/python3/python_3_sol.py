import sys
import copy

class Grid (object):
	def __init__(self):
		with open(str(sys.argv[1])) as f:
			raw_data = f.readlines()

		self.fire_indexes = [ [] for i in range(12)  ]
		self.free_tiles = [ [] for i in range(12)  ]
		self.grid = [list(line[:-1])for line in raw_data]
		self.path = ''
		self.forbidden = []
		for i,line in enumerate(self.grid) :
			for j,e in enumerate(line):
				if e =='&' : self.fire_indexes[i].append(j)
				if e =='S' : self.fireman_index = (i,j)
				if e =='E' : self.exit_index = (i,j)
				if e =='.' : self.free_tiles[i].append(j)

	def print_grid(self,grid):
		for elem in grid: print (elem)

	def count_fire_surrounding(self,x,y,input_grid) :
		# remember that indexing starts from 0 when you call this function
		if input_grid : grid= input_grid
		else : grid= self.grid
		num_of_fires = 0
		surrounding = 	   ((-1, -1), (-1,  0), (-1,  1),
	                       (0 , -1),           (0 ,  1),
	                       (1 , -1), (1 ,  0), (1 ,  1))
		for i,j in surrounding:
			if ((x+i)>=0) and (y+j)>=0 and (x+i)<12 and (y+j) < 16 :
				num_of_fires+= grid[x+i][y+j]=='&'
		return num_of_fires

	def evolve_fire(self):
		update_grid = copy.deepcopy(self.grid)
		update_fire_indexes = copy.deepcopy(self.fire_indexes)
		update_free_tiles = copy.deepcopy(self.free_tiles)
		#extingushing
		for i,line in enumerate(self.fire_indexes):
			if len(line)>0 :
				for j in line:
					if self.count_fire_surrounding(i,j,None) not in {2,3} :
						update_grid[i][j] = '.'
						update_free_tiles[i].append(j)
						update_fire_indexes[i].remove(j)

		#propagation
		for i,line in enumerate(self.free_tiles):
			if len(line)>0 :
				for j in line:
					if self.count_fire_surrounding(i,j,None) >2 :
						#if update_grid[i][j] == 'S' : print ('ALAAAAAAARRRRRMMM')
						update_grid[i][j] = '&'
						update_fire_indexes[i].append(j)
						update_free_tiles[i].remove(j)

		self.grid , self.fire_indexes, self.free_tiles = update_grid,\
								update_fire_indexes,update_free_tiles

	def de_evolve(self):
		self.grid = copy.deepcopy(self.previous_grid)
		self.fire_indexes = copy.deepcopy(self.previous_fire_indexes)
		self.free_tiles = copy.deepcopy(self.previous_free_tiles)
		self.fireman_index = copy.deepcopy(self.previous_fireman_index)

	def move_fireman(self):
		possible_moves = []
		tmp_grid = copy.deepcopy(self.grid)
		#propagation in a tmp grid to anticipate fire propagation
		for i,line in enumerate(self.free_tiles):
			if len(line)>0 :
				for j in line:
					if self.count_fire_surrounding(i,j,None) >2 :
						tmp_grid[i][j] = '&'


		a,b = self.exit_index
		x,y = self.fireman_index
		surrounding = 	   (			(-1,  0),
		                       (0 , -1),           (0 ,  1),
				                        (1 ,  0)			)
		for i,j in surrounding:
			if ((x+i)>=0) and (y+j)>=0 and (x+i)<12 and (y+j) < 16 :
				if tmp_grid[x+i][y+j] in {'.','E'} : possible_moves.append((i,j))

		if len(self.forbidden) > 0 :
			possible_moves.remove(self.forbidden[0])
			del self.forbidden[0]

		if len(possible_moves) > 0 :
			distances = [abs(a-x-i) + abs(b-y-j) for i,j in possible_moves]
			self.previous_grid = copy.deepcopy(self.grid)
			self.previous_fire_indexes = copy.deepcopy(self.fire_indexes)
			self.previous_free_tiles = copy.deepcopy(self.free_tiles)
			self.previous_fireman_index = copy.deepcopy(self.fireman_index)
			
			i,j = possible_moves[distances.index(min(distances))]
			self.previous_move = (i,j)
			self.fireman_index = (x+i,y+j)
			self.grid[x][y] = '#'  # using # to denote previous positions of
									# the fireman so he won't return
			self.grid[x+i][y+j] = 'S'
			translation_dict = {			(-1,  0):'N',
			                       (0 , -1):'W',           (0 ,  1):'E',
					                        (1 ,  0):'S'			}
			self.path+= translation_dict[(i,j)]
			return 0
			
		else : 
			#print('NO POSSIBLE MOVES ! ')
			self.forbidden.append(self.previous_move)
			self.path = self.path[:-1]
			return 1
		


def main():	
	max_moves = 22
	num_iteration = 0
	grid = Grid()
	
	#game loop
	while  (grid.fireman_index != grid.exit_index) and (max_moves > 0)  :
		##print('iteration n= {}  and {} moves left'.format(num_iteration,max_moves) )
		if (grid.move_fireman() == 0) :
			grid.evolve_fire()
			num_iteration+=1
			max_moves-=1
		else :
			max_moves +=1
			num_iteration+=1
			grid.de_evolve()
	
	print (grid.path)
		
if __name__ == '__main__' :
	main()