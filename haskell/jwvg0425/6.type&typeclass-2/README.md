# type & typeclass 2

```hs
data Bool = False | True

data Shape = Circle Float Float Float
            | Rectangle Float Float Float Float deriving (Show)

-- :t Circle
-- Circle :: Float -> Float -> Float -> Shape

-- deriving Show를 붙이면 Show 타입 클래스를 자동으로 상속받게 됨
-- 내가 직접 만든 데이터 타입을 결과 창에 띄우려면 deriving Show를 써줘야함

map (Circle 10 20) [4,5,6,6]

-- data Person = Person String String Int String deriving (Show)

-- firstname ( Person firstname _ _ _) = firstname
-- 위와 같은 함수를 매번 만드는 건 인력 낭비가 심하다
-- 그래서 나온 Record Syntax

data Person = Person { firstname :: String
                    , lastname :: String
                    , age :: Int
                    , address :: String} deriving (Show)

let nam = Person "nam" "hyeonuk" 21 "blahblah"
age nam
--21

data Circle = Circle { origin :: (Int, Int)
                    , radius :: Int } deriving (Show)

let c = Circle { radius = 5, origin = (0,0)}
origin c

-- Type parameter
data Maybe a = Nothing | Just a

-- Type synonyms
-- type 키워드로 내부적으로는 완전히 동일하나 이름만 서로 다른 데이터 타입을 만들어 낼 수 있다.
-- 둘은 호환도 된다.
-- 이를 쓰는 이유는 가독성 때문이다.
-- String과 [Char]를 예로 들 수 있다.

-- Derived instances
-- driving (Eq, Show) 등을 이용해 필요한 행동을 구현하게 해줌

-- typeClass
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)

-- 특정 타입이 어떤 타입 클래스의 인스턴스가 되도록 정의하는 방법
data TrafficLight = Red | Yellow | Green

instance Eq TrafficLight where
    Red == Red = True
    Green == Green = True
    Yellow == Yellow = True
    _ == _ = False

-- sub typeclass
class (Eq a) => Ord a where
    compare :: a -> a -> Ording
    -- 그 아래 자세한 구현은 생략

class (Eq m) => Eq (Maybe m) where
    Just x == Just y = x == y
    Nothing == Nothing = True
    _ == _ = False
```