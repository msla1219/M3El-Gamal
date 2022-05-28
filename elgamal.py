import random

from params import p
from params import g

def keygen():
	sk = random.randint(1, p)
	pk = pow(g, sk, p)

	return pk,sk

def encrypt(pk,m):

	# To encrypt m, generate a random r in the range 1≤r≤q,
	q = (p-1)/2
	r = random.randint(1,q)

	c1 = pow(g, r, p)
	c2 = m * pow(pk, r, p) % p

	return [c1,c2]


def decrypt(sk,c):

	m = (c[1] * pow(c[0], p - 1 - sk, p)) % p

	return m
