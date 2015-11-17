class Input:
	def __init__(self, value):
		self.value = value

	def set_value(self, value):
		self.value = value

	def output(self):
		return self.value

class Bias:
	def __init__(self, value):
		self.value = value

	def output(self):
		return self.value

class Neuron:
	def __init__(self):
		# Inputs:
		# {<Neuron_1>:weight_1, <Neuron_2>:weight_2, ..., <Neuron_n>:weight_n}
		# 
		# Output:
		# Value calculated using all inputs.
		
		self.inputs = {}

	def __str__(self):
		string = ''

		for neuron in self.inputs:
			string += 'Input value: ' + str(neuron.output()) + ' | Weight: ' + str(self.inputs[neuron]) + '\n'

		return string

	def output(self):
		output = 0

		for neuron in self.inputs:
			weight = self.inputs[neuron]
			output += neuron.output() * weight

		return output

	def add_input(self, neuron, weight):
		self.inputs[neuron] = weight

class Network:
	def __init__(self, in_count, hidden_count, out_count):
		self.inputs = [Neuron() for i in range(in_count)]
		self.hidden = [Neuron() for i in range(hidden_count)]
		self.outputs = [Neuron() for i in range(out_count)]

		for input_neuron in self.inputs:
			for neuron in self.hidden:
				# Start out with 1 as the weight
				neuron.add_input(input_neuron, 1)

		for hidden in self.hidden:
			for neuron in self.outputs:
				neuron.add_input(hidden, 1)

		self.input_values = []

	# Not finished
	def train(self, *inputs):
		if len(inputs) == len(self.inputs):
			if self.input_values == []:
				for i in range(len(inputs)):
					value = inputs[i]
				# for value in inputs:
					_input = Input(value)
					self.input_values.append(_input)
					# for neuron in self.inputs:
					neuron = self.inputs[i]
					neuron.add_input(_input, 1)
			else:
				for i in range(len(inputs)):
					value = inputs[i]
					self.input_values[i].set_value(value)



# net = Network(2, 3, 1)
# net.train(1, 2)

# Logic AND test
# A = 1
# B = 1
# n1 = Neuron()
# init1 = Input(A)
# init2 = Input(B)

# n1.add_input(init1, 1)
# n1.add_input(init2, 1)
# print(n1.output())