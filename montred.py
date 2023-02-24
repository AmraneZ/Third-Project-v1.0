
import math

class Montgomery:
	
	def __init__(self, mod):
		# verfier le modulus
		if int(mod) < 3 or int(mod) % 2 == 0:
			raise ValueError("Le modulus doit etre impaire et plus grand que trois")
		self.modulus = int(mod)
		
		# intructions pour la reduction
		self.reducerbits = (int(mod).bit_length() // 8 + 1) * 8 
		self.reducer = 1 << self.reducerbits  
		self.mask = self.reducer - 1
		assert self.reducer > int(mod) and math.gcd(self.reducer, int(mod)) == 1
		
	
		self.reciprocal = Montgomery.reciprocal_mod(self.reducer % int(mod), int(mod))
		self.factor = (self.reducer * self.reciprocal - 1) // int(mod)
		self.convertedone = self.reducer % int(mod)
	
	
	# transformer x sous forme de montgomery
	def convert_in(self, x):
		return (int(x) << self.reducerbits) % self.modulus
	
	
	# Retransfomer x sous la forme standard 
	def convert_out(self, x):
		return (int(x) * self.reciprocal) % self.modulus
	
	
	# x , y et le resultat retouné sont sous la forme montgomery
	def multiply(self, x, y):
		mod = self.modulus
		assert 0 <= x < int(mod) and 0 <= y < int(mod)
		product = x * y
		temp = ((product & self.mask) * self.factor) & self.mask
		reduced = (product + temp * int(mod)) >> self.reducerbits
		result = reduced if (reduced < int(mod)) else (reduced - int(mod))
		assert 0 <= result < int(mod)
		return result
	
	
	
	# x et le resultat de la puissance sont sous la forme montgomery 
	def pow(self, x, y):
		assert 0 <= x < self.modulus
		if y < 0:
			raise ValueError("la puissance est negative ! ")
		z = self.convertedone
		while y != 0:
			if y & 1 != 0:
				z = self.multiply(z, x)
			x = self.multiply(x, x)
			y >>= 1
		return z
	@staticmethod
	def reciprocal_mod(x, mod):
		 #calculé à partir d'une simplification de l'algorithme d'euclide
		assert int(mod) > 0 and 0 <= x < int(mod)
		y = x
		x = int(mod)
		a = 0
		b = 1
		while y != 0:
			a, b = b, a - x // y * b
			x, y = y, x % y
		if x == 1:
			return a % int(mod)
		else:
			raise ValueError("la reciproque n'existe pas")
