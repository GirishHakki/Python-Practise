from collections import Counter
def max_occurrence(s):
    counter = Counter(s)
    max_count = max(counter.values())
    max_chars = [char for char, count in counter.items() if count == max_count]
    return max_chars

string = "Hello, World!"
print("Maximum occurring character(s) in the string:", max_occurrence(string))