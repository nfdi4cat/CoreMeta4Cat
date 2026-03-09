# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="coremeta4cat"
LINKML_SCHEMA_AUTHOR="Hendrik Borgelt <hendrik.borgelt@tu-dortmund.de>"
LINKML_SCHEMA_DESCRIPTION="CoreMeta4Cat is a community-driven metadata initiative under NFDI4Cat that defines the minimum information required for reporting catalysis research data. Built on the FAIR principles — Findable, Accessible, Interoperable, and Reusable — it provides a shared language for researchers to describe, share, and discover catalysis datasets across institutions and disciplines. By standardizing metadata, CoreMeta4Cat aims to enhance data interoperability, facilitate data sharing, and accelerate scientific discovery in the field of catalysis."
LINKML_SCHEMA_SOURCE_DIR="src/coremeta4cat/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS="--truncate-descriptions False --hierarchical-class-view --subfolder-type-separation --index-name overview"

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS=

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
