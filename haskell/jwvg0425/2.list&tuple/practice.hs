-- list 
lastButOne x = if (length x > 1) then x !! (length x - 2) else -999
_lastButOne x = last (init x)
notCapital x = [y | y <- x, y `notElem` ['A'..'Z']]
diff x y = [z|z<-x, z `notElem` y]

-- tuple & list
swap x = [(y,z) | (z,y) <- x]
_sum x = if length x == 1 then head x else head x + _sum (tail x)
divisors x = [y | y <- [1..x], x `mod` y == 0]