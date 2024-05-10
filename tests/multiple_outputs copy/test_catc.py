from catc.config import Config, CONFIG_FILE_NAME
from os.path import join, dirname, exists
from ..helpers import run_catc

PROJECT_ROOT = join(dirname(__file__), "project")
config = Config.from_file(join(PROJECT_ROOT, CONFIG_FILE_NAME))


def test_catc():
    run_catc("project", dirname(__file__))

    for out in config.output:
        assert exists(join(PROJECT_ROOT, out))
