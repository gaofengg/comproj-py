import compileall
import logging
import os
from pathlib import Path
from random import random
import shutil
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
@click.option('-v', '--version', default=None, type=str, help='Specify the version number.')
# 关于 path 的说明：
# 如果 path 以 / 结尾，会将 path 当成一个目录，并将目录中的每一个子目录当成一个项目迭代编译
# 否则 path 会被当成一个独立的项目编译
def compile(path: str, reserve: bool, version: str):
    # Read the number of files and directories next to the folder specified by path
    if os.name == 'nt':
        import win32api
        import win32con

    def ignore_files(f: str):
        # ignore hide files
        if os.name == 'nt':
            if os.path.isfile(f):
                click.echo(
                    f'WARNING: {f} is a file and should be contained in a folder.')
                return True
            attribute = win32api.GetFileAttributes(f)
            if not len(list(Path(f).rglob("*.py"))):
                return True
            return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM) or ('pyc' in f)
        else:
            # 如果指定目录下有文件，需要将文件包含进文件夹中
            if os.path.isfile(f):
                click.echo(
                    f'WARNING: {f} is a file and should be contained in a folder.')
                return True
            # 过滤已经编译完成的目录
            if not len(list(Path(f).rglob("*.py"))):
                return True
            return f.startswith('.') or ('pyc' in f)  # linux-osx

    file_list = []
    files_num = 0
    # current_day = '-' + datetime.date.today().strftime('%Y.%m.%d')  # 当前日期
    if path == '.' or path.endswith('/'):
        file_list = [f for f in os.listdir(path) if not ignore_files(f)]
        files_num = len(file_list)
    else:
        file_list.append(path)
        files_num = 1

    # Compile all files suffixed with py in the specified directory

    def compile_all_to_pyc(file, version):

        root = Path(file)
        # 先删除根目录下的pyc文件和__pycache__文件夹
        for src_file in root.rglob("*.pyc"):
            os.remove(src_file)
        for src_file in root.rglob("__pycache__"):
            os.rmdir(src_file)

        if version == None:
            version = f'pyc.{random()}'

        edition: str = f'-{version}'  # 设置版本号

        # 目标文件夹名称
        dest = Path(
            # root.parent / f"{root.name}{edition}{current_day}")
            root.parent / f"{root.name}{edition}")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(root, dest)

        compileall.compile_dir(root, force=True)  # 将项目下的py都编译成pyc文件

        for src_file in root.glob("**/*.pyc"):  # 遍历所有pyc文件
            relative_path = src_file.relative_to(root)  # pyc文件对应模块文件夹名称
            # 在目标文件夹下创建同名模块文件夹
            dest_folder = dest / str(relative_path.parent.parent)
            os.makedirs(dest_folder, exist_ok=True)
            dest_file = dest_folder / \
                (src_file.stem.rsplit(".", 1)[
                    0] + src_file.suffix)  # 创建同名文件
            print(f"install {relative_path}")
            shutil.copyfile(src_file, dest_file)  # 将pyc文件复制到同名文件

        # 清除源py文件
        for src_file in dest.rglob("*.py"):
            os.remove(src_file)

        # 清除源目录文件
        if not reserve:
            if os.path.exists(root):
                shutil.rmtree(root)
            dest.rename(root)

    # If there is no file in the folder, output a prompt message and exit
    if files_num == 0:
        logger.error("No files found in the project directory.")
        sys.exit(1)

    # If the number of files in the folder is greater than 1,
    # a prompt message will be output to let the user confirm whether to process all the files
    if files_num > 1:
        logging.warning('More than one file found in the project directory.')
        if click.confirm(
                'All old pyc files and __pycache__ directories will be deleted or replaced with new ones.\nDo you want to compile all files? '):
            click.echo("Compiling all files...")
            for file in file_list:
                compile_all_to_pyc(file, version)

    if files_num == 1:
        for file in file_list:
            compile_all_to_pyc(file, version)


if __name__ == '__main__':
    check_setting_and_env()
    compile()
