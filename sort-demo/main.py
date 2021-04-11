from sort import SortImpl, Sorts

def main():

    sort_impl_obj = SortImpl(Sorts.quick_sort) 
    
    sort_impl_obj.sort_impl()

if __name__ == '__main__':
    main()