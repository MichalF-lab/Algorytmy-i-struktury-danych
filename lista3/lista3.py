import random
import numpy
import time

# Przygotowanie tablic do testów

main_table = numpy.arange(random.randint(5,7))

for item in main_table:
    main_table[item] = float(random.randint(1,100))

#main_table = [37,18,45,50,28,80]


def quicksort(tab):

    if (len(tab) <= 1 ): return tab
    
    a = tab[-1]
    ltab, rtab = [], []

    for item in tab[:-1]:
        if (item <= a): ltab.append(item)
        if (item > a): rtab.append(item)

    ltab = quicksort(ltab)
    rtab = quicksort(rtab)

    ext = []
    if ltab:
        ext.extend(ltab)
    ext.append(a)
    if rtab:
        ext.extend(rtab)
        
    return ext
    

def heapsort(tab):

    if (len(tab) <= 1 ): return tab

    def sort_the_heap(heap,root,lenght):
        left = 2 * root + 1
        if left > lenght : return heap
        right = 2 * root + 2

        if heap[left] > heap[root]:
            heap[left], heap[root] = heap[root], heap[left]
        
        if right > lenght : return heap

        if heap[right] > heap[root] and heap[right] > heap[left]:
            heap[right], heap[root] = heap[root], heap[right] 



    def sort_whole_heap(tab,N):
        for i in range(N, -1, -1):
            sort_the_heap(tab, i, N)

    for i in range(len(tab)-1, 0, -1):
        sort_whole_heap(tab, i)
        tab[i], tab[0] = tab[0], tab[i]

    return tab



if __name__ == '__main__':
    a = 10
    # print(main_table)
    # print(quicksort(main_table))
    print(main_table)
    # print(heapsort(main_table))
    print(quicksort(main_table) == heapsort(main_table))
