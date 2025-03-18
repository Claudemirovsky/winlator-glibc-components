from pathlib import Path
import json

GIT_RAW_URL = "https://raw.githubusercontent.com"
GIT_REPO_BRANCH = "components"
GIT_REPO = "Claudemirovsky/winlator-glibc-components"
GIT_REPOSITORY_URL = f"{GIT_RAW_URL}/{GIT_REPO}/{GIT_REPO_BRANCH}"

if __name__ == "__main__":
    current = Path()
    valid = (x for x in current.iterdir() if x.is_dir() and not x.name.startswith("."))
    metadata = []
    threshold = 7  # Maximum amount of components of the same type
    for path in valid:
        path_type = path.joinpath("type.txt").read_text()
        files = list(path.glob("*.wcp"))
        valid, old = files[-threshold:], files[:-threshold]
        for file in old:
            file.unlink()
        for file in valid:
            version = file.stem[file.stem.index("-") + 1 :]
            metadata.append(
                {
                    "type": path_type,
                    "verName": version,
                    "verCode": 1,
                    "remoteUrl": f"{GIT_REPOSITORY_URL}/{file.as_posix()}",
                }
            )

    with (current / "metadata.json").open("w+") as f:
        json.dump(metadata, f, indent=4)
