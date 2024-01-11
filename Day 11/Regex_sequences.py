import re

# Sample string
text = "Hello 123 world! This is an example."

# Using \A: Matches the start of the string
result_a = re.search(r'\AHello', text)
print(result_a.group() if result_a else "Not found")

# Using \b: Matches a word boundary
result_b = re.search(r'\b123\b', text)
print(result_b.group() if result_b else "Not found")

# Using \B: Matches a non-word boundary
result_c = re.search(r'\B123\B', text)
print(result_c.group() if result_c else "Not found")

# Using \d: Matches any digit (equivalent to [0-9])
result_d = re.search(r'\d', text)
print(result_d.group() if result_d else "Not found")

# Using \D: Matches any non-digit
result_e = re.search(r'\D', text)
print(result_e.group() if result_e else "Not found")

# Using \s: Matches any whitespace character
result_f = re.search(r'\s', text)
print(result_f.group() if result_f else "Not found")

# Using \S: Matches any non-whitespace character
result_g = re.search(r'\S', text)
print(result_g.group() if result_g else "Not found")

# Using \w: Matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
result_h = re.search(r'\w', text)
print(result_h.group() if result_h else "Not found")

# Using \W: Matches any non-alphanumeric character
result_i = re.search(r'\W', text)
print(result_i.group() if result_i else "Not found")

# Using \Z: Matches the end of the string
result_j = re.search(r'example\Z', text)
print(result_j.group() if result_j else "Not found")