(define (domain greeting)
  (:requirements :strips :typing)
  (:types recipient)
  (:predicates (greeted ?person - recipient))
  (:action greet
    :parameters (?person - recipient)
    :precondition (and)
    :effect (greeted ?person)))
