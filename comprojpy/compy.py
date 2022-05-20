import logging
import logging
import sys
import click

logger = logging.getLogger('comprojpy')


def check_setting_and_env():
    logger.info("Checking settings and environment...")
    if sys.version_info < (3, 6):
        logger.error("Python 3.6 or higher is required to run this program.")
        sys.exit(1)


@click.command()
@click.option('-p', '--path', default='.', type=click.Path(), help='Path to the project.')
@click.option('-r', '--reserve', default=True, type=bool, help='True means Reserve the project source directory.')
def compile(path: str, reserve: bool):
    click.echo(path)
    click.echo(reserve)


if __name__ == '__main__':
    check_setting_and_env()
    compile()
