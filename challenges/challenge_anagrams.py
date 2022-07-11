def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    quick_sort(first_list, 0, len(first_list) - 1)
    quick_sort(second_list, 0, len(second_list) - 1)
    if(first_list == second_list):
        return True
    return False


def quick_sort(list, start, end):
    if start < end:
        p = partition(list, start, end)
        quick_sort(list, p + 1, end)
        quick_sort(list, start, p - 1)


def partition(list, start, end):
    pivot = list[end]
    d = start - 1
    for i in range(start, end):
        if list[i] <= pivot:
            d = d + 1
            list[i], list[d] = list[d], list[i]
    list[d + 1], list[end] = list[end], list[d + 1]
    return d + 1
