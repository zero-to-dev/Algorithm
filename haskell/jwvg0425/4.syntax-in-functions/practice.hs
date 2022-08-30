yesNo :: Bool -> String
yesNo True = "Yes"
yesNo False = "No"

trueman :: [Bool] -> Int
trueman [] = 0
trueman (True:xs) = 1 + trueman xs
trueman (_:xs) = trueman xs

listToPairs :: (Num a) => [a] -> [(a,a)]
listToPairs [] = []
listToPairs [a] = []
listToPairs (a:b:xs) = (a,b):listToPairs xs

maximumm :: [Int] -> Int
maximumm [] = error "you cannot run this on empty list"
maximumm [x] = x
maximumm (x:xs)
    | x <= max = max
    | otherwise = x
    where max = maximumm xs

take' :: Int -> [Int] -> [Int]
take' n _ | n <= 0 = []
take' _ [] = []
take' a (x:xs) = x:take' (a-1) xs

zipp :: [Int] -> [Int] -> [(Int, Int)]
zipp [] _ = []
zipp _ [] = []
zipp (x:xs) (y:ys) = (x,y):zipp xs ys

-- 맨 앞을 pivot으로
quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort [a] = [a]
quicksort (a:xs) =
    let b = [x | x<-xs, x <= a]
        c = [x | x<-xs, x > a]
    in quicksort b ++ [a] ++ quicksort c