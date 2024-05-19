
import click

# Get available finanicial institutions
from beancount_multitool import __INSTITUTIONS__

from beancount_multitool import JABank
from beancount_multitool import RakutenBank
from beancount_multitool import RakutenCard
from beancount_multitool import ShinseiBank

def validate_name(ctx, param, value):
    """Check given name is one of supported financial institutions.
    """
    if value in __INSTITUTIONS__:
        return value
    else:
        raise click.BadParameter(f"Name must be one of: {__INSTITUTIONS__}")

@click.command()
@click.argument('name', type=str, callback=validate_name)
@click.argument('config', type=click.Path(exists=True))
@click.argument('data', type=click.Path(exists=True))
@click.option('--output', default="output.bean", type=click.Path(), help="Resulting Beancount file")
@click.version_option()
def main(name: str, config, data, output):
    """Read financial data and output a Beancount file.

    NAME is the name of the financial institution, e.g. RakutenBank.

    CONFIG is a .toml file with run-time configurations, e.g. config.toml.

    DATA is the raw financial data downloaded from NAME, e.g. input.csv.
    """
    #click.echo(name)
    #click.echo(data)
    #click.echo(config)
    #click.echo(output)
    if name == JABank.NAME:
        tool = JABank(config)
    elif name == RakutenBank.NAME:
        tool = RakutenBank(config)
    elif name == RakutenCard.NAME:
        tool = RakutenCard(config)
    elif name == ShinseiBank.NAME:
        tool = ShinseiBank(config)

    tool.convert(data, output)
