from pathlib import Path
import importlib.metadata, json
from dataweave import DataWeave
with DataWeave() as engine:
    result = engine.run(Path(__file__).with_name('hello.dwl').read_text(encoding='utf-8'), raise_on_error=True)
    assert result.success and result.mime_type == 'application/json', repr(result)
    text = result.get_string()
    assert json.loads(text) == {'greeting': 'Hello, World!'}, text
    print(text)
    print('DataWeave native '+importlib.metadata.version('dataweave-native')+' execution PASS.')
