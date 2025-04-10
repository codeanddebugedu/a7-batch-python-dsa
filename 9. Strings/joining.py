# Join (list -> str)

words = ["python", "is", "a", "good", "language", "and", "we", "are", "doing", "DSA"]

# ans = " ".join(words)
ans = " ".join(w + "z" for w in words)
print(ans)
