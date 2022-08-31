# functor

## 개념
- Functor 타입 클래스는 context에 대해 함수를 적용할 수 있는 타입들의 집합
- Functor 타입 클래스는 다음 하나의 함수 인터페이스만을 갖고 있음

```hs
class Functor f where
    fmap :: (a -> b) -> f a -> f b
```

- Maybe 타입에 대한 Functor는 다음과 같이 정의

```hs
instance Functor Maybe where
    fmap _ Nothing = Nothing
    fmap f (Just a) = Just (f a)

threeRepeat :: (Functor f) => f a -> f [a]
threeRepeat = fmap (replicate 3)

threeRepeat [1,2,3,4]
-- [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
threeRepeat (Just 3)
Just [3,3,3]
```

- Functor 타입 클래스에 속하는 타입들이 만족해야 하는 규칙
  1. fmap id = id
  2. fmap (f.g) = fmap f . fmap g

# Applicative Functor

```hs
fmap (*) (Just 3)
-- Just (*3)

class (Functor f) => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b

instance Applicative Maybe where
    pure = Just
    Nothing <*> _ = Nothing
    (Just f) <*> something = fmap f something

Just (+3) <*> Just 9
-- Just 12
pure (+3) <*> Just 10
-- Just 13
Just (++"hahaha") <*> Nothing
-- Nothing
Nothing <*> Just "Test"
-- Nothing

pure (+) <*> Just 3 <*> Just 5
-- Just 8
pure (+) <*> Just 3 <*> Nothing
-- Nothing
pure (+) <*> Nothing <*> Just 5
-- Nothing

(<$>) :: (Functor f) => (a -> b) -> f a -> f b
f <$> x = fmap f x

-- pure f <*> x <*> y <*> ...
-- f <$> x <*> y <*> ..

-- List 역시 Applicative Functor

instance Applicative [] where
    pure x = [x]
    fs <*> xs = [f x | f <- fs, x <- xs]

[(*0), (+100), (^2)] <*> [1,2,3]
-- [0,0,0,101,102,103,1,4,9]
[(+), (*)] <*> [1,2] <*> [3,4]
-- [4,5,5,6,3,4,6,8]
(++) <$> ["ha","heh","hmm"] <*> ["?", "!", "."]
-- ["ha?","ha!","ha.","heh?","heh!","heh.","hmm?","hmm!","hmm."]
(++) <$> (Just "ha") <*> (Just "!")
Just "ha!"

-- Applicative Functor가 지켜야하는 규칙

1. pure id <*> v = v
2. pure (.) <*> u <*> v <*> w = u <*> (v <*> w)
3. pure f <*> pure x = pure (f x)
4. u <*> pure y = pure ($ y) <*> u
```