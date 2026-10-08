(deffacts greeting-input
  (greeting "Hello, World!"))

(defrule say-greeting
  ?fact <- (greeting ?text)
  =>
  (printout t ?text crlf)
  (retract ?fact))
