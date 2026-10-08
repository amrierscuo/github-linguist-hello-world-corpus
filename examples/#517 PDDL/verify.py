from pyperplan.planner import search_plan
from pyperplan.search import breadth_first_search
plan = search_plan("hello.pddl", "problem.pddl", breadth_first_search, None)
assert plan is not None and len(plan) == 1
assert plan[0].name == "(greet hello-world)"
print("Hello, World!")
