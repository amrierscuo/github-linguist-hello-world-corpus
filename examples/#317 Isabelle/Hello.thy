theory Hello
  imports Main
begin

definition greeting :: string where
  "greeting = ''Hello, World!''"

lemma greeting_correct: "greeting = ''Hello, World!''"
  by (simp add: greeting_def)

value greeting

end
