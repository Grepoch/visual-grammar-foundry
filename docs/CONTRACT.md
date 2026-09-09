# Public child contract

This repository defines the public interoperability surface between `visual-grammar-foundry-core` and independently released `visual-grammar-<slug>` child repositories.

## Version dimensions

- `contract_version` identifies the public package shape. The current value is `1`.
- Child `version` is SemVer and describes the child’s behavior compatibility.
- Private run identifiers and provenance records stay in the core repository.

A contract-version change requires coordinated updates to the schemas, child template, standalone validator, CI, and migration notes.

## Boundary

The public contract may contain operational behavior, public catalogs, public eval cases, original demonstrations, and safe attribution notes. It must not contain private training notes, discovery history, source inventories, hidden routing weights, prompts, private scores, or raw source materials without verified redistribution rights.

## Release requirements

A child release must:

1. use a lowercase kebab-case slug and a SemVer version;
2. declare `contract_version: 1` in `release.json`;
3. include every file listed by `required_files`;
4. declare `contains_private_training_notes: false` and `contains_source_reconstruction: false`;
5. contain at least three original examples and three public eval cases;
6. state provenance status in `REFERENCES.md`;
7. pass its standalone `scripts/validate_public.py` check;
8. receive human review before publication.

The template contains placeholders by design and is not itself a released child. The private core replaces those placeholders during compilation and runs the standalone validator before export.
