#!/usr/bin/env bash
# Build one week's worksheet + answer-key PDFs from its .md source.
# Usage: ./build.sh 01 ../week-01/Week-01-Fields-Vector-Space-Axioms-Complex-Numbers.md ./hints/week-01.json /tmp/out
set -euo pipefail
WEEK="$1"; MD="$2"; HINTS="$3"; OUT="$4"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$DIR/render.py" "$MD" "$WEEK" "$HINTS" "$OUT"

for kind in worksheet answerkey; do
  pandoc "$OUT/Week-$WEEK-$kind.md" -o "$OUT/Week-$WEEK-$kind.pdf" \
    --pdf-engine=xelatex -V geometry:margin=0.9in -V fontsize=11pt -V colorlinks=true \
    -H "$DIR/preamble.tex" --from markdown+raw_tex
  echo "wrote $OUT/Week-$WEEK-$kind.pdf"
done
