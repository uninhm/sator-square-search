def binary_search(lst, prefix): # a.k.a. lower bound
    low = 0
    high = len(lst) - 1
    while low <= high-1:
        mid = (low + high) // 2
        if lst[mid] > prefix:
            high = mid
        elif lst[mid] < prefix:
            low = mid + 1
        else:
            return mid
    return low

def double_search(lst, prefix, suffix):
    # Search for all words that start with prefix and end with suffix in an ordered list
    idx = binary_search(lst, prefix)
    while idx < len(lst) and lst[idx].startswith(prefix):
        if lst[idx].endswith(suffix):
            yield lst[idx]
        idx += 1


with open('words.txt', 'r') as f:
    words = [
        l.strip()
         .replace('á', 'a')
         .replace('é', 'e')
         .replace('í', 'i')
         .replace('ó', 'o')
         .replace('ú', 'u')
         .replace('ñ', 'n')
        for l in f.readlines()]
    words2 = []
    # Filter words that have meaning when reversed and remove duplicates
    for word in words:
        rev = word[::-1]
        idx2 = binary_search(words, rev)
        if words[idx2] == rev and words[-1] != word:
            words2.append(word)
    words = words2

for word1 in double_search(words, '', ''):
    for word2 in double_search(words, word1[1], word1[3]):
        for word3 in double_search(words, word1[2]+word2[2], word2[2]+word1[2]):
            print(word1)
            print(word2)
            print(word3)
            print(word2[::-1])
            print(word1[::-1])
            print()
