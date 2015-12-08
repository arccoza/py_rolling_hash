from pprint import pprint
from six.moves import range
from collections import deque


class Rabin_Fingerprint(object):
	def __init__(self, size, seed=None):
		self.size = size
		self.window = deque(maxlen=size)
		self.hash = None
		self.seed = seed or 101#10007
		self._maxfact = self.seed**(self.size-1) #store the prime ^ size-1 value, so we don't have to calc it everytime.

	def calc(self, window, seed):
		w = window
		n= len(window)
		p = seed
		h = 0

		for i in range(0, n):
			try:
				v = ord(w[i])
			except TypeError as ex:
				v = w[i]
			h += (p**(n-i-1))*(v)
			# print(p**(n-i-1), v)
		# print(h)
		return h

	def feed(self, items):
		s = self.size
		n = None
		w = self.window
		p = self.seed
		ps = self._maxfact
		h = 0
		for i, v in enumerate(items):
			n = s - 1 - len(w)
			n = n if n > 0 else 0
			try:
				v = ord(v)
			except TypeError as ex:
				pass
			if len(w) == s:
				h = ((h - (w[0] * ps)) * p) + v
				w.append(v)
			else:
				h += (p**n) * v
				w.append(v)
		# pprint(h)
		# pprint(w)
		self.hash = h

	def __str__(self):
		return str(self.hash)

	def __len__(self):
		return len(self.window)


if __name__ == '__main__':
	f = Rabin_Fingerprint(3)
	# f.calc('bra', 101)
	f.feed('abra')
	pprint(len(f))