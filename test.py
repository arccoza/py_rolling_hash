from __init__ import RabinFingerprint, RsyncChecksum
import timeit
import cProfile, pstats, StringIO


pr = cProfile.Profile()

rf = RabinFingerprint(3)
# rf.feed('abr', is_str=True)
rf.feed([97, 98, 114])
def rabin_test():
	# rf.feed('a', is_str=True)
	rf.feed([97])
	# ord('a')

rc = RsyncChecksum(3)
# rc.feed('abr', is_str=True)
rc.feed([97, 98, 114])
def rsync_test():
	# rc.feed('a', is_str=True)
	rc.feed([97])

if __name__ == '__main__':
	# pr.enable()
	# print(timeit.timeit(stmt='rabin_test()', setup='from __main__ import rabin_test', number=1000000))
	# pr.disable()
	# s = StringIO.StringIO()
	# sortby = 'cumulative'
	# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
	# ps.print_stats()
	# print s.getvalue()
	# cProfile.run('rabin_test()')
	# print(timeit.timeit('"h = (((999509 - (97 * 10201)) * 101) + 97)"', number=10000000))

	pr.enable()
	print(timeit.timeit(stmt='rsync_test()', setup='from __main__ import rsync_test', number=1000000))
	pr.disable()
	s = StringIO.StringIO()
	sortby = 'cumulative'
	ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
	ps.print_stats()
	print s.getvalue()