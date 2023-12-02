def nth_most_rate_signature(lst, n):
    unique_list = list(set(lst))
    sorted_list = sorted(unique_list)
    ans = print(sorted_list[n - 1])
    return ans
