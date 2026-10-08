From Coq Require Import String.
Open Scope string_scope.

Definition greeting : string := "Hello, " ++ "World!".
Example greeting_value : greeting = "Hello, World!".
Proof. reflexivity. Qed.
Compute greeting.
