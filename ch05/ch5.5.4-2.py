def another_palindrome(word):
	return word == word[::-1]
print(another_palindrome('radar'))
print(another_palindrome('halibut'))
