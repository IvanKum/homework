class Planets:
	img = ''
	planet_order = 0
	mass = 0
	volume = 0
	description = ''

	def print_description(self):
		print(self.description)

	def return_index(self):
		return self.volume / self.mass

Neptune = Planets()
Venus = Planets()

Saturn = Planets()
Saturn.planet_order = 6
Saturn.mass = 568340000000000000000000
Saturn.volume = 827130000000000
Saturn.img = "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg"
Saturn.description = 'Saturn is the sixth planet from the Sun and the \n' \
					 'second-largest in the Solar System, after Jupiter.\n' \
					 ' It is a gas giant with an average radius of about nine\n' \
					 ' and a half times that of Earth. It has only one-eighth the\n' \
					 ' average density of Earth; however, with its larger volume, \n' \
					 'Saturn is over 95 times more massive.'

Saturn.print_description()
print(Saturn.return_index())
