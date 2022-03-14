class Instance: 
	def __init__(self, name):
		sequences = []
		file = open(name)
		for line in file:
			if not line.startswith(">"):
				sequences.append(line)
		file.close()

		self.seq1 = sequences[0].rstrip()
		self.seq2 = sequences[1]
		self.length = 0
		self.rna1 = ""
		self.rna2 = ""
		self.hamming_dis = 0

	def check_length(self):
		if len(self.seq1) == len(self.seq2):
			self.length = len(self.seq1)
		else:
			print("This program works only for sequences of the same length.\nPlease make sure that sequences in your input file are of the same length.")
			exit()

	def hamming_distance(self):
		if self.length > 0:
			nucleotides = Iterator(self.seq1, self.seq2)
			for i, nucl in enumerate(nucleotides):
				if nucl[0] != nucl[1]:
					self.hamming_dis += 1

	def transcription(self):
		if self.length > 0:
			nucleotides = Iterator(self.seq1, self.seq2)
			for i, nucl in enumerate(nucleotides):
				if nucl[0] == 'T':
					self.rna1 += 'U'
					self.rna2 += nucl[1]
				elif nucl[1] == 'T':
					self.rna1 += nucl[0]
					self.rna2 += 'U'
				elif nucl[0] == 'T' and nucl[1] == 'T':
					self.rna1 += 'U'
					self.rna2 += 'U'
				else:
					self.rna1 += nucl[0]
					self.rna2 += nucl[1]

	def print_info(self):
		print(self.seq1)
		print(self.seq2)
		print(len(self.seq1))
		print(len(self.seq2))
		print(f'Hamming distance is {self.hamming_dis}.\n')

	def print_premrna(self):
		print(f'Pre-mRNA1: {self.rna1}\nPre-mRNA2: {self.rna2}\n')

	def save_file(self, name):
		output = open(name, 'w')
		output.write(f'Sequence 1:\n{self.seq1}\nSequence 2:\n{self.seq2}\n')
		output.write(f'\nHamming distance is {self.hamming_dis}.\n\n')
		output.write(f'Pre-mRNA 1:\n{self.rna1}\nPre-mRNA 2:\n{self.rna2}')
		output.close()
		

class Iterator:
	def __init__(self, seq1, seq2):
		self.seq_val = -1
		self.seq_1 = seq1
		self.seq_2 = seq2
		self.seq1_len = len(seq1) - 1
		self.seq2_len = len(seq2) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.seq_val >= self.seq1_len and self.seq_val >= self.seq2_len:
			raise StopIteration
		elif self.seq_val < self.seq1_len and self.seq_val < self.seq2_len:
			self.seq_val += 1
			return [self.seq_1[self.seq_val], self.seq_2[self.seq_val]]

if __name__ == '__main__':
	filename = "instance.txt"
	ins = Instance(filename)
	ins.check_length()
	ins.hamming_distance()
	ins.transcription()
	ins.print_info()
	ins.print_premrna()
	save_filename = input("Enter the name of a save file (without any filename extension): ")
	save_filename += '.txt'
	ins.save_file(save_filename)
