from pathlib import Path
import sys
import pyomo.environ as pyo

codes=list(b'Hello, World!')
model=pyo.ConcreteModel(name='CorpusGreeting')
model.i=pyo.RangeSet(0,len(codes)-1)
model.character=pyo.Var(model.i,bounds=(0,127))
model.encoding=pyo.Constraint(model.i,rule=lambda m,i:m.character[i]==codes[i])
model.objective=pyo.Objective(expr=sum(model.character[i] for i in model.i))
model.write(str(Path(sys.argv[1])),format='nl',io_options={'symbolic_solver_labels':False})
print('PASS: native Pyomo NL writer; 13 ASCII-valued variables/equalities')
