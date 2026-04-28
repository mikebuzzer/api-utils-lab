<div align="center">
  
# API Utils Lab
A lightweight Python library for working with APIs, including request handling, validation, and utility helpers.

</div>

---

## Features

- Simple GET and POST request helpers
- JSON response handling
- Error handling for failed requests
- Retry mechanism for unstable APIs
- Timeout and headers support
- URL validation utilities
- Response time measurement

---

## Installation

```bash
pip install -e .
````

---

## Usage

### GET request

```python
from api_utils.client import get_json

data = get_json("https://api.github.com")
print(data)
```

---

### POST request

```python
from api_utils.client import post_json

payload = {"name": "test"}
response = post_json("https://api.example.com/items", payload)
print(response)
```

---

### Headers support

```python
headers = {"Authorization": "Bearer TOKEN"}

data = get_json("https://api.example.com/data", headers=headers)
```

---

### Timeout & retry

```python
data = get_json(
    "https://api.example.com/data",
    timeout=5,
    retries=3
)
```

---

### Validator utilities

```python
from api_utils.validator import is_success_status, is_valid_url

print(is_success_status(200))  # True
print(is_valid_url("https://example.com"))  # True
```

---

### Utility helpers

```python
from api_utils.utils import current_timestamp_ms, response_time_ms

start = current_timestamp_ms()
end = current_timestamp_ms()

print(response_time_ms(start, end))
```

---

## Error Handling

If a request fails, the helper functions return:

```text
None
```

This prevents crashes and allows safer handling of API failures.

---

## Running Tests

```bash
pytest
```

---

## Project Structure

```
api-utils-lab/
├── src/api_utils/
│         ├──__init__.py
│         ├── client.py
│         ├── validator.py
│         └── utils.py
├── tests/
│      ├── test_utils.py
│      └── test_validator.py
├── README.md
└── pyproject.toml
```
