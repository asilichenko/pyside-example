import sys
from pathlib import Path


def _root() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    return Path(__file__).parent.parent


ROOT = _root()

LOGS = ROOT / "logs"

if __name__ == '__main__':
    print(f'{ROOT = }')
    print(f'{LOGS = }')
