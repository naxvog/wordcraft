#!/bin/sh
# The harness's WORDCRAFT_CLI while scoring: `convert <fixture>/input.docx <out.pdf>` hands it the PDF the PR's
# binary made beforehand in its own container (score.sh step 2); no PDF there means the conversion failed.
[ "$1" = convert ] || exit 2
rel=${2#*tests/fixtures/}
cp "/pdf/${rel%/input.docx}/wordcraft.pdf" "$3"
