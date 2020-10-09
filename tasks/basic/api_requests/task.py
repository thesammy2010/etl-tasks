import logging
from typing import Any

import requests  # pylint: disable=E0401

URL: str = "https://api.exchangeratesapi.io/2020-09-01"


def get_response(url: str = URL) -> Any:

    req: requests.models.Response = requests.get(URL)
    logging.info(req.url, req.status_code, req.encoding)

    return req.json()


def main() -> None:

    rates = get_response()

    sum_of_rates: float = sum([rates["rates"].get(key) for key in rates["rates"].keys()])

    print(sum_of_rates)


if __name__ == "__main__":
    main()
