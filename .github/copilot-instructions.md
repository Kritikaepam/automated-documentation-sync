# Automated Documentation Sync - Copilot Instructions

## Project Purpose

This project implements an Agentic SDLC pipeline for automated documentation
synchronization using GitHub Copilot.

The SDLC flow is:

Requirements → Architecture → Design Review → Implementation Planning
→ Implementation → Code Review → Verification → Pull Request

## General Rules

- Always inspect existing files before creating new files.
- Do not invent requirements that are not present in the source material.
- If information is missing, explicitly mark it as "Not Found".
- Ask clarification questions when requirements are ambiguous.
- Do not silently make assumptions about business requirements.
- Keep generated documentation consistent across all SDLC artifacts.
- Prefer small, reviewable changes.
- Do not expose secrets, credentials, tokens, API keys, or personal information.
- Validate user input and external data.
- Follow existing project coding conventions.
- Reuse existing utilities instead of duplicating logic.

## Human-in-the-Loop Rule

Copilot may analyze, recommend, generate and modify files.

However:

- Architecture decisions require human approval.
- Design review findings require human approval.
- Implementation plans require human approval.
- Production code changes require human review.
- Pull requests must not be considered approved automatically.

## Documentation Artifacts

The following files are authoritative:

- requirements.md
- architecture.md
- design-review.md
- impl-plan.md

Changes to implementation must remain consistent with these documents.

## Missing Information

When required information cannot be determined from the available
source material, write:

"Not Found"

Do not fabricate values.

## Testing

Every implementation must include appropriate tests.

Tests should cover:

- Happy path
- Missing input
- Invalid input
- Not Found cases
- External/API failures
- Empty repository or missing files where applicable

## Code Quality

Review for:

- Correctness
- Security
- Error handling
- Test coverage
- Code clarity
- DRY principle
- Dependency safety

## Documentation Sync

When implementation changes behavior described in requirements.md,
architecture.md, or other documentation, identify the inconsistency and
recommend or perform the appropriate documentation update.