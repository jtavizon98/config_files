from pathlib import Path


def _load_secrets():
    secrets_path = Path.home() / ".config" / "qtile" / "secrets.env"

    try:
        lines = secrets_path.read_text().splitlines()
    except OSError as error:
        raise RuntimeError(
            f"Qtile secrets file is missing or unreadable: {secrets_path}"
        ) from error

    secrets = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        name, separator, value = line.partition("=")
        if not separator:
            continue

        name = name.strip()
        if name.startswith("export "):
            name = name[7:].strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        secrets[name] = value

    try:
        return secrets["OPENWEATHER_API_KEY"]
    except KeyError as error:
        raise RuntimeError(
            "OPENWEATHER_API_KEY is missing from "
            f"{secrets_path}"
        ) from error


open_weather = _load_secrets()
