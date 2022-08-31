applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

-- applyTwice (+3) 10
-- applyTwice (++ "Haha") "Sunman"
-- applyTwice (3:) [1]

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (a:ar) (b:br) = f a b : zipWith' f ar br
