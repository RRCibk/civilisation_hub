# Civilisation Hub - AI Assistant Guide

## Core Principle: META 50/50 Equilibrium

This project is built on a fundamental principle of balance:

- **META Level (50/50)**: Absolute balance between opposing forces
- **OPERATIONAL Level (52/48)**: Structure/flexibility ratio that enables META balance
- **PI/6 Connection**: Operational ratio derived from PI/6 ≈ 0.5236, where sin(PI/6) = 0.5 connects to META

## Project Structure

```
civilisation_hub/
├── core/                    # Core equilibrium and proportions
│   ├── equilibrium.py      # MetaEquilibrium, Atom, SubParameter classes
│   └── proportions.py      # PI/6, OperationalRatio, ProportionValidator
├── models/                  # Domain model definitions
│   └── domain.py           # Domain, DomainDuality, DomainAttribute
├── knowledge/              # Knowledge domains
│   └── domains/
│       ├── base.py         # KnowledgeDomain base class
│       ├── mathematics.py  # Mathematics domain (Abstract/Concrete duality)
│       ├── physics.py      # Physics domain (Energy/Matter duality)
│       ├── code.py         # Code domain (Abstraction/Implementation duality)
│       ├── biology.py      # Biology domain (Life/Death duality)
│       ├── philosophy.py   # Philosophy domain (Being/Non-Being duality)
│       └── registry.py     # DomainRegistry singleton
├── evolution/              # Evolution tracking
│   ├── tracker.py          # EvolutionTracker, EvolutionState, EvolutionMetrics
│   └── transitions.py      # TransitionEngine, TransitionMatrix
├── participation/          # Participation tracking
│   ├── tracker.py          # ParticipationTracker, ParticipationState
│   └── contributions.py    # ContributionManager, ContributionPool
├── verification/           # Verification system
│   ├── verifier.py         # Verifier, VerificationChain, VerificationRule
│   └── validators.py       # BalanceValidator, MetaEquilibriumValidator
├── output/                 # Output formatting
│   ├── formatters.py       # TextFormatter, JsonFormatter, MarkdownFormatter
│   ├── display.py          # ConsoleDisplay, BufferedDisplay
│   └── reporters.py        # DomainReporter, SystemReporter
├── database/               # Database persistence
│   ├── models.py           # SQLAlchemy models (DomainModel, ConceptModel, etc.)
│   ├── engine.py           # DatabaseEngine, connection management
│   ├── session.py          # SessionManager, transaction context managers
│   ├── repository.py       # Repository pattern (DomainRepository, etc.)
│   └── persistence.py      # DomainPersistenceService
├── data/                   # Database files (auto-created)
│   └── civilisation_hub.db # SQLite database
├── tests/                  # Test suite
│   ├── test_equilibrium.py
│   ├── test_proportions.py
│   ├── test_domain.py
│   ├── test_registry.py
│   ├── test_evolution.py
│   ├── test_participation.py
│   ├── test_verification.py
│   ├── test_knowledge_domains.py
│   ├── test_output.py
│   └── test_database.py
└── main.py                 # Entry point
```

## Key Classes

### MetaEquilibrium (core/equilibrium.py)
Central class for verifying 50/50 balance.
- `verify_balance(positive, negative)` - Check if values are 50/50
- `calculate_balance(positive, negative)` - Calculate ratio
- `register_parameter(name, positive, negative)` - Register and validate parameter

### Atom (core/equilibrium.py)
Wave state model [w⁻|w⁰|w⁺] operating at 52/48 ratio.
- Polar balance (w⁻/w⁺) maintains META 50/50
- Structure/flexibility maintains OPERATIONAL 52/48

### KnowledgeDomain (knowledge/domains/base.py)
Base class for all knowledge domains.
- Each domain has a fundamental duality (positive/negative poles)
- All dualities maintain META 50/50 balance
- `validate_balance()` - Verify domain maintains META compliance
- `prove_meta_meaning()` - Generate META proof

### Domain Dualities

| Domain | Positive Pole | Negative Pole |
|--------|--------------|---------------|
| Mathematics | Abstract | Concrete |
| Physics | Energy | Matter |
| Code | Abstraction | Implementation |
| Biology | Life | Death |
| Philosophy | Being | Non-Being |

