# 왜 함수형 프로그래밍이 중요한가 — John Hughes 1989

- 나중에 다시 읽어야지
- [한글 링크](https://medium.com/@jooyunghan/%EC%99%9C-%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4-%EC%A4%91%EC%9A%94%ED%95%9C%EA%B0%80-john-hughes-1989-f6a1074a055b#.3x63auh15)
- [본문 링크](http://worrydream.com/refs/Hughes-WhyFunctionalProgrammingMatters.pdf)

## 요약
- 고차 함수 (higher-order function)과 지연 연산(lazy evaluation)이 모듈화 수준을 매우 높여준다.
- 예제로 알파-베타 휴리스틱(게임에 사용되는 인공지능의 한 알고리즘)을 구현한다.

## 함수 결합하기

- `listof * ::= Nil | Cons * (listof *)`
- ```
  sum Nil = 0
  sum (Cons n list) = n + sum list
  ```
- `sum = foldr (+) 0` 모든 원소의 합 구하기
- ```
  (foldr f x) Nil = x
  (foldr f x) (Cons a l) = f a ((foldr f x) l)
  ```
- `product = foldr (*) 1` 모든 원소의 곱 구하기
- `anytrue = foldr (⋁) False` 불 값의 리스트에 참 값이 있는지
- `alltrue = foldr (⋀) True` 불 값의 리스트의 모든 값이 참인지
- (foldr f a)는 Cons를 f로 Nil을 a로 치환하는 것과 같다
  - `Cons 1 (Cons 2 (Cons 3 Nil))` 여기에 (foldr (+) 0)을 취하면
  - `(+) 1 ((+) 2 ((+) 3 0)) = 6` 이런식으로 바꿀 수 있다
  - (foldr Cons Nil)은 리스트를 단순히 복사
  - `append a b = foldr Cons b a` 리스트 두 개를 붙이는 것
  - ```
    // 리스트 개수를 세는 것
    length = foldr count 0
    count a n = n + 1
    ```
  - ```
    // 모든 리스트의 요소에 2를 곱하는 함수
    doubleall = foldr doubleandcons Nil
    doubleandcons n list = Cons (2 * n) list
    ```