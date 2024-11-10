def all_variants(text: str):
    l = len(text)
    for j in range(1, l + 1):
        for i in range(l - j + 1):
            yield text[i:i + j]

a = all_variants("abc")
for i in a:
    print(i)