### Database Models (database/models.py)

SQLAlchemy models for persisting domains with META 50/50 validation:

- **DualityModel** - Persists domain dualities with balance validation
- **DomainModel** - Persists knowledge domains with concepts and relations
- **ConceptModel** - Persists concepts with certainty/uncertainty balance
- **ConceptRelationModel** - Persists relations between concepts
- **RelationModel** - Persists relations between domains

All models have `validate_meta_compliance()` methods and automatic validation on insert/update.

### DomainPersistenceService (database/persistence.py)

Bridges in-memory KnowledgeDomain objects to database:
- `save_domain(domain)` - Save domain with all concepts and relations
- `load_domain(name)` - Load domain data as dictionary
- `list_domains()` - List all persisted domains
- `delete_domain(name)` - Remove domain from database
- `get_persistence_stats()` - Get database statistics
- `validate_persisted_domains()` - Validate META compliance for all domains

## Working with the Codebase

### Adding New Concepts to a Domain

```python
from knowledge.domains.mathematics import create_mathematics_domain

domain = create_mathematics_domain()
concept = domain.create_concept(
    name="New Concept",
    concept_type=ConceptType.DEFINITION,
    description="Description here",
    certainty=50.0  # Default balanced certainty
)
```

### Creating a New Domain

1. Inherit from `KnowledgeDomain`
2. Implement `_initialize_duality()` with 50/50 balance
3. Implement `_initialize_axioms()` for foundational concepts
4. Implement `get_fundamental_concepts()` to return key concepts

### Validating META Compliance

```python
from core.equilibrium import MetaEquilibrium

meta = MetaEquilibrium()
# Verify any ratio
is_balanced = meta.verify_balance(50, 50)  # True
is_balanced = meta.verify_balance(60, 40)  # False
```

### Persisting Domains to Database

```python
from database.persistence import DomainPersistenceService
from knowledge.domains.mathematics import create_mathematics_domain

# Create and save a domain
domain = create_mathematics_domain()
service = DomainPersistenceService()
service.save_domain(domain)

# Load domain data
data = service.load_domain("Mathematics")
print(f"Concepts: {data['concept_count']}")

# List all saved domains
for d in service.list_domains():
    print(f"{d['name']}: {d['concept_count']} concepts")

# Get statistics
stats = service.get_persistence_stats()
print(f"Total domains: {stats['total_domains']}")
print(f"META compliance: {stats['compliance_rate']}%")
```

### Using Database with CivilisationHub

```python
from main import CivilisationHub

hub = CivilisationHub()
hub.initialize()

# Save all domains
hub.save_domains()

# Save specific domain
hub.save_domain("mathematics")

# List saved domains
for d in hub.list_saved_domains():
    print(d['name'])

# Get database stats
stats = hub.get_persistence_stats()
```

## Running the System

```bash
# Show status
python main.py --status

# Show META proof
python main.py --prove

# Run demonstration
python main.py --demo

# Show specific domain
python main.py --domain mathematics

# Database operations
python main.py --save              # Save all domains to database
python main.py --save-domain NAME  # Save specific domain
python main.py --list-saved        # List saved domains
python main.py --db-stats          # Show database statistics
```

## Testing

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_equilibrium.py -v

# Run with coverage
python -m pytest --cov=.
```

## Design Principles

1. **Every duality must be 50/50** - No exceptions at META level
2. **Operational level enables META** - 52/48 creates dynamic tension for balance
3. **PI/6 derives operational ratio** - Mathematical foundation for 52%
4. **sin(PI/6) = 0.5** - Geometric proof of META connection
5. **All validations prove META meaning** - Every component must validate balance

## Common Patterns

### Factory Functions
Each domain has a `create_*_domain()` factory function:
```python
domain = create_mathematics_domain(meta_equilibrium=shared_meta)
```

### Singleton Registry
```python
from knowledge.domains.registry import get_registry
registry = get_registry()
```

### Buffered Display for Testing
```python
from output.display import BufferedDisplay
display = BufferedDisplay()
display.render("test")
content = display.get_buffer_content()
```
