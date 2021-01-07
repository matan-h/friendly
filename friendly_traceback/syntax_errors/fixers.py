"""Various functions used to find fixes to SyntaxErrors"""

from .. import debug_helper
from .. import token_utils


def replace_token(tokens, original_token, new_token_string):
    """Replaces a single token string to produce a new source.
    More specifically, given::

        tokens: a list of tokens
        original_token: single token to be replaced
        replace: new string to replace original_token.string

    It creates a new list of tokens with the replacement having been done,
    untokenize it to produce a modified source which is stripped of
    leading and ending spaces so that it could be inserted in a
    code sample at the beginning of a line with no indentation.
    """
    return _modify_source(tokens, original_token, replace=new_token_string)


def modify_token(tokens, original_token, prepend="", append=""):
    """Replaces a single token string to produce a new source.
    More specifically, given::

        tokens: a list of tokens
        original_token: single token to be replaced
        append: string to append to original_token.string
        prepend: string to prepend to original_token.string

    It creates a new list of tokens with the replacement having been done,
    untokenize it to produce a modified source which is stripped of
    leading and ending spaces so that it could be inserted in a
    code sample at the beginning of a line with no indentation.
    """
    return _modify_source(
        tokens, original_token, original_token.string, prepend=prepend, append=append
    )


def _modify_source(tokens, original_token, replace="", append="", prepend=""):
    """Replaces a single token string to produce a new source.
    More specifically, given::

        tokens: a list of tokens
        original_token: single token to be replaced
        string: new string to use
        add: if True, the new string is added to the existing one

    It creates a new list of tokens with the replacement having been done,
    untokenize it to produce a modified source which is stripped of
    leading and ending spaces so that it could be inserted in a
    code sample at the beginning of a line with no indentation.
    """
    if not tokens:
        debug_helper.log("Problem in fixers._modify_source().")
        debug_helper.log("Empty token list was received")
        debug_helper.log_error()
        return ""

    try:
        new_tokens = []
        for tok in tokens:
            if tok is original_token:
                new_token = original_token.copy()
                new_token.string = prepend + replace + append
                new_tokens.append(new_token)
            else:
                new_tokens.append(tok)

        source = token_utils.untokenize(new_tokens)
        return source.strip()
    except Exception as e:
        debug_helper.log("Problem in fixers._modify_source().")
        debug_helper.log_error(e)
        return ""


def check_statement(statement):
    """Given a single line of code expected to be a valid 'statement',
    that is a line which could be part of a larger source of code and
    contains no unmatched brackets and would not end with the continuation
    character, it is potentially modified to include some required
    'environment' and compiled to see if it raises any SyntaxErrors.

    Returns True if no SyntaxError is raised, False otherwise.
    """
    if not statement:  # If an empty string has been the result of modifying the code.
        return False
    try:
        if statement.endswith(":"):
            statement += " pass"

        if statement.startswith("elif") or statement.startswith("else"):
            statement = if_block % statement
        elif statement.startswith("return") or statement.startswith("yield"):
            statement = def_block % statement
        elif statement.startswith("except") or statement.startswith("finally"):
            statement = try_block % statement

        try:
            compile(statement, "fake-file", "exec")
            return True
        except SyntaxError:
            return False

    except Exception as e:
        debug_helper.log("Problem in token_utils.check_statement().")
        debug_helper.log_error(e)
        return False


if_block = """
if True:
    pass
%s
"""

def_block = """
def test():
    %s
"""

try_block = """
try:
    pass
%s
"""