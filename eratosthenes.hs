
sieve :: Int -> [Int]
sieve limit = eratosthenes [2 .. limit]
  where
    eratosthenes (p:xs) = p : eratosthenes [x | x <- xs, x `mod` p /= 0]
    eratosthenes [] = []

primesUpTo100 = sieve 100
print primesUpTo100 