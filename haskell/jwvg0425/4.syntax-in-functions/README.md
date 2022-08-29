# Syntax in functions

## 개념

- 어떤 데이터가 가져야 할 패턴을 명시

```hs
-- 1
f :: (Integral a, Num b) => 1 -> b
f 0 = 0
f 1 = 1
f n = f(n-1) + f(n - 2)

-- 2
addVector :: (Num a) => (a, a) -> (a, a) -> (a,a)
-- addVector a b = (fst a + fst b, snd a + snd b)
addVector (a1, b1) (a2, b2) = (a1 + a2, b1 + b2)

-- 3
first :: (a, b, c) -> a
first (x, _, _) = x

second :: (a, b, c) -> a
second (_, y, _) = y

-- 4
pairToNum :: (Num a) => [(a, a)] -> [a]
pariToNum xs = [ a + b | (a, b) <-xs ]

-- 5 
head' :: [a] -> a
head' [] = error "Can't call head on empty list."
head' (x:_) = x

-- 6
length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

-- 7
sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

-- 8
headFirst :: (Show a) => [a] -> String
headFirst [] = "empty string"
headFirst all@(x:_) = show all ++ "'s first element is " ++ show x
```

## Guard

- 가드는 데이터가 특정 조건을 만족하는 지를 판단하는 방법
- 여러 개의 if ~else if 가 나열되어 있는 구조와 비슷한 형태

```hs
bmiTell :: (Floating a) => a -> String
bmiTell bmi
    | bmi <= 18.5 = "You are underweight"
    | bmi <= 25.0 = "You are normal"
    | bmi <= 30.0 = "You are fat"
    | otherwise = "you are very fat"
```

## Where

```hs
bmiTell :: (Floating a) => a -> a -> String
bmiTell weight height
    | bmi <= 18.5 = "You are underweight"
    | bmi <= 25.0 = "You are normal"
    | bmi <= 30.0 = "You are fat"
    | otherwise = "you are very fat"
    where bmi = weight / height ^ 2

bmiTell :: (Floating a) => a -> a -> String
bmiTell weight height
    | bmi <= skinny = "You are underweight"
    | bmi <= normal = "You are normal"
    | bmi <= fat = "You are fat"
    | otherwise = "you are very fat"
    where bmi = weight / height ^ 2
          (skinny, normal, fat) = (18.5, 25.0, 30.0)

calcFibos :: (Integral a) => [a] -> a
calcFibos xs = [fibo x | x <- xs]
    where fibo 0 = 0
          fibo 1 = 1
          fibo n = fibo (n - 1) + fibo (n - 2)
```

## let in

```hs
cylinder :: (Num a) => a -> a -> a
cylinder r h =
    let sideArea = 2 * pi * r * h
        topArea = pi * r^2
    in sideArea + 2 * topArea

[f x | x <- [0..10], let f 0 = 0; f 1 = 1; f n = f (n-1) + f (n-2)]
```

## case expression

```hs
case expression of pattern -> result
                of pattern -> result
                of pattern -> result
                ...

head' :: [a] -> a
head' xs = case xs of [] -> error "Can't call head on empty list."
                      (x:_) -> x

descList :: [a] -> String
descList xs = "this List is " ++ case xs of [] -> "Empty List"
                                            [x] -> "Singleton List"
                                            xs -> "Long List"
```