import time
from header_data import TEST_PATTERNS, SEARCH_LENGTHS, QUERY_LENGTHS, EXPECTED_RESULT 

def bm_match(txt: str, pat: str) -> int:
    skip = [len(pat)] * 256

    for i, c in enumerate(pat):
        skip[ord(c)] = len(pat) - i - 1

    pt = len(pat) - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp <= 0:
                return pt
            pt -= 1
            pp -= 1
        if skip[ord(txt[pt])] < len(pat) - pp:
            pt += len(pat) - pp
        else:
            pt += skip[ord(txt[pt])]
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
    if res == EXPECTED_RESULT[(test_pattern, search_length, query_length)]:
        trial = "success"
    else:
        trial = 'failed (expected: {:' '>8}'.format(EXPECTED_RESULT[(test_pattern, search_length, query_length)])
        trial += '; result: {:' '>8})'.format(res)
    print(f'{str(end - start)[:16]} s; result: {trial} ', end='')
    print('(N: {:' '>4}, '.format(to_KM(search_length)), end='')
    print('M: {:' '>5})'.format(query_length))
    return end - start

if __name__ == "__main__":
    total_time = 0
    for cnt, test_pattern in enumerate(TEST_PATTERNS):
        case_total_time = 0
        print(f'Test Case {cnt + 1}: {test_pattern}')
        for search_length in SEARCH_LENGTHS:
            for query_length in QUERY_LENGTHS:
                case_total_time += execute_and_time(test_pattern, search_length, query_length)
        print(f'Test Case Total Time: {case_total_time} s')
        total_time += case_total_time
        print()
    print(f'Total Time: {total_time} s')
