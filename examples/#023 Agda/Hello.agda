module Hello where

open import Agda.Builtin.IO using (IO)
open import Agda.Builtin.Unit using (⊤)
open import Agda.Builtin.String using (String)

postulate
  putLine : String → IO ⊤

{-# FOREIGN GHC import qualified Data.Text as Text #-}
{-# COMPILE GHC putLine = putStrLn . Text.unpack #-}

main : IO ⊤
main = putLine "Hello, World!"
