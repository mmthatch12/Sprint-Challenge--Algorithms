#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0 O(1) the input is constant
    while (a < n * n * n): O(n)
      a = a + n * n O(1)
      overall O(n)


b) sum = 0 O(1)
    for i in range(n): O(n)
      j = 1 O(1)
      while j < n: O(1)
        j *= 2 O(1)
        sum += 1 O(1)
        overall O(n)


c) def bunnyEars(bunnies):
      if bunnies == 0: O(1)
        return 0 O(1)

      return 2 + bunnyEars(bunnies-1) 
      overall 
      this is recursive with a comparison operator O(n^2)

## Exercise II


