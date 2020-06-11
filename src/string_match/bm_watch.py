def bm_match(txt: str, pat: str) -> int:
    # skip = [len(pat)] * 256

    skip = [None] * 256
    for pt in range(256):
        skip[pt] = len(pat)
    
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    for i in range(ord('Z') - ord('A') + 1):
        item = skip[i + ord('A')]
        print(f"{chr(ord('A') + i)}: {item}")

bm_match("ABCXDEZCABACABAC", "ABAC")
