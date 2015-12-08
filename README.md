# py_rolling_hash
Rabin fingerprint rolling hash.

## API
#### Rabin_Fingerprint(size[, seed])
Creates a new object, with a window size `size`, which you can feed values.

`size` - Length of the window for the rolling hash (number of bytes/chars).
`seed` - Prime number used as the base in the hash calculation (optional).

#### Rabin_Fingerprint.feed(items)
Calculates the hash in a rolling manner, when the window is full value are removed from the end and 
added at to the beginning.

`items` - An iterable collection of values to add to the hash, can be a string or list of values.
When the window is full, ie. you've added as many items as `size`, the function will start rolling.

#### Rabin_Fingerprint.hash

`hash` - The value of the hash, calculated from `feed`.

#### Rabin_Fingerprint.calc(window[, seed])
Calculates a hash value from a window once off, no rolling/feeding possible.

`window` - A list, string or other iterable to calculate the hash.

`seed` - The prime number base for the calculation (optional).

##Use
```py
f = Rabin_Fingerprint(3)
f.feed('abr')
print(f.hash)
# 999509
```
