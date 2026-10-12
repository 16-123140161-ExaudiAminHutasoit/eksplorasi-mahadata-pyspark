"""Unduh data Cleveland Heart Disease dari UCI ke folder data/."""

from pathlib import Path
import hashlib
from urllib.request import urlretrieve

URL = (
    "https://archive.ics.uci.edu/ml/"
    "machine-learning-databases/heart-disease/processed.cleveland.data"
)
TARGET = Path("data/processed.cleveland.data")
SHA256_DICATAT = "a74b7efa387bc9d108d7d0115d831fe9b414b29ae7124f331b622b4efa0427c8"


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    if not TARGET.exists():
        urlretrieve(URL, TARGET)
    checksum = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    print(f"Lokasi: {TARGET.resolve()}")
    print(f"Ukuran: {TARGET.stat().st_size} bytes")
    print(f"SHA-256: {checksum}")
    if checksum != SHA256_DICATAT:
        raise RuntimeError("Checksum data berbeda dari file yang digunakan dalam eksperimen.")
    print("Dataset sesuai dengan file eksperimen.")


if __name__ == "__main__":
    main()
