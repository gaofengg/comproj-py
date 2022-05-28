import logging
import os
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
def compile(path: click.Path(), reserve: bool):
    # Read the number of files and directories next to the folder specified by path
    if os.name == 'nt':
        import win32api
        import win32con

    def file_is_hidden(p):
        if os.name == 'nt':
            attribute = win32api.GetFileAttributes(p)
            return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
        else:
            return p.startswith('.')  # linux-osx
    file_list = [f for f in os.listdir('.') if not file_is_hidden(f)]
    files_num = len(file_list)

    # Compile all files suffixed with py in the specified directory
    def compile_all_to_pyc():
        pass

    # If there is no file in the folder, output a prompt message and exit
    if files_num == 0:
        logger.error("No files found in the project directory.")
        sys.exit(1)

    # If the number of files in the folder is greater than 1,
    # a prompt message will be output to let the user confirm whether to process all the files
    if files_num > 1:
        if click.confirm('More than one file found in the project directory.\nDo you want to compile all files? '):
            click.echo("Compiling all files...")

    if files_num == 1:
        pass

    for file in file_list:
        print(file)
    click.echo(files_num)
    click.echo(reserve)


if __name__ == '__main__':
    check_setting_and_env()
    compile()
