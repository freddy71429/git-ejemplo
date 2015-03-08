class Cliente:

	def __init__(self, nombre, dni, fech_nac):
		self.nombre = nombre
		self.dni = dni
		self.fech_nac = fech_nac

	def get_nombre(self):
		
		return self.nombre

	def show(self):

		print self.get_nombre()



cliente = Cliente("Freddy C","12345678","12-03-2000")
cliente.show()
