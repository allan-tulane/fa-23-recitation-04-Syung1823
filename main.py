import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    else:
        pivot = pivot_fn(a)
        great = []
        less =[]
        for i in a:
            if i > pivot:
                great.append(i)
            else:
                less.append(i)

    return qsort(less, pivot_fn) + [pivot] + qsort(great, pivot_fn)
    
    
def qsort_fixed(a):
    
    return (a.pop((len(a)//2)))

def qsort_rand(a):
    return a.pop(random.randrange(0,len(a)))

def qsort_first(a):
    return a.pop(0)

def selection_sort(a):
    if len(a) > 10000:
        return a
    for i in range(len(a)):
        m = a.index(min(a[i:]))
        a[i], a[m] = a[m], a[i]  

    return a


def time_search(sort_fn, mylist, pivot_fn = None):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    if pivot_fn == None:
        sort_fn(mylist)
    else:
        sort_fn(mylist, pivot_fn)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort
    qsort_random_pivot = qsort
    qsort_first_pivot = qsort
    timsort= sorted
    ssort = selection_sort
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist, qsort_fixed),
            time_search(qsort_random_pivot, mylist, qsort_rand),
            time_search(ssort, mylist),
            time_search(timsort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot','selection sort', 'timsort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()

