module Example.Calculator exposing (..)

addition : Float -> Float -> Float
addition first second =
    first + second

subtraction : Float -> Float -> Float
subtraction first second =
    first - second

multiplication : Float -> Float -> Float
multiplication first second =
    first * second

division : Float -> Float -> Maybe Float
division first second =
    if second == 0 then
        Nothing
    else
        Just (first / second)