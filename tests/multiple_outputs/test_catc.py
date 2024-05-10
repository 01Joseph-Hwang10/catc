import shutil
from itertools import permutations
from catc.config import Config, CONFIG_FILE_NAME
from os.path import join, dirname
from ..helpers import run_catc, read

PROJECT_ROOT = join(dirname(__file__), "project")
config = Config.from_file(join(PROJECT_ROOT, CONFIG_FILE_NAME))


def setup_module():
    shutil.rmtree(join(PROJECT_ROOT, "gen"), ignore_errors=True)


def test_catc():
    run_catc(path="project", cwd=dirname(__file__))

    for out in config.destinations:
        possible_cases = [config.separator.join(p) for p in permutations("abc")]
        assert read(join(PROJECT_ROOT, out)) in possible_cases
