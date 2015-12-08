from __init__ import Rabin_Fingerprint
import timeit


f = Rabin_Fingerprint(3)
f.feed('abr')
def speed_test():
	f.feed('a')

if __name__ == '__main__':
	print(timeit.timeit(stmt='speed_test()', setup='from __main__ import speed_test', number=10000000))