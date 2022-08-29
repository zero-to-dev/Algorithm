inverse xs = map (1/) xs

longList xs = filter ((>= 3).length) xs

dot xs ys = zipWith (\(x1,y1) (x2,y2) -> x1*x2 + y1*y2) xs ys

finalPosition (x1, y1) = foldl (\(x2, y2) (x3, y3) -> (x2+x3, y2 + y3) ) (x1, y1)

nineDigit :: (Integral a, Show a, Integral b) => a -> b
nineDigit = fromIntegral . length . filter (=='9') . show