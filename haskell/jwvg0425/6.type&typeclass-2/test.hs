data Bool = False | True

-- data Shape = Circle Float Float Float
--             | Rectangle Float Float Float Float deriving (Show)

-- :t Circle
-- Circle :: Float -> Float -> Float -> Shape

-- deriving Show를 붙이면 Show 타입 클래스를 자동으로 상속받게 됨
-- 내가 직접 만든 데이터 타입을 결과 창에 띄우려면 deriving Show를 써줘야함

-- map (Circle 10 20) [4,5,6,6]

-- data Person = Person String String Int String deriving (Show)

-- firstname ( Person firstname _ _ _) = firstname
-- 위와 같은 함수를 매번 만드는 건 인력 낭비가 심하다
-- 그래서 나온 Record Syntax

data Person = Person { firstname :: String
                     , lastname :: String
                     , age :: Int
                     , address :: String} deriving (Show)

-- let nam = Person "nam" "hyeonuk" 21 "blahblah"

data Circle = Circle { origin :: (Int, Int)
                    , radius :: Int } deriving (Show)

-- let c = Circle { radius = 5, origin = (0,0)}
-- origin c