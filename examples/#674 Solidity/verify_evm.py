import json,sys
from pathlib import Path
from eth_tester import EthereumTester, PyEVMBackend
from eth_utils import keccak
from eth_abi import decode
compiled=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
chain=EthereumTester(PyEVMBackend())
account=chain.get_accounts()[0]
tx=chain.send_transaction({'from':account,'gas':3000000,'data':'0x'+compiled['evm']['bytecode']['object']})
receipt=chain.get_transaction_receipt(tx)
assert receipt['status']==1 and receipt['contract_address']
result=chain.call({'from':account,'to':receipt['contract_address'],'gas':3000000,'data':'0x'+keccak(text='greeting()')[:4].hex()})
value=decode(['string'],bytes.fromhex(result[2:]))[0]
assert value=='Hello, World!'
print(value)
