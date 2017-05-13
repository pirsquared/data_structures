    min_heap = Heap('min')
    max_heap = Heap('max')

    min_heap.insert(in09[0])
    size = 1
    print(min_heap.extreme * 1.)
    for x in in09[1:3]:
        if x >= min_heap.extreme:
            min_heap.insert(x)
        else:
            max_heap.insert(x)
        while min_heap.size - max_heap.size > 1:
            max_heap.insert(min_heap.pop_extreme())
        while max_heap.size - min_heap.size > 1:
            min_heap.insert(max_heap.pop_extreme())

        size += 1
        if size % 2 == 0:
            print((max_heap.extreme + min_heap.extreme) / 2)
        else:
            if min_heap.size > max_heap.size:
                print(min_heap.extreme * 1.)
            else:
                print(max_heap.extreme * 1.)
