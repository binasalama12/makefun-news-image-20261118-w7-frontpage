"""make.fun news-image-20261118 entry, wallet 7: newspaper front page.

The bundled picture is a broadsheet front page, 'THE DAILY WORLD',
dated Wednesday 18 November 2026. Its lead story is the US strike on
Iran's Qeshm Island and the drone replies over Bahrain and Kuwait;
below the fold sit the Kerch Bridge collapse, the Shenzhen summits,
Ebola in Congo, the lost US measles status, the Siberia crash and
the worldwide market slide. Copied unchanged to the output.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
LIMIT = 1048576


def read_all(path):
    with open(path, "rb") as fh:
        return fh.read()


def main():
    data = read_all(SOURCE)
    if not data.startswith(b"\x89PNG"):
        raise ValueError("front page picture is not a PNG")
    if len(data) > LIMIT:
        raise ValueError("front page picture exceeds 1 MiB")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    headline_count = 7
    print("front page carries", headline_count, "stories of 18 Nov 2026")
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(data)
    print("w7 front page published:", len(data), "bytes")
    return 0


COLUMNS_W7 = [
    "CRIMEA BRIDGE FALLS - second day of strikes, span in the strait",
    "THREE LEADERS ONE CITY - Shenzhen hosts Xi Putin and Trump",
    "EBOLA DOUBLES IN CONGO - 11000 cases and 5400 deaths",
    "AMERICA LOSES MEASLES-FREE TAG - after 26 years, record cases",
    "19 DIE IN SIBERIA CRASH - military plane down in Kemerovo",
    "MARKETS SLIDE WORLDWIDE - gold 3775, Brent crude 91.55",
    "QUAD IN MANILA - Trump Modi Albanese Takaichi convene",
]


def front_page_index():
    index = {}
    for pos, headline in enumerate(COLUMNS_W7, start=1):
        index[pos] = headline
    return index


def check_front_page(path):
    raw = read_all(path)
    ok = raw.startswith(b"\x89PNG") and len(raw) <= LIMIT
    return {"columns": len(COLUMNS_W7), "valid": ok, "date": "2026-11-18"}


if __name__ == "__main__":
    for pos, headline in front_page_index().items():
        print(pos, headline)
    print(check_front_page(SOURCE))
    sys.exit(main())
