# CLAUDE.md

## Project Overview

A Python utility package providing reusable string and math helper functions.

## Repository Structure

```
src/
├── __init__.py
└── utils/
    ├── __init__.py
    ├── string_utils.py   # String manipulation helpers
    └── math_utils.py     # Math operation helpers
```

## Conventions

- **Type hints** on all function signatures.
- **Google-style docstrings** with `Args`, `Returns`, and `Raises` sections.
- All public functions are exported via `src/utils/__init__.py`.
- Use `ValueError` for invalid input (e.g., division by zero, negative factorial input).

## Running

No external dependencies. Run from the repo root with `PYTHONPATH=src`:

```bash
PYTHONPATH=src python -c "from utils import add; print(add(1, 2))"
```

## Pending Work

The following functions are marked as TODO and need to be implemented. Follow the existing conventions (type hints, docstrings, export in `__init__.py`).

| Function | File | Requirements |
|---|---|---|
| `is_palindrome(text: str) -> bool` | `src/utils/string_utils.py` | Case-insensitive, ignores spaces |
| `factorial(n: int) -> int` | `src/utils/math_utils.py` | Raise `ValueError` for negative input |
| `is_prime(n: int) -> bool` | `src/utils/math_utils.py` | Numbers < 2 are not prime |

## Notes for AI Assistants

- Match the existing docstring style exactly (Google-style with typed Args/Returns).
- Add new exports to `src/utils/__init__.py` when adding new functions.
- No test suite exists yet; consider adding one in a `tests/` directory if asked.
- No dependency manager or `pyproject.toml` is present; keep the project dependency-free unless explicitly asked to add one.
