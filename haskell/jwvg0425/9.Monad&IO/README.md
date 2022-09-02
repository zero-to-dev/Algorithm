# Monad&IO

## 개념
- Monad는 Applicative Functor에서 한 발 더 나아간 개념

```hs
(>>=):: (Monad m) => m a -> (a -> m b) -> m b
-- ">>=" we call it "bind"
```

## Monad의 함수
- return
  - Applicative Functor의 pure와 같은 역할
  - 어떤 값이 주어져있을 때 이 값을 해당 context 속으로 집어넣는 역할
  - 명령형 언어에서의 return과는 전혀 다른 의미
- >>=
  - 앞에서 설명한 bind 함수
  - Monad의 동작에서 핵심적인 역할
- >>
  - 지금은 크게 신경쓸 필요 없음
  - 이후 뒤에서 다시 설명
- fail
  - 직접 사용하는 함수가 아님
  - Monad 연산에서 뭔가 문제가 생겼을 때 컴파일러가 사용

```hs
instance Monad Maybe where
  return x = Just x
  Nothing >>= f = Nothing
  Just x >>= f = f x
  fail _ = Nothing

return "WHAT" :: Maybe String
-- Just "WHAT"
Just 9 >>= \x -> return (x*10)
-- Just 90
Nothing >>= \x -> return (x*10)
-- Nothing

square :: Integer -> Maybe Integer
square n
    | 0 <= n = Just (n * n)
    | otherwise = Nothing

squareRoot :: Integer -> Maybe Integer
squareRoot n
    | 0 <= n = squareRoot' 1
    | otherwise = Nothing
    where squareRoot' x
        | n > x * x = squareRoot' (x+1)
        | n < x * x = Nothing
        | otherwise = Just x

squareSumRoot :: Integer -> Integer -> Maybe Integer
-- 예외처리가 많은 명령형 언어 방식의 정의
-- squareSumRoot a b = case square a of
--                         Nothing -> Nothing
--                         Just as -> case square b of
--                                     Nothing -> Nothing
--                                     Just bs -> squareRoote (as + bs)
-- do를 쓰지 않은 정의
-- squareSumRoot a b = square a >>= (\as ->
--                     square b >>= (\bs ->
--                     squareRoot (as + bs)))
squareSumRoot a b = do
        as <- square a
        bs <- square b
        squareRoot (as + bs)

-- do e1
--    e2
-- 는 e1 >> e2와 동일

-- do p <- e1
--    e2
-- 는
-- e1 >>= (\v -> case v of p -> e2
--                         _ -> fail "s")와 동일

instance Monad [] where
    return x = [x]
    xs >>= f = concat (map f xs)
    fail _ = []

[3,4,5] >>= \x -> [x, -x]
-- [3,-3,4,-4,5,-5]
[1,2] >>= \n -> ['a','b'] >>= \ch -> return (n, ch)
-- [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

listOfTuples = do
    n <- [1,2]
    let chs = ['a','b']
    ch <- chs
    return (n, ch)

listOfTuples' = [ (n, ch) | n <- [1,2], ch <- ['a','b']]

-- Monad가 지켜야 하는 규칙 (==는 -이 위아래로 세 개 있는 모양을 대신함)
-- 1. Left Identity
-- return a >>= g == fa
-- 2. Right Identity
-- m >>= return == m
-- 3. Associativity
-- (m >>= f) >>= g == m >>= (\x -> f x >>= g)

main :: IO()
main = do
    putStrLn "Hello, World!"

main = do 
    str <- getLine
    putStrLn str
```