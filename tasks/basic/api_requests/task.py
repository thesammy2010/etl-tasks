from typing import Dict

import requests  # pylint: disable=E0401

URL: str = "https://api.exchangeratesapi.io/2020-09-01"


def main() -> None:

    req: requests.models.Response = requests.get(URL)
    print(req.url, req.status_code, req.encoding)
    data: Dict[str, Dict[str, float]] = req.json()
    print(data)


if __name__ == "__main__":
    main()
