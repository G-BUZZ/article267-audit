from pathlib import Path

import yaml

from .models import Case


def load_source_register(path: str | Path) -> dict:
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_source_ids(case: Case, source_register: dict) -> None:
    source_ids = {
        source["source_id"]
        for source in source_register.get("sources", [])
    }

    for issue in case.issues:
        if issue.provenance.source_id not in source_ids:
            raise ValueError(
                f"Unknown source_id: {issue.provenance.source_id}"
            )
