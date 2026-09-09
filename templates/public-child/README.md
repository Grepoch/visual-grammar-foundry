# {{CHILD_NAME}}

A reusable public style-skill generated from a supplied material set.

## Use

Invoke the skill with a subject, text, image, or carrier request. The skill applies its learned visual grammar while producing an original result rather than reconstructing a source reference.

### Examples

- `Use {{CHILD_SLUG}} to make an original poster about a night market.`
- `Transform this supplied image with {{CHILD_SLUG}} while preserving the subject.`
- `Use {{CHILD_SLUG}} for a square cover. Keep the exact title “SIDE B”.`

## Public behavior

- Exact user-supplied text and factual content are preserved.
- Unspecified choices use stable defaults.
- Supplied references are treated as visual evidence, not templates.
- The output includes the artifact when tools are available and a production specification when they are not.

## Included

- `SKILL.md`: public entry point
- `design-system/`: operational tokens and bounded choices
- `evals/`: public behavior contract
- `examples/`: original demonstrations
- `REFERENCES.md`: provenance and attribution
- `scripts/validate_public.py`: standalone public-package validator

## Versioning

The child is independently versioned with semantic versions in `release.json` and `CHANGELOG.md`. Create a Git tag for public releases, for example `v1.0.0`. Keep the child package version separate from the parent’s private run identifier and from the public contract/schema version. The package can be maintained and validated without the parent project.

## Rights, attribution, and assets

See `REFERENCES.md` and `ASSET-LICENSE.md`. Attribution is not permission: source material remains subject to its original rights and is not automatically relicensed by this package. Unknown or unauthorized source material must not be redistributed. “Distillation” or “style transfer” does not guarantee a legal right to copy protected expression, trademarks, personal data, or provider output.
