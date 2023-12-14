def rabin_karp_search(haystack, needle):
    if not haystack or not needle:
        return []

    prime = 22
    mod = 10**9 + 9

    def calculate_hash(string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * prime + ord(char)) % mod
        return hash_value

    needle_hash = calculate_hash(needle)
    needle_length = len(needle)

    haystack_hash = calculate_hash(haystack[:needle_length])

    occurrences = []

    for i in range(len(haystack) - needle_length + 1):
        if haystack_hash == needle_hash and haystack[i:i + needle_length] == needle:
            occurrences.append(i)

        if i < len(haystack) - needle_length:
            haystack_hash = (haystack_hash * prime + ord(haystack[i + needle_length]) - ord(haystack[i]) * (prime ** needle_length)) % mod

    return occurrences

haystack = "ababcababcabcabc"
needle = "abc"
result = rabin_karp_search(haystack, needle)
print(f"Індекси входжень: {result}")
