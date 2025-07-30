from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Sample JSON data (e.g., API response)
response_data = {
    "id": 101,
    "name": "John Doe",
    "email": "john@example.com",
    "active": True
}

# JSON Schema to validate against
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "active": {"type": "boolean"}
    },
    "required": ["id", "name", "email", "active"]
}

# Validate
try:
    validate(instance=response_data, schema=schema)
    print("✅ JSON is valid.")
except ValidationError as e:
    print("❌ JSON is invalid.")
    print("Error:", e.message)
