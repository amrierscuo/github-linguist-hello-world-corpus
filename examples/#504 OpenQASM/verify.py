from pathlib import Path
from qiskit import qasm2
from qiskit_aer import AerSimulator
circuit = qasm2.loads(Path("hello.qasm").read_text(encoding="utf-8"))
assert circuit.num_qubits == circuit.num_clbits == 104
result = AerSimulator(method="stabilizer").run(circuit, shots=1, memory=True).result()
assert result.success
bits = result.get_memory()[0].replace(" ", "")[::-1]
text = bytes(int(bits[i:i+8][::-1], 2) for i in range(0,104,8)).decode("ascii")
assert text == "Hello, World!"
print(text)
