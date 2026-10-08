from pathlib import Path
import yaml
from openapi_spec_validator import validate
value = yaml.safe_load(Path("hello.yaml").read_text(encoding="utf-8"))
validate(value)
response = value["paths"]["/hello"]["get"]["responses"]["200"]["content"]["text/plain"]
assert response["schema"] == {"type": "string"}
assert response["example"] == "Hello, World!"
print(response["example"])
