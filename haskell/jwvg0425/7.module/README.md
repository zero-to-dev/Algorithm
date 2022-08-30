# Module

```hs
-- import (module name)
import Data.List -- nub은 리스트에서 중복되는 요소는 하나로 합쳐줌
numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

import Data.List (nub, sort) -- 특정 몇 개만 가져올 때
import Data.List hiding (nub) -- 특정 몇 개만 제외할 때

-- 이름 충돌이 일어날 떼

import qualified Data.List

numUniques :: (Eq a) => [a] -> Int
numUniques = length . Data.List.nub

-- 이름 충돌에 별칭으로 대응하기 

import qualified Data.List as L

numUniques :: (Eq a) => [a] -> Int
numUniques = length . L.nub

-- 자주 쓰이는 모듈들
-- Data.List: 리스트와 관련한 함수, sort, group, find, nub
-- Data.Char: 문자 처리와 관련한 함수
-- Data.Map: key-value쌍 자료구조

-- 모듈 만들기!! 모듈 이름은 파일 이름과 동일해야함!

-- Test.hs
module Test where

foo = "foo"
bar = "bar"

-- Test.hs, foo만 내보내기
module Test (foo) where

foo = "foo"
bar = "bar"

-- 서브모듈 만들기

-- Test.hs - foo 만 외부에서 사용 가능
module Test where
import Test.Foo

-- Test 폴더의 Foo.hs 파일
module Test.Foo (foo) where
foo = "foo"
```