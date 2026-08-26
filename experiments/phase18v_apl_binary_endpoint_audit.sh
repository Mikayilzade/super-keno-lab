#!/usr/bin/env bash
set -euo pipefail

OUT="results/phase18v_apl_binary_endpoint_audit.txt"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p results

URL='https://d.apkpure.net/b/XAPK/az.affa.fantasy?version=latest'

{
  echo "Phase 18V — APL Fantasy public binary endpoint audit"
  echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "Package: az.affa.fantasy"
  echo "Source: public APKPure redirect; binary is temporary and is not committed."
  echo
} > "$OUT"

curl -L --fail --retry 2 --connect-timeout 20 --max-time 180 \
  -A 'Mozilla/5.0' "$URL" -o "$TMP/apl.xapk"

printf 'Downloaded bytes: %s\n\n' "$(stat -c%s "$TMP/apl.xapk")" >> "$OUT"

unzip -qq "$TMP/apl.xapk" -d "$TMP/xapk"

# Inventory only; no proprietary binary is preserved.
echo "Archive members:" >> "$OUT"
find "$TMP/xapk" -maxdepth 2 -type f -printf '%P\n' | sort | head -80 >> "$OUT"
echo >> "$OUT"

# Extract printable strings from APKs/native libs/dex and retain only network-looking artifacts.
RAW="$TMP/network_strings.txt"
: > "$RAW"
while IFS= read -r -d '' f; do
  case "$f" in
    *.apk)
      d="$TMP/apk_$(basename "$f" .apk)"
      mkdir -p "$d"
      unzip -qq -o "$f" -d "$d" || true
      find "$d" -type f \( -name '*.dex' -o -name '*.so' -o -name '*.json' -o -name '*.xml' -o -name '*.js' \) -print0 |
        while IFS= read -r -d '' g; do strings -n 6 "$g" 2>/dev/null || true; done >> "$RAW"
      ;;
    *.so|*.dex|*.json|*.xml|*.js)
      strings -n 6 "$f" 2>/dev/null >> "$RAW" || true
      ;;
  esac
done < <(find "$TMP/xapk" -type f -print0)

{
  echo "Candidate absolute URLs:"
  grep -Eao 'https?://[^[:space:]"<>]+' "$RAW" | sed 's/[),;]}]*$//' | sort -u | head -300 || true
  echo
  echo "Candidate APL/Fantaking/API/domain strings:"
  grep -Eai 'aplfantasy|affa-fantasy|fantaking|api[./_-]|graphql|championship|league|ranking|standing|private' "$RAW" |
    sed 's/^[[:space:]]*//' | sort -u | head -500 || true
} >> "$OUT"

# Explicitly verify no downloaded package remains under the repository tree.
if find . -maxdepth 3 -type f \( -name '*.apk' -o -name '*.xapk' -o -name '*.aab' \) | grep -q .; then
  echo "ERROR: binary artifact found in repository tree" >&2
  exit 2
fi

# trigger: phase18v-1
