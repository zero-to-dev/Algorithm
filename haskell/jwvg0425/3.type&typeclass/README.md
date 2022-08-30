# Concept

- 타입은 표현식 뒤에 :: 기호오 함께 표기됨
- Type 종류
 1. Int: -2147483648 ~ 2147483647
 2. Integer: 범위에 제한이 없음
 3. Float
 4. Double: Float 보다 더 정밀한 부동 소수점
 5. Bool
 6. Char: ' 홑따옴표로 감싼 하나의 문자 형태
 7. Tuple

# Type Variable
- 제네릭과 비슷한 개념
- `function :: [certainType] -> certainType`
- `function :: [certainType1, certainType2] -> certainType1`

# Type Class 
- 타 언어의 class와는 아무 관련이 없다
- 오히려 인터페이스의 개념에 가깝다
- ```hs
    Prelude > :t (==)
    (==) :: Eq a => a -> a -> Bool
    -- '=>' 앞의 것은 클래스 제약(class constraint)라고 부름
    -- 위에서는 타입 변수 a가 타입클래스 Eq에 속하는 경우에만 '==' 함수를 쓸 수 있다는 뜻
  ```
- 종류
  1. Eq
    - 서로 같은지 다른지 판별할 수 있는 타입
    - '==' 나 '/=' 함수와 사용할 수 있음
  2. Ord
    - 순서를 가진 타입
    - '>', '>=', 'compare' 등의 함수를 제공
    - Ord에 속하면 Eq에도 속해야함
  3. Show
    - 문자열로 변환할 수 있는 타입
    - 'show' 등의 함수 제공
  4. Read
    - Show와 반대되는 타입 클래스
    - 문자열로부터 해당 타입의 값을 만들 수 있음
    - 'read' 함수를 제공
    - ```hs
        read "4" + 5
        -- 9
        read "3" :: Int
        -- 3
        read "[1,2,3,4]" :: Int
        -- [1,2,3,4]
      ```
  5. Enum
    - 열거될 수 있는 타입들을 위한 타입 클래스
    - 'pred', 'succ' 함수 제공 (이전 값과 다음 값을 가져오는 함수)
    - list range를 사용할 수 있음
    - ```hs
        succ 'B'
        -- 'C'
      ```
  6. Bounded
    - 상한선과 하한선을 갖는 타입
    - ```hs
        minBound :: Int
        -- -2147483648
        maxBound :: True
        -- True
      ```
  7. Num
    - 숫자처럼 동작
  8. Integral
  9. Floating
  10. fromIntegral
    - (Integral b, Num a) => a -> b