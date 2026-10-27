# Knowledge Memory Architecture v0.1 — Storage Foundation

Status: ARCHITECTURAL DRAFT
Scope: Memory storage and retrieval foundation
Relationship: Independent of H-JEPA implementation

## 1. Principle

Memory stores reusable value, not everything that happened.

Storage is not confirmation:
Storage != Verification != Adoption

## 2. Three memory classes

### Experience Memory
Stores useful episodes, observations, hypotheses, actions/search paths, outcomes, evidence, and uncertainty.

### Knowledge Memory
Stores distilled claims with evidence, verification state, scope, dependencies, and lineage.

### Procedural Memory
Stores reusable procedures/skills with preconditions, execution steps, expected results, and failure conditions.

## 3. Minimal Memory Record

id
type
content
source
evidence
status
confidence
scope
timestamp
dependencies
reuse_count

## 4. Status lifecycle

CANDIDATE -> LOCKED -> VERIFIED -> CONFIRMED -> ADOPTED

Not every record must reach ADOPTED.

## 5. Retrieval boundary

Current State -> Memory Router -> relevant Experience / Knowledge / Procedure

The router is replaceable; storage technology is not part of the core contract.

## 6. Retention

KEEP: active reusable value
CONSOLIDATE: redundant records become a stronger compact representation
ARCHIVE: historical value remains but leaves the hot retrieval path

Failures are retained when they carry reusable negative knowledge.

## 7. Separation

Working Memory = current active state.
Knowledge Memory = durable distilled memory.
Knowledge Circle = broader knowledge lifecycle.

No layer silently replaces another.

## 8. Next design gate

Before implementation, define:
- exact record schemas
- retrieval scoring
- consolidation rules
- retention thresholds
- promotion evidence
- indexing strategy
- cold/archive representation