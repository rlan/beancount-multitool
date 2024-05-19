from .__version__ import __version__  # noqa

from .as_transaction import as_transaction
from .read_config import read_config

__INSTITUTIONS__ = []

from .JABank import JABank
__INSTITUTIONS__.append(JABank.NAME)

from .RakutenBank import RakutenBank
__INSTITUTIONS__.append(RakutenBank.NAME)

from .RakutenCard import RakutenCard
__INSTITUTIONS__.append(RakutenCard.NAME)

from .ShinseiBank import ShinseiBank
__INSTITUTIONS__.append(ShinseiBank.NAME)
