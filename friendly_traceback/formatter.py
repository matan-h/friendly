"""formatter.py

First version - needs to be documented.
"""
import inspect
import os

from . import generic_info
from . import specific_info

CONTEXT = 4


def explain_traceback(etype, value, tb):
    """ Provides a basic explanation for a traceback.

        Consider the following example, that has four different parts

        # 1. Generic explanation
        Python exception:
            NameError: name 'c' is not defined

        A NameError exception indicates that a variable or
        function name is not known to Python.
        Most often, this is because there is a spelling mistake.
        However, sometimes it is because the name is used
        before being defined or given a value.

        # 2. Likely cause
        Likely cause:
            In your program, the unknown name is 'c'.

        # 3. last call made
        Execution stopped on line 48 of file 'tb_common.py'.

           46:                     mod = __import__(name)
           47:                     if function is not None:
        -->48:                         getattr(mod, function)()
           49:                 except Exception:

        # 4. origin of the exception
        Exception raised  on line 8 of file 'raise_name_error.py'.

            6:     # Should raise NameError
            7:     a = 1
        --> 8:     b = c
            9:     d = 3

    """
    result = []

    result.append(provide_generic_explanation(etype.__name__, value))
    cause = get_likely_cause(etype, value)
    if cause is not None:
        result.append(cause)

    records = inspect.getinnerframes(tb, CONTEXT)

    _frame, filename, linenumber, _func, lines, index = records[0]  # last call
    info = get_source_info(filename, linenumber, lines, index)
    result.append(add_source_info(info))

    if len(records) > 1:
        _frame, filename, linenumber, _func, lines, index = records[-1]  # origin
        info = get_source_info(filename, linenumber, lines, index)
        result.append(add_source_info(info, last_call=False))

    return "\n".join(result)


def provide_generic_explanation(name, value):
    """Provides a generic explanation about a particular error.
    """
    if name in generic_info.generic:
        explanation = generic_info.generic[name]()
    else:
        explanation = generic_info.generic["Unknown"]()
    # fmt: off
    return _(
        "\n"
        "    Python exception: \n"
        "        {name}: {value}\n"
        "\n"
        "{explanation}"
    ).format(name=name, value=value, explanation=explanation)
    # fmt: on


def get_likely_cause(etype, value):
    if etype.__name__ in specific_info.get_cause:
        return _("    Likely cause:\n{cause}").format(
            cause=specific_info.get_cause[etype.__name__](etype, value)
        )
    else:
        return None


def get_source_info(filename, linenumber, lines, index):
    if filename and os.path.abspath(filename):
        filename = os.path.basename(filename)
    elif not filename:
        return None
    if index is not None:
        source = highlight_source(linenumber, index, lines)
    else:
        return None

    return {"filename": filename, "source": source, "linenumber": linenumber}


def add_source_info(info, last_call=True):

    if last_call:
        message = _(
            "\n"
            "    Execution stopped on line {linenumber} of file '{filename}'.\n"
            "\n"
            "{source}\n"
        ).format(**info)

    else:
        message = _(
            "\n"
            "    Exception raised  on line {linenumber} of file '{filename}'.\n"
            "\n"
            "{source}\n"
        ).format(**info)

    return message


def highlight_source(linenumber, index, lines):
    """Displays a few relevant lines from a file, showing line numbers
       and identifying a particular line.
    """
    new_lines = []
    nb_digits = len(str(linenumber + index))
    no_mark = "       {:%d}: " % nb_digits
    with_mark = "    -->{:%d}: " % nb_digits
    i = linenumber - index
    for line in lines:
        if i == linenumber:
            num = with_mark.format(i)
        else:
            num = no_mark.format(i)
        new_lines.append(num + line.rstrip())
        i += 1
    return "\n".join(new_lines)
