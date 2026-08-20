import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

source = BASE / "data/canon/official_eotc_inventory.json"
output = BASE / "data/canon/canon_inventory.json"

with source.open(encoding="utf-8") as f:
    data = json.load(f)

entries = []

for i, name in enumerate(data["old_testament"], 1):
    entries.append({
        "canonical_id": f"OT-{i:03d}",
        "testament": "OLD_TESTAMENT",
        "official_name": name,
        "canonical_position": i,
        "identity_status": "UNVERIFIED"
    })

for i, name in enumerate(data["new_testament"], 1):
    entries.append({
        "canonical_id": f"NT-{i:03d}",
        "testament": "NEW_TESTAMENT",
        "official_name": name,
        "canonical_position": i,
        "identity_status": "UNVERIFIED"
    })

result = {
    "schema_version": "1.0.0",
    "source_claim": {
        "old_testament": 46,
        "new_testament": 35,
        "total": 81
    },
    "generated_entries": len(entries),
    "entries": entries
}

with output.open("w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Inventário gerado: {len(entries)} entradas")
print("AT:", sum(x["testament"] == "OLD_TESTAMENT" for x in entries))
print("NT:", sum(x["testament"] == "NEW_TESTAMENT" for x in entries))

assert len(entries) == 81
