import time

test_patterns = ["random_chars", "first_missed", "last_missed", "either_missed", "failure"]
search_lengths =[10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
query_lengths = [10, 100, 1000, 10000]

def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256    
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

def to_KM(num: int) -> str:
    if num < 1000:
        return str(num)
    num //= 1000
    if num < 1000:
        return str(num) + "K"
    num //= 1000
    return str(num) + "M"

def execute_and_time(test_pattern: str, search_length: int, query_length: int):
    if test_pattern == "failure":
        filename = "test_data/failure/" + str(search_length) + ".txt"
    else:
        filename = "test_data/" + test_pattern + "/" + str(search_length) + "-" + str(query_length) + ".txt"
    s_f = open(filename, "r")
    s = s_f.read()
    s_f.close()
    query_name = "test_data/queries/" + str(query_length) + ".txt"
    q_f = open(query_name, "r")
    q = q_f.read()
    q_f.close()
    start = time.time()
    ## Change to the implemented function
    res = bm_match(s, q)
    end = time.time()
    print(f'(\"{test_pattern}\", {search_length}, {query_length}): {res},')
    return end - start

if __name__ == "__main__":
    total_time = 0
    for cnt, test_pattern in enumerate(test_patterns):
        case_total_time = 0
        for search_length in search_lengths:
            for query_length in query_lengths:
                case_total_time += execute_and_time(test_pattern, search_length, query_length)
        total_time += case_total_time


