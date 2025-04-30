import System.IO
import Control.Monad
import Data.List (sort)
import Control.Monad (replicateM)

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    
    -- Read number of elements
    nStr <- getLine
    let n = read nStr :: Int

    -- Read n integers into a list
    nums <- replicateM n (fmap read getLine :: IO Int)

    -- Sort the list
    let sorted = sort nums

    -- Compute minimum difference between adjacent elements
    -- Zips the sorted with the sorted minus the first elements with minus operator - then find minimum.
    let diffs = zipWith (-) (tail sorted) sorted
        minDiff = minimum diffs

    -- Print the result
    print minDiff

    return ()
