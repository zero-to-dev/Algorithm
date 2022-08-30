_even x = if (mod x 2) == 0
_factorial x = if x == 1 then 1 else x * (_factorial (x-1))
-- using product & list(see study 2)
_factorial n = product [1..n]