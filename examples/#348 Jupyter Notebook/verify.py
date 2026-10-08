from pathlib import Path
import nbformat,sys
from nbclient import NotebookClient
source = Path(sys.argv[1]); notebook=nbformat.read(source, as_version=4)
nbformat.validate(notebook)
client=NotebookClient(notebook, timeout=60, kernel_name='python3', allow_errors=False)
client.execute(cwd=str(Path(sys.argv[2]).resolve()))
code=[cell for cell in notebook.cells if cell.cell_type=='code']
assert len(code)==1 and code[0].execution_count==1
outputs=code[0].outputs
assert len(outputs)==1 and outputs[0].output_type=='stream' and outputs[0].name=='stdout'
assert outputs[0].text=='Hello, World!\n'
nbformat.validate(notebook)
nbformat.write(notebook, Path(sys.argv[2])/'executed.ipynb')
print(outputs[0].text, end='')
print('PASS: native nbformat validation and actual Jupyter kernel execution')
