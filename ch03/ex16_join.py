# p83

marxes = ["Groucho", "Chico", "Harpo"]
print(", ".join(marxes))

friends = ["Harry", "Hermione", "Ron"]
separator = " * "
joined = separator.join(friends)
print(joined)

separated = joined.split(separator)
print(separated)
print(separated == friends)
