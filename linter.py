from SublimeLinter.lint import Linter, util


class Candran(Linter):
    cmd = ('canc', '-parse', '-')
    regex = r'^.+?:.+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)$'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.candran'
    }
