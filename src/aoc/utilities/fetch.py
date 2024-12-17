from pathlib import Path
import os 
import requests

def _load_session_id():
    res = "53616c7465645f5ff440ddf318d83dd3b40a91e756d80ab2167be270a67cdf0dcdaf15df3617666d33ac9c271c7212c62b9fbcccb95d2d96959290d7559bcc5f"
    if not res:
        raise Exception("Set the AOC_SESSION_ID environment variable")
    return res

INPUT_DIR = Path("inputs/")
HEADERS = {"user-agent": "github.com/Callum-Leach"}
COOKIES = {"session": _load_session_id()}

def get_input(day: int) -> str:
    if not (1 <= day <= 25):
        raise Exception("day must be between 1 and 25 inclusive")

    data_path = INPUT_DIR / Path(str(day))

    if not data_path.exists():
        _fetch(day, data_path)

    return open(data_path).read()


def _fetch(day: int, out_path: Path):
    url = f"https://adventofcode.com/2024/day/{day}/input"

    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if not response.ok:
        raise RuntimeError(
            f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
        )

    os.makedirs(INPUT_DIR, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(response.text[:-1])


