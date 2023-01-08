"""Script Tools
"""
import os
from pathlib import Path

from tomlkit import parse
import pysftp


TOML_FILE_TEMPLATE = """\
[sftp]
user = "user"
port = "port"
host = "host"
password = "password"
"""

ROMOTE_DIR = "/usr/share/nginx/work-wiki"


def init():
    """Initializing configuration file
    """
    app_data_dir = Path(os.getenv('APPDATA'))
    sphinx_doc_server_path = app_data_dir / "sphinx_doc_server"
    sphinx_doc_server_path.mkdir(parents=True, exist_ok=True)
    config_file = (sphinx_doc_server_path / "config.toml")
    if not config_file.exists():
        config_file.write_text(TOML_FILE_TEMPLATE, encoding="utf8")

def publish():
    """Publish to remote server
    """
    app_data_dir = Path(os.getenv('APPDATA'))
    sphinx_doc_server_path = app_data_dir / "sphinx_doc_server"
    config_file = (sphinx_doc_server_path / "config.toml")
    toml_file = parse(config_file.open("r", encoding="utf8").read())
    user = toml_file['sftp']['user']
    port = int(toml_file['sftp']['port'])
    host = toml_file['sftp']['host']
    password = toml_file['sftp']['password']

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None 
    with pysftp.Connection(
            host,
            port=port,
            username=user,
            password=password,
            cnopts=cnopts
        ) as sftp:
        local_dir = Path("home/build/html").absolute().as_posix()
        sftp.put_r(local_dir, ROMOTE_DIR, preserve_mtime=True)

def build():
    """build docs
    """
    make_file = Path("home/make.bat").absolute().as_posix()
    os.system(f"{make_file} html")

def show():
    """show local doc server
    """
    os.system(".\\home\\build\\html\\index.html")

def show_remote():
    """show remote doc server
    """
    # pylint: disable=W0511
    # TODO: support `bash`
    os.system("""explorer "https://workwiki.3gee.me/index.html" """)
    