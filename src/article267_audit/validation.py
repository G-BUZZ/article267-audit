from pathlib import Path

import yaml

from .models import Case


def load_case(path: str | Path) -> Case:
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return Case.model_validate(data)


def validate_case(path: str | Path) -> None:
    load_case(path)
