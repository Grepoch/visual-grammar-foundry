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

## License and scope

This child package uses the MIT License for original child-authored code, instructions, schemas, and demonstrations that the package owner is entitled to license. Commercial use of that MIT-covered material is allowed without a separate fee or permission, subject to the MIT notice and warranty disclaimer in `LICENSE`.

The MIT License does **not** relicense supplied source materials, third-party images, fonts, logos, trademarks, user-provided text, model outputs, or other assets. Those materials remain subject to the terms recorded in `REFERENCES.md` and `ASSET-LICENSE.md`. Attribution is not permission. Do not publish or commercially use an asset unless its rights have been verified.
