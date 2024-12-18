import System.IO
import Control.Monad

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    
    -- Auto-generated code below aims at helping you parse
    -- the standard input according to the problem statement.
    
    input_line <- getLine
    let surfacen = read input_line :: Int -- the number of points used to draw the surface of Mars.
    
    replicateM surfacen $ do
        input_line <- getLine
        let input = words input_line
        let landx = read (input!!0) :: Int -- X coordinate of a surface point. (0 to 6999)
        let landy = read (input!!1) :: Int -- Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        return ()
    
    -- game loop
    forever $ do
        input_line <- getLine
        let input = words input_line
        let x = read (input!!0) :: Int
        let y = read (input!!1) :: Int
        let hspeed = read (input!!2) :: Int -- the horizontal speed (in m/s), can be negative.
        let vspeed = read (input!!3) :: Int -- the vertical speed (in m/s), can be negative.
        let fuel = read (input!!4) :: Int -- the quantity of remaining fuel in liters.
        let rotate = read (input!!5) :: Int -- the rotation angle in degrees (-90 to 90).
        let power = read (input!!6) :: Int -- the thrust power (0 to 4).
        
        -- hPutStrLn stderr "Debug messages..."
        
        -- 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
        if (vspeed > -39) then
            putStrLn "0 0"
        else
            putStrLn "0 4"
