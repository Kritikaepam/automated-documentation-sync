---
name: code-review
description: Perform a complete pre-PR code review.
agent: Code Review Agent
---

# Code Review

Review the entire implementation against:

requirements.md
architecture.md
design-review.md
impl-plan.md

Evaluate:

- Correctness
- Security
- Error handling
- Test coverage
- Code clarity
- DRY principle
- Dependency safety

Return a structured review.

End with either:

APPROVED

or

CHANGES REQUIRED