from subprocess import check_output
import sys
from typing import Iterable, Iterator, List, NewType

from packaging.version import Version, InvalidVersion


Tag = NewType("Tag", str)


def _get_tags() -> List[Tag]:
    return check_output(["git", "tag"], text=True).strip().split("\n")


def _get_versions(tags: Iterable[Tag]) -> Iterator[Version]:
    for tag in tags:
        try:
            version = Version(tag)
        except InvalidVersion:
            pass
        else:
            yield version


def get_next_dev_version(v: Version, template="{major}.{minor}.dev{dev}") -> Version:
    if v.is_devrelease:
        minor, dev = v.minor, int(v.dev) + 1
    else:
        minor, dev = int(v.minor) + 1, 0
    return Version(template.format(major=v.major, minor=minor, dev=dev))


def main(args=None):
    args = args or list(sys.argv[1:])
    tags = args or _get_tags()
    versions = sorted(_get_versions(tags))
    latest_version = versions[-1]
    next_dev_version = get_next_dev_version(latest_version)
    print(str(next_dev_version))
    return 0


if __name__ == "__main__":
    sys.exit(main())
