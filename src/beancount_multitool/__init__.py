from .__version__ import __version__  # noqa

# from .as_transaction import as_transaction
# from .read_config import read_config
from .ChaseSPCard import ChaseSPCard
from .JABank import JABank
from .RakutenBank import RakutenBank
from .RakutenCard import RakutenCard
from .ShinseiBank import ShinseiBank
from .SumishinNetBank import SumishinNetBank

__INSTITUTIONS__ = []
__INSTITUTIONS__.append(ChaseSPCard.NAME)
__INSTITUTIONS__.append(JABank.NAME)
__INSTITUTIONS__.append(RakutenBank.NAME)
__INSTITUTIONS__.append(RakutenCard.NAME)
__INSTITUTIONS__.append(ShinseiBank.NAME)
__INSTITUTIONS__.append(SumishinNetBank.NAME)
