"""Knowledge domains package."""

from knowledge.domains.registry import (
    DomainRegistry,
    get_registry,
    reset_registry,
)

__all__ = [
    "DomainRegistry",
    "get_registry",
    "reset_registry",
]
