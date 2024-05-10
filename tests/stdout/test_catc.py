import shutil
from itertools import permutations
from catc.config import Config, CONFIG_FILE_NAME
from os.path import join, dirname
from ..helpers import run_catc

PROJECT_ROOT = join(dirname(__file__), "project")
config = Config.from_file(join(PROJECT_ROOT, CONFIG_FILE_NAME))


def setup_module():
    shutil.rmtree(join(PROJECT_ROOT, "gen"), ignore_errors=True)


def test_catc():
    merged = run_catc(path="project", cwd=dirname(__file__)).rstrip("\n")

    possible_cases = [config.separator.join(p) for p in permutations("abc")]
    assert merged in possible_cases
