from incolumepy_curso_hashtag_instagram_bot import __version__
import re
import pytest


@pytest.mark.parametrize(
    'version',
    [
        __version__,
        '0.1.0-dev.0',
        '0.1.0-alpha.11',
        '0.1.0-beta.111',
        '10.1.0-rc.111',
    ],
)
def test_version(version):
    regex = r'\d+(\.\d+){2}(-\w+\.\d+)?'
    assert re.compile(regex).fullmatch(version)
