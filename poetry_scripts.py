"""Script Tools
"""
import os
from collections.abc import Generator
from pathlib import Path
from contextlib import contextmanager

from tomlkit import parse
from paramiko import SFTPClient, Transport
from rich.console import Console
from rich.progress import Progress

_console = Console()

TOML_FILE_TEMPLATE = """\
[sftp]
user = "user"
port = "port"
host = "host"
password = "password"
"""

REMOTE_DIR = "/usr/share/nginx/work-wiki"
LOCAL_BUILD_PAH = Path(".") / "home" / "build" / "html"


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
    _console.print("[green] begin to publish...")
    copy_dir_by_sftp(LOCAL_BUILD_PAH, REMOTE_DIR)


@contextmanager
def sftp_server(
        host: str,
        port: int,
        user: str,
        password: str
    ) -> Generator[SFTPClient, None, None]:
    """SFTP Server

    Args:
        host (str): host
        port (int): port
        user (str): user
        password (str): password

    Returns:
        SFTPClient: SFTPClient

    Yields:
        Iterator[SFTPClient]: SFTPClient
    """
    try:
        tp = Transport((host, port)) # pylint: disable=C0103
        tp.connect(None, user, password)
        sftp = SFTPClient.from_transport(tp)
        yield sftp
    finally:
        if sftp:
            sftp.close()
        if tp:
            tp.close()

def copy_dir_by_sftp(
        local_path: Path,
        remote_dir: str
    ) -> None:
    """Using paramiko to upload file

    Args:
        local_path (Path): Local Directory Path
        remote_dir (str): Remote Direcrory string
    """
    app_data_dir = Path(os.getenv('APPDATA'))
    sphinx_doc_server_path = app_data_dir / "sphinx_doc_server"
    config_file = (sphinx_doc_server_path / "config.toml")
    toml_file = parse(config_file.open("r", encoding="utf8").read())
    user = toml_file['sftp']['user']
    port = int(toml_file['sftp']['port'])
    host = toml_file['sftp']['host']
    password = toml_file['sftp']['password']

    local_path_list = sorted(list(LOCAL_BUILD_PAH.glob("**/*")))
    file_num = len(local_path_list)
    with Progress() as progress:
        task = progress.add_task("[green]Uploading...", total=file_num)

        with sftp_server(host, port, user, password) as sftp:
            for i, temp_path in enumerate(local_path_list):
                progress.update(task, advance=1)
                progress.console.print(
                    f"[green bold][reverse][{i+1}/{file_num}][/reverse] start to copy "
                    f"[underline]{temp_path.as_posix()}[/underline]"
                )
                if temp_path.is_dir():
                    progress.console.print(
                        f"[cyan][reverse][{i+1}/{file_num}][/reverse] "
                        f"[underline]{temp_path.as_posix()}[/underline] is a folder"
                    )
                    remote_folder = Path(remote_dir) / temp_path.relative_to(local_path)
                    try:
                        progress.console.print(
                            f"[cyan][reverse][{i+1}/{file_num}][/reverse] make directory "
                            f"[underline]{remote_folder.as_posix()}[/underline]"
                        )
                        sftp.mkdir(remote_folder.as_posix())
                    except OSError:
                        progress.console.print(
                            f"[magenta][reverse][{i+1}/{file_num}][/reverse] skip folder "
                            f"[underline]{temp_path.as_posix()}[/underline]"
                        )
                else:
                    progress.console.print(
                        f"[cyan][reverse][{i+1}/{file_num}][/reverse] "
                        f"[underline]{temp_path.as_posix()}[/underline] is a file"
                    )
                    remote_file = Path(remote_dir) / temp_path.relative_to(local_path)
                    progress.console.print(
                            f"[cyan][reverse][{i+1}/{file_num}][/reverse] copy "
                            f"[underline]{temp_path.as_posix()}[/underline]"
                            f" to [underline]{remote_file.as_posix()}[/underline]"
                        )

                    sftp.put(temp_path.as_posix(), remote_file.as_posix())


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
    