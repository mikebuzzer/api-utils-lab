# api-utils-lab

A lightweight Python utility package for simple API workflows.

## Features

- Simple GET requests
- JSON response parsing
- Basic status code checking
- URL validation helper

## Installation

```bash
pip install -e .
```

## Usage

```python
from api_utils.client import get_json
from api_utils.validator import is_success_status

data = get_json("https://api.example.com/data")
print(data)

print(is_success_status(200))
```

## Development

Run tests:

```bash
pytest
```

## License

MIT
