headFirst :: (Show a) => [a] -> String
headFirst [] = "empty string"
headFirst all@(x:_) = show all ++ "'s first element is " ++ show x

bmiTell :: Float -> String
bmiTell bmi
    | bmi <= 18.5 = "You are underweight"
    | bmi <= 25.0 = "You are normal"
    | bmi <= 30.0 = "You are fat"
    | otherwise = "you are very fat"

bmiTell' :: Float -> Float -> String
bmiTell' weight height
    | bmi <= 18.5 = "You are underweight"
    | bmi <= 25.0 = "You are normal"
    | bmi <= 30.0 = "You are fat"
    | otherwise = "you are very fat"
    where bmi = weight / height ^ 2

cylinder :: Float -> Float -> Float
cylinder r h =
    let sideArea = 2 * 3.14 * r * h
        topArea = 3.14 * r^2
    in sideArea + 2 * topArea

head' :: [a] -> a
head' xs = case xs of [] -> error "Can't call head on empty list."
                      (x:_) -> x

descList :: [a] -> String
descList xs = "this List is " ++ case xs of [] -> "Empty List"
                                            [x] -> "Singleton List"
                                            xs -> "Long List"
