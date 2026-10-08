from pathlib import Path
import sys
import numpy as np

# Select one explicit fixed-width record layout for Linguist's broad Formatted
# data category. Parsing is delegated to NumPy's existing fixed-width reader.
record = np.genfromtxt(Path(sys.argv[1]), delimiter=(3, 13, 4),
                      dtype=[('id', 'i4'), ('greeting', 'U13'), ('length', 'i4')],
                      encoding='utf-8', comments=None, autostrip=False)
assert record.shape == ()
assert record['id'].item() == 1
assert record['greeting'].item() == 'Hello, World!'
assert record['length'].item() == len(record['greeting'].item()) == 13
print(record['greeting'].item())
print('PASS: existing NumPy fixed-width record reader; declared I3/A13/I4 layout')
