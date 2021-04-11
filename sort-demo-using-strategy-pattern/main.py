from sortImpl.merge_sort import MergeSortStategy
from doSort import DoSort


def main():
    merge_sort_strategy = MergeSortStategy()
    do_sort = DoSort(merge_sort_strategy)
    do_sort.do_sort()
    

if __name__ == '__main__':
    main()