# Contributing to Civilisation Hub

Thank you for your interest in contributing to Civilisation Hub! This document provides guidelines for contributing to the project.

## Core Principle: META 50/50 Equilibrium

All contributions must respect the fundamental META 50/50 equilibrium principle:

- **META Level (50/50)**: Absolute balance between opposing forces
- **Operational Level (52/48)**: Structure/flexibility ratio that enables META balance
- **Every duality must be balanced**: No exceptions at the META level

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/RRCibk/civilisation_hub.git
   cd civilisation_hub
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

5. Verify setup:
   ```bash
   pytest
   ```

## Development Workflow

### Before Making Changes

1. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Ensure tests pass before starting:
   ```bash
   pytest
   ```

### Making Changes

1. Write code following the project style (enforced by ruff)
2. Add tests for new functionality
3. Ensure META 50/50 compliance for any new dualities
4. Run the full test suite:
   ```bash
   pytest
   ```

5. Run linting and type checking:
   ```bash
   ruff check .
   ruff format .
   mypy .
   ```

   Or use pre-commit to run all checks:
   ```bash
   pre-commit run --all-files
   ```

### Submitting Changes

1. Commit your changes with a clear message:
   ```bash
   git commit -m "Add feature: description of changes"
   ```

2. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Open a Pull Request against `main`

4. Fill out the PR template completely

5. Wait for CI checks to pass and address any feedback

## Code Style

### Python Style

- Follow PEP 8 (enforced by ruff)
- Line length: 100 characters
- Use type hints for function signatures
- Write docstrings for public functions and classes

### Import Order

Imports are sorted automatically by ruff:
1. Standard library
2. Third-party packages
3. First-party modules (core, models, knowledge, etc.)

### Naming Conventions

- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_equilibrium.py -v

# Run specific test
pytest tests/test_equilibrium.py::TestMetaEquilibrium::test_verify_balance -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names that explain what is being tested
- Test both success and failure cases
- Test META compliance for new features

Example:
```python
def test_domain_maintains_meta_balance():
    """Verify domain duality is balanced at 50/50."""
    domain = create_mathematics_domain()
    assert domain.validate_balance()

    duality = domain.duality
    assert duality.positive_weight == 50.0
    assert duality.negative_weight == 50.0
```

## Adding New Features

### Adding a New Knowledge Domain

1. Create a new file in `knowledge/domains/`
2. Inherit from `KnowledgeDomain`
3. Implement required methods:
   - `_initialize_duality()` - Must be 50/50 balanced
   - `_initialize_axioms()` - Foundational concepts
   - `get_fundamental_concepts()` - Key concepts list
4. Add factory function `create_*_domain()`
5. Add comprehensive tests
6. Register in `main.py` if appropriate

### Adding New Validators

1. Inherit from `Validator` in `verification/validators.py`
2. Implement `validate()` method
3. Ensure META compliance validation
4. Add tests

## META 50/50 Compliance Checklist

Before submitting, verify:

- [ ] All new dualities have 50/50 balance
- [ ] `validate_balance()` returns True for new domains
- [ ] No hardcoded imbalanced values
- [ ] Tests verify META compliance
- [ ] Documentation mentions balance requirements

## Pull Request Requirements

PRs must:

1. Pass all CI checks (lint, test, type-check)
2. Include tests for new functionality
3. Maintain or improve code coverage
4. Follow the PR template
5. Have a clear description of changes

## Reporting Issues

- Use the bug report template for bugs
- Use the feature request template for enhancements
- Include META impact assessment
- Provide reproducible examples when possible

## Questions?

- Check the [README](README.md) for usage information
- Review [CLAUDE.md](CLAUDE.md) for detailed architecture
- Open an issue for questions not covered in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
