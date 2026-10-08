\documentclass{article}
\begin{document}
Questo programma letterato usa il tipo Main della libreria standard Agda.
\begin{code}
module Hello where
open import IO using (Main; run; putStrLn)

main : Main
main = run (putStrLn "Hello, World!")
\end{code}
\end{document}
