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

      return 2 + bunnyEars(bunnies-1) O(n)
      overall 
      this is recursive with a comparison operator. if it was was a normal for loop it would be O(n). Even though it is recursive I still think it is O(n) because there is no huge growth when n or bunnies grows so it may be O(2n) as compared to a normal for loop of O(n) but O(2n) simplifies to O(n)

## Exercise II


