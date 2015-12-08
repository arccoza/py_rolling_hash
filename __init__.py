from pprint import pprint
from six.moves import range
from collections import deque


class Rabin_Fingerprint(object):
	def __init__(self, size, base=None):
		self.size = size
		self.window = deque(maxlen=size)
		self.hash = None
		self.base = base or 101#10007
		self._maxfact = self.base**(self.size-1) #store the prime ^ size-1 value, so we don't have to calc it everytime.

	@staticmethod
	def calc(window, base=None):
		w = window
		n= len(window)
		p = base or 101
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
		p = self.base
		ps = self._maxfact
		h = 0

		# if isinstance(items, str):
		# 	items = [ord(v) for v in items]

		for i, v in enumerate(items):
			l = len(w)
			n = s - 1 - l
			n = n if n > 0 else 0
			try:
				v = ord(v)
			except TypeError as ex:
				pass
			if l == s:
				h = ((h - (w[0] * ps)) * p) + v
				w.append(v)
			else:
				h += (p**n) * v
				w.append(v)
		# pprint(h)
		# pprint(w)
		self.hash = h
		return h

	def __str__(self):
		return str(self.hash)

	def __len__(self):
		return len(self.window)



if __name__ == '__main__':
	f = Rabin_Fingerprint(3)
	Rabin_Fingerprint.calc('bra', 101)
	f.feed('abra')
	pprint(len(f))