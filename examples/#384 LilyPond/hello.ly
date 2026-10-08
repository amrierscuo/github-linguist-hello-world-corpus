\version "2.24.3"
\header { title = "Hello, World!" composer = "Corpus Example" }
\paper { tagline = ##f }
\score {
  \new Staff \relative c' { \time 4/4 c4 d e c }
  \layout { }
}
