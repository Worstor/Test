# CLAUDE.md - AI Assistant Guidelines for Test Repository

This document provides essential context and guidelines for AI assistants working with this codebase.

## Project Overview

This is a **Python utility library** providing reusable helper functions for mathematical operations and string manipulation. The project is in early development with a clean, modular structure designed for expansion.

## Repository Structure

```
/home/user/Test/
├── CLAUDE.md              # AI assistant guidelines (this file)
├── .gitignore             # Git ignore patterns
└── src/                   # Main source package
    ├── __init__.py        # Package initialization
    └── utils/             # Utility modules
        ├── __init__.py    # Exports all utility functions
        ├── math_utils.py  # Mathematical operations
        └── string_utils.py # String manipulation functions
```

## Technology Stack

- **Language**: Python 3.x (vanilla, no external dependencies)
- **Type System**: PEP 484 type hints throughout
- **Documentation**: Google-style docstrings

## Code Conventions

### Style Guidelines

1. **Naming**: Use `snake_case` for functions, variables, and modules
2. **Type Hints**: All functions must include type annotations for parameters and return values
3. **Docstrings**: Use Google-style format with Args, Returns, and Raises sections

### Example Function Pattern

```python
def function_name(param: str, count: int) -> str:
    """Brief description of what the function does.

    Args:
        param: Description of the parameter.
        count: Description of the count parameter.

    Returns:
        Description of the return value.

    Raises:
        ValueError: When the input is invalid.
    """
    # Implementation
    return result
```

### Error Handling

- Validate inputs explicitly where necessary
- Raise `ValueError` with descriptive messages for invalid input
- Example: Division by zero check in `divide()` function

## Available Modules

### Math Utilities (`src/utils/math_utils.py`)

| Function | Signature | Description |
|----------|-----------|-------------|
| `add` | `(a: float, b: float) -> float` | Add two numbers |
| `subtract` | `(a: float, b: float) -> float` | Subtract b from a |
| `multiply` | `(a: float, b: float) -> float` | Multiply two numbers |
| `divide` | `(a: float, b: float) -> float` | Divide a by b (raises ValueError if b=0) |

### String Utilities (`src/utils/string_utils.py`)

| Function | Signature | Description |
|----------|-----------|-------------|
| `capitalize_words` | `(text: str) -> str` | Capitalize each word |
| `reverse_string` | `(text: str) -> str` | Reverse a string |
| `count_vowels` | `(text: str) -> int` | Count vowels (case-insensitive) |
| `truncate` | `(text: str, max_length: int) -> str` | Truncate with "..." suffix |

## Importing Functions

```python
# Import specific functions
from src.utils import add, multiply, capitalize_words

# Or import all from a module
from src.utils.math_utils import add, subtract, multiply, divide
from src.utils.string_utils import capitalize_words, reverse_string
```

## Development Workflow

### Running Python Code

```bash
# Execute from repository root
python -c "from src.utils import add; print(add(2, 3))"

# Interactive testing
python
>>> from src.utils import capitalize_words
>>> capitalize_words("hello world")
'Hello World'
```

### Git Workflow

```bash
# Check status
git status

# Stage changes
git add <file>

# Commit with descriptive message
git commit -m "Add/Fix/Update: brief description"

# Push to feature branch
git push -u origin <branch-name>
```

## Planned Features (TODOs)

The following features are marked for implementation:

### Math Utilities
- [ ] `factorial(n: int) -> int` - Calculate factorial of a number
- [ ] `is_prime(n: int) -> bool` - Check if a number is prime

### String Utilities
- [ ] `is_palindrome(text: str) -> bool` - Check if a string is a palindrome

## Testing

> **Note**: No test infrastructure is currently configured. When adding tests:
> - Use `pytest` as the testing framework
> - Place tests in a `tests/` directory at the repository root
> - Name test files as `test_<module>.py`
> - Follow the `test_<function_name>` naming convention for test functions

## Configuration Files

### .gitignore

The project ignores:
- `__pycache__/` - Python cache directories
- `*.pyc` - Compiled Python bytecode
- `*.pyo` - Optimized Python bytecode

## Best Practices for AI Assistants

1. **Read before modifying**: Always read a file before making changes
2. **Follow existing patterns**: Match the style of surrounding code
3. **Include type hints**: All new functions must have type annotations
4. **Document with docstrings**: Use Google-style format consistently
5. **Keep it simple**: This is a utility library - functions should be focused and reusable
6. **Validate inputs**: Add appropriate error handling for edge cases
7. **Update exports**: When adding new functions, update `src/utils/__init__.py`

## Quick Reference

| Task | Command/Action |
|------|----------------|
| Run Python | `python -c "..."` or `python` for REPL |
| Check syntax | `python -m py_compile src/utils/<file>.py` |
| View structure | `find . -type f -name "*.py"` |
| Git status | `git status` |
