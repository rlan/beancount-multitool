# This file is needed for Pytest
import sys

if __name__ == "__main__":
    from .cli import main
    sys.exit(main())
