
# Security policy

## Reporting a vulnerability

Report security vulnerabilities privately through GitHub's private vulnerability reporting:

<https://github.com/nfdi4cat/CoreMeta4Cat/security/advisories/new>

Do not open a public issue or disclose vulnerabilities publicly before they have been addressed.

Please include a description of the vulnerability, its potential impact, and steps to reproduce it, if possible. The maintainers will acknowledge receipt and coordinate with the reporter on assessment, remediation, and disclosure.

## Scope

This repository covers:

- The CoreMeta4Cat LinkML schema, including its modules defining the shared metadata model and the Synthesis, Characterization, Reaction, and Simulation domains.
- Scripts and tooling used to validate, transform, and generate schema-derived artifacts, including Python datamodels, OWL, JSON-LD, TypeScript, and Excel workbooks.
- GitHub Actions workflows and other automation used to test, validate, generate, and publish project artifacts.
- The documentation and reference materials published through GitHub Pages.
- The Metadata Checker web application and associated scripts and resources maintained in this repository.

Report vulnerabilities in third-party dependencies or upstream projects to their respective maintainers as well. Please notify the CoreMeta4Cat maintainers if the vulnerability also affects this repository.

## Supported versions

Security fixes are made on the `main` branch.

Updates to the schema, tooling, and documentation are published through the project's regular development and release processes.

Released versions and their generated artifacts are considered fixed snapshots. Security fixes are generally applied to the current development version rather than retroactively modifying previous releases.
