# high order functions

## 개념
- 커링이랑 여러개의 인자를 받는 함수를 단일 인자를 받는 함수 여러개로 변환하는 것

## 코드
```hs
let divideByTen = (`div` 10)
divideByTen 23
-- 2

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

applyTwice (+3) 10
applyTwice (++ "Haha") "Sunman"
applyTwice (3:) [1]

zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith _ [] _ = []
zipWith _ _ [] = []
zipWith f (a:ar) (b:br) = f a b : zipWith f ar br

map :: (a -> b) -> [a]-> [b]
map _ [] = []
map f (x:xr) = f x: map f xr

filter :: (a -> Boolean) -> [a] -> [a]
filter _ [] = []
filter f (x:xr) =
    | p x = x: filter f xr
    | otherwise = filter f xr

--lambda
map (\x -> x + 3) [1,2,3]
-- [4,5,6]
map (\x -> x `mod` 3 == 0 || x `mod` 5 == 0) [1,2,3,4,5,6,7,8,9]
-- [3,5,6,9]

-- fold
sum' :: (Num a) => [a] -> a
sum' xs = foldl (\acc x -> acc + x) 0  xs

elem' :: (Eq a) => a -> [a] -> Bool
elem' x xs = foldl (\acc y -> if x == y then True else acc) False xs

product' xs = foldl (*) 1 xs

-- $
-- 아무 일도 하지 않음
-- 다만 우측 결합이여서 오른쪽 식을 먼저 계산하고 그 결과를 왼쪽에 적용시킴
-- 괄호의 남발을 줄여줌
($) :: (a -> b) -> a -> b
f $ x = f x
map ($3) [(4+), (10*), (^2)] -- 이렇게 쓸 수도 있다.
sum (map (+3) [1..100])
sum $ map (+3) [1..100]

-- . 은 함수 합성에 쓰임
(.) || (b -> c) -> (a ->b) -> a -> c
f . g = \x -> f (g x)
allNegate xs = map (\x -> negate (abs x)) xs
allNegate xs = map (negate . abs) xs
```