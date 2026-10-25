"""
    pygments.lexers.rgc
    ~~~~~~~~~~~~~~~~~~~

    Lexer for the RGC programming language.

    RGC is a Python-style, compiled, statically typed language with
    ownership/borrow checking and an LLVM backend.

    :copyright: Copyright 2006-present by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace

__all__ = ['RgcLexer']


class RgcLexer(RegexLexer):
    """
    Lexer for the RGC programming language.

    Example::

        def fib(n: int) -> int:
            if n <= 1:
                return n
            return fib(n - 1) + fib(n - 2)
    """
    name = 'RGC'
    url = 'https://github.com/rgc-lang/rgc'
    aliases = ['rgc']
    filenames = ['*.rg']
    mimetypes = ['text/x-rgc']
    version_added = '2.22'
    _example = 'rgc/test.rg'

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'#.*$', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),

            (r'"(\\\\|\\"|[^"\\])*"', String),

            (words((
                'def', 'class', 'enum', 'interface', 'import',
                'if', 'elif', 'else', 'for', 'in', 'while',
                'match', 'case', 'and', 'or', 'not',
                'return', 'break', 'continue', 'pass', 'var',
            ), suffix=r'\b'), Keyword),
            (words(('int', 'float', 'bool', 'str'), suffix=r'\b'),
             Keyword.Type),
            (words(('True', 'False', 'None'), suffix=r'\b'),
             Keyword.Constant),

            (r'@var\b', Keyword),
            (r'@[A-Za-z_][A-Za-z0-9_]*', Name.Decorator),

            (r'0[xX][0-9a-fA-F_]+', Number.Hex),
            (r'0[bB][01_]+', Number.Bin),
            (r'0[oO][0-7_]+', Number.Oct),
            (r'[0-9][0-9_]*(\.[0-9][0-9_]*)?([eE][+-]?[0-9][0-9_]*)?',
             Number),
            (r'\.[0-9][0-9_]*([eE][+-]?[0-9][0-9_]*)?', Number.Float),

            (r'\b[A-Za-z_][A-Za-z0-9_]*(?=\s*\()', Name.Function),
            (r'\b[A-Za-z_][A-Za-z0-9_]*\b', Name),

            (r'->|=>|<<|>>|\*\*|//', Operator),
            (r'[+\-*/%&|^~!<>=]=?', Operator),
            (r'[()\[\]{}.,:;@]', Punctuation),
        ],
    }

    def analyse_text(text):
        if re.search(r'\bdef\s+[A-Za-z_]\w*\s*\([^)]*\)\s*->', text):
            return 0.4
        if re.search(r'\b@var\b', text):
            return 0.3
        if re.search(r'\b(?:interface|enum)\s+[A-Za-z_]\w*', text):
            return 0.2
        return 0.0