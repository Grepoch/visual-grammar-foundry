# Visual Grammar Foundry

[English](README.md) · [简体中文](README.zh-CN.md)

Public interoperability contract for standalone `style-skill` child packages.

This repository is intentionally separate from the private production system:

```text
private repository: visual-grammar-foundry-core
public repository:  visual-grammar-foundry
child repositories: visual-grammar-<slug>
```

The public repository defines the package shape and provides a reusable child template. It does **not** contain the parent orchestration pipeline, private protocols, source inventories, provenance records, research notes, or run artifacts. The private core generates and validates child packages; each released child is exported into its own independent repository.

## Contract

The current public package contract is `contract_version: 1`. A released child is standalone and must include:

- `SKILL.md` as its public entry point;
- `README.md`, `CHANGELOG.md`, `LICENSE`, `ASSET-LICENSE.md`, and `REFERENCES.md`;
- `release.json` with SemVer and public-boundary declarations;
- public `design-system/` catalogs and `evals/` contract files;
- at least three original demonstrations;
- `scripts/validate_public.py` and its standalone CI workflow.

See [`docs/CONTRACT.md`](docs/CONTRACT.md) for the compatibility rules and [`templates/public-child/`](templates/public-child/) for the package scaffold.

## Validation

Validate the public contract repository itself:

```bash
python3 scripts/validate_contract.py
```

A generated and released child is validated from inside that child with:

```bash
python3 scripts/validate_public.py
```

## Naming

- Internal project: **Visual Grammar Foundry**
- Private core repository: `visual-grammar-foundry-core`
- Public contract repository: `visual-grammar-foundry`
- Public child repository: `visual-grammar-<slug>`

## License

The public contract repository is released under the Apache License, Version 2.0. You may use, copy, modify, distribute, sublicense, and sell the repository’s original schemas, templates, validators, and documentation, subject to the Apache-2.0 notice and warranty disclaimer in [`LICENSE`](LICENSE).

Apache-2.0 does not grant access to `visual-grammar-foundry-core`, private run artifacts, unpublished methods, or third-party material. A child package has its own license and rights record; its license covers only child-authored material that the child owner is entitled to license. Source assets, fonts, trademarks, logos, supplied text, and other third-party content remain subject to their own terms. Commercial use of Apache-2.0-covered repository code does not require a separate fee or permission, but every third-party right and child-specific license still needs review.

## Rights and originality

The contract does not grant rights to reproduce source materials. Child packages must not redistribute unverified source assets, copied wording, logos, signatures, distinctive lettering, exact layouts, or source-specific metadata. Attribution is not permission; each release is responsible for its own licenses, rights records, and human originality review.
