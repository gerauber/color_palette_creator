import matplotlib as mpl
import os
import random

class Colours:
	def __init__(self, number: int, order: bool=False):
		self.number = number
		self.order = order
		self.list_cols_rgba=[]
		self.list_cols_hex=[]
			
	def get_palette(self):
		v=self.number
		cols,i=[],0
		lim_012t,lim_012p=0,0.9
		lim_3t,lim_3p=0.2,1
		def rand_col(min_val, max_val):
			return float(f'{random.uniform(min_val, max_val):<0.2f}')
		def too_close(list_cols, co):
			sum_lim=0.5
			for cols in list_cols:
				diff=[abs(cols[i]-co[i]) for i in range(len(cols))]
				if sum(diff)<=sum_lim:
					return True
			return False
		while i<v:
			co=[rand_col(lim_012t, lim_012p), 
			rand_col(lim_012t, lim_012p), 
			rand_col(lim_012t, lim_012p), 
			rand_col(lim_3t, lim_3p)]
			if co not in cols and not too_close(cols, co):
				cols.append(co)
				i+=1
		if self.order:
			cols.sort()
		self.list_cols_rgba=list(cols)
		self.list_cols_hex=[mpl.colors.rgb2hex(row, keep_alpha=True) for row in cols]
		
		
	def get_colours_rgba(self):
		return self.list_cols_rgba
		
	def get_colours_hex(self):
		return self.list_cols_hex
		
	def get_colours_str(self):
		txt='in RGBA: \n'
		txt+="[%s]"%", \n".join([str(c) for c in self.list_cols_rgba])
		txt+='\nin hex: \n'
		txt+="[%s]"%", \n".join([str(c) for c in self.list_cols_hex])
		return txt

	def get_print(self):
		print("The colours are")
		print(self.get_colours_str())
		

	def save_colours(self, path, name):
		if os.path.exists(f'{path}{name}.txt'):
			i=0
			while os.path.exists(f'{path}{name}_{i}.txt'):
				i+=1
			file_name=f'{path}{name}_{i}.txt'
		else:
			file_name=f'{path}{name}.txt'
		f=open(file_name,"w+")
		f.write(self.get_colours_str())
		f.write("\n")
		f.close()

	def quest_save_colours(self):
		print("Would you like to save the last colors?")
		choice_save_cols = input("(y/n): ")
		if choice_save_cols!='y' and choice_save_cols!='n':
			while choice_save_cols!='y' and choice_save_cols!='n':
				choice_save_cols = input("Please enter either 'y' or 'n': ")
		return choice_save_cols
		
	def quest_path_name(self):
		print("Please enter")
		choice_path=input("file path: ")
		choice_name=input("file name: ")
		return [choice_path, choice_name]
		
	def quest_path_name_corr(self):
		choice_path, choice_name=self.quest_path_name()
		print("\nIs this correct?")
		print(f"File path: {choice_path}\nFile name: {choice_name}")
		choice_path_name=input("(y/n): ")
		if choice_path_name!='y' and choice_path_name!='n':
				while choice_path_name!='y' and choice_path_name!='n':
					choice_path_name=input("Please enter either 'y' or 'n': ")
		if choice_path_name=='n':
			self.quest_path_name_corr()
		if choice_path_name=='y':
			self.save_colours(choice_path, choice_name)
			return [choice_path, choice_name]

	def print_question(self):
		choice_path,choice_name=None,None
		choice_save_cols=self.quest_save_colours()
		if choice_save_cols=='y':
			choice_path,choice_name=self.quest_path_name_corr()
		return [choice_path, choice_name]
			
		
		
