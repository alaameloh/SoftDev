import gdb
import sys

class ScanPointers(gdb.Command):

	def __init__ (self):
		super().__init__ ("fpointers", gdb.COMMAND_USER)
		#the type of command (COMMAND_USER) is a choice

	#the invoke method is for gdb when "FindPointers" is 
	def invoke (self, arg, from_tty):
		args = gdb.string_to_argv(arg) # getting the two arguments of fpointers
		address = int(args[0], 16)  #base 16 for address pointers	
		size = int(args[1]) #we could also cast size to a base16 int for homogeneity
		#print("address = {}".format(address))
		#print("size = {}".format(size))

		#looping over the addresses pool
		for i in range(size):
			#careful with the indexing
			entry = gdb.execute("x/gx {}".format(hex(address+i)), to_string=True)
			#print("entry = {}".format(entry))
			entry = entry.replace(":","").split("\t")
			target_address = int(entry[0], 16)
			content = int(entry[1], 16)
			if(content >= address and content <= address+size):
				print("Pointer at", hex(target_address), "-->", hex(content))

ScanPointers()