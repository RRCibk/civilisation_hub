# Civilisation Hub

[![CI](https://github.com/rafalchalupka/civilisation_hub/actions/workflows/ci.yml/badge.svg)](https://github.com/rafalchalupka/civilisation_hub/actions/workflows/ci.yml)

A knowledge management system built on the principle of META 50/50 Equilibrium.

## Overview

Civilisation Hub is a comprehensive knowledge domain system that maintains perfect balance across all components. The system is built on a fundamental principle:

**META 50/50**: Every system, every domain, every concept maintains balance between opposing forces.

### Core Principles

- **META Level (50/50)**: Absolute balance - the fundamental principle
- **Operational Level (52/48)**: Structure/flexibility ratio that enables META balance
- **PI/6 Connection**: Mathematical derivation where PI/6 ≈ 0.5236 yields 52%, and sin(PI/6) = 0.5 connects to META

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd civilisation_hub

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Show system status
python main.py --status

# Show META proof
python main.py --prove

# Run full demonstration
python main.py --demo

# Show specific domain details
python main.py --domain mathematics

# Save domains to database
python main.py --save

# List saved domains
python main.py --list-saved
```

## Features

### Knowledge Domains

Five integrated knowledge domains, each with balanced dualities:

| Domain | Duality | Description |
|--------|---------|-------------|
| **Mathematics** | Abstract / Concrete | Numbers, structures, patterns |
| **Physics** | Energy / Matter | Physical laws and phenomena |
| **Code** | Abstraction / Implementation | Software development principles |
| **Biology** | Life / Death | Living systems and processes |
| **Philosophy** | Being / Non-Being | Fundamental questions of existence |

### System Components

- **Core Equilibrium** - META 50/50 verification and Atom wave states
- **Proportions** - PI/6 calculations and ratio validation
- **Evolution Tracking** - Phase transitions and progress monitoring
- **Participation** - Engagement tracking with give/receive balance
- **Verification** - Claim validation and proof chains
- **Output** - Multiple formatters (text, JSON, markdown, table)
- **Database Persistence** - SQLite storage with META compliance validation

## Architecture

```
civilisation_hub/
├── core/                    # Core equilibrium and proportions
├── models/                  # Domain model definitions
├── knowledge/domains/       # Knowledge domain implementations
├── evolution/              # Evolution tracking
├── participation/          # Participation tracking
├── verification/           # Verification system
├── output/                 # Output formatting
├── database/               # Database persistence (SQLAlchemy)
├── data/                   # SQLite database storage
├── tests/                  # Comprehensive test suite
└── main.py                 # Entry point
```

## Usage Examples

### Check META Balance

```python
from core.equilibrium import MetaEquilibrium

meta = MetaEquilibrium()

# Verify balance
is_balanced = MetaEquilibrium.verify_balance(50, 50)  # True
is_balanced = MetaEquilibrium.verify_balance(60, 40)  # False

# Calculate balance ratio
ratio = MetaEquilibrium.calculate_balance(50, 50)  # (50.0, 50.0)
```

### Work with Domains

```python
from knowledge.domains.mathematics import create_mathematics_domain

# Create domain with shared equilibrium
domain = create_mathematics_domain()

# Check balance
is_valid = domain.validate_balance()  # True

# Get statistics
stats = domain.get_domain_stats()
print(f"Concepts: {stats['concepts']}")

# Prove META meaning
proof = domain.prove_meta_meaning()
print(proof['proof'])
```

### Generate Reports

```python
from output.display import ConsoleDisplay
from output.reporters import DomainReporter

display = ConsoleDisplay()
reporter = DomainReporter(display)

report = reporter.generate_report(domain)
reporter.render_report(report)
```

### Persist Domains to Database

```python
from database.persistence import DomainPersistenceService
from knowledge.domains.mathematics import create_mathematics_domain

# Create service and domain
service = DomainPersistenceService()
domain = create_mathematics_domain()

# Save domain with all concepts
service.save_domain(domain)

# Load domain data
data = service.load_domain("Mathematics")
print(f"Concepts: {data['concept_count']}")

# List all saved domains
for d in service.list_domains():
    print(f"{d['name']}: {d['concept_count']} concepts")

# Get persistence statistics
stats = service.get_persistence_stats()
print(f"META compliance: {stats['compliance_rate']}%")
```

## Testing

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest tests/test_equilibrium.py -v

# Run with coverage (requires pytest-cov)
python -m pytest --cov=. --cov-report=term-missing
```

Current test count: **592 tests**

## The META 50/50 Principle

The entire system is built on a fundamental truth: balance exists at the core of all phenomena.

### Mathematical Foundation

- PI/6 ≈ 0.5236 (radians)
- This yields approximately 52% (operational structure)
- sin(PI/6) = 0.5 exactly (connects to META 50/50)

### Domain Dualities

Each domain maintains balanced opposition:
- Positive pole: 50%
- Negative pole: 50%
- Total: 100%

This isn't arbitrary - it reflects the fundamental nature of complementary forces.

## Output Sample

```
══════════════════════
META 50/50 EQUILIBRIUM
══════════════════════
META Balance: [█████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░] (50.0% / 50.0%)
The fundamental principle of perfect balance:

  Positive: 50%  ←→  Negative: 50%

  All systems derive from this balance.
  OPERATIONAL 52/48 enables META 50/50.

═════════════
System Status
═════════════
Version: 1.0.0
META Balanced: Yes
Domains: 5
Total Concepts: 278
System Valid: Yes

Domains
───────
  ✓ mathematics: 33 concepts
  ✓ physics: 50 concepts
  ✓ code: 64 concepts
  ✓ biology: 54 concepts
  ✓ philosophy: 77 concepts
```

## Development

See [CLAUDE.md](CLAUDE.md) for detailed development guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
