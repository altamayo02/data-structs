import random

def random_alphanumerical(length: int) -> str:
	string = ""
	for _ in range(length):
		string += chr(random.randint(ord("A"), ord("z")))
	return string