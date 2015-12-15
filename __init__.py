from pprint import pprint
from six.moves import range
from collections import deque
# from numba import jit
# import numpy


fn = lambda h, w, ps, p, v: ((h - (w[0] * ps)) * p) + v

class RabinFingerprint(object):
	def __init__(self, size, base=None):
		self.size = size
		self.window = deque(maxlen=size)
		self.cur = len(self.window)
		self.hash = None
		self.base = base or 101#10007
		self._maxfact = self.base**(self.size-1) #store the prime ^ size-1 value, so we don't have to calc it everytime.

	@staticmethod
	def calc(window, base=None):
		w = window
		n = len(window)
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
		
	def feed(self, items, is_str=False):
		s = self.size
		n = None
		w = self.window
		l = self.cur
		p = self.base
		ps = self._maxfact
		h = 0
		# is_str = isinstance(items, str)

		# if isinstance(items, str):
		# 	items = [ord(v) for v in items]

		# for i, v in enumerate(items):
		for v in items:
			# l = len(w)
			# print(l, i)
			n = s - 1 - l
			n = n if n > 0 else 0
			# try:
			# 	v = ord(v)
			# except TypeError as ex:
			# 	pass
			if is_str:
				v = ord(v)
			if l == s:
				h = ((h - (w[0] * ps)) * p) + v
				# h = fn(h, w, ps, p, v)
				w.append(v)
			else:
				h += (p**n) * v
				# h += numpy.multiply(numpy.power(p,n), v)
				w.append(v)
				l += 1
		# pprint(h)
		# pprint(w)
		self.cur = l
		self.hash = h
		return h

	def __str__(self):
		return str(self.hash)

	def __len__(self):
		return len(self.window)


class RsyncChecksum(object):
	def __init__(self, size, base=None):
		self.size = size
		self.window = deque(maxlen=size)
		self.cur = len(self.window)
		# self.hashA = 0
		self.ihash = 0 # Interim hash (A).
		self.hash = 0 # Final hash (B).

	@staticmethod
	def calc(window):
		w = window
		n = len(window)
		a = 0
		b = 0

		for i in range(0, n):
			try:
				v = ord(w[i])
			except TypeError as ex:
				v = w[i]
			a += v
			b += a
		# print(b)
		return b
		
	def feed(self, items, is_str=False):
		s = self.size
		w = self.window
		l = self.cur
		a = self.ihash
		b = self.hash

		for v in items:
			if is_str:
				v = ord(v)
			if l == s:
				# a -= w[0]
				# a += v
				a = a - w[0] + v
				# b -= s * w[0]
				# b += a
				b = b - (s * w[0]) + a
				w.append(v)
			else:
				a += v
				b += a
				w.append(v)
				l += 1
		# pprint(b)
		# pprint(w)
		self.cur = l
		self.ihash = a
		self.hash = b
		# self.hash = b
		return b

	def __str__(self):
		return str(self.hash)

	def __len__(self):
		return len(self.window)



if __name__ == '__main__':
	# f = RabinFingerprint(3)
	# RabinFingerprint.calc('bra', 101)
	# f.feed('abr', is_str=True)
	# pprint(len(f))
	f = RsyncChecksum(3)
	RsyncChecksum.calc('bra')
	f.feed('abra', is_str=True)
	# pprint(len(f))