"""
friendly_traceback.__init__.py
==============================

With the exceptions of the functions that are specific to the console,
this module contains all the functions that are part of the public API.
While Friendly-traceback is still considered to be in alpha stage,
we do attempt to avoid creating incompatibility for the functions
here when introducing changes.

The goal is to be even more careful to avoid introducing incompatibilities
when reaching beta stage, and planning to be always backward compatible
starting at version 1.0 -- except possibly for the required minimal
Python version.

Friendly-traceback is currently compatible with Python versions 3.6
or newer.

If you find that some additional functionality would be useful to
have as part of the public API, please let us know.
"""
import sys

valid_version = sys.version_info.major >= 3 and sys.version_info.minor >= 6

if not valid_version:
    print("Python 3.6 or newer is required.")
    sys.exit()

del valid_version

# ===========================================

import inspect
import warnings as _warnings
from pathlib import Path

from . import editors_helpers
from . import path_info
from .config import session
from .my_gettext import current_lang
from .theme import rich_available
from .version import __version__  # noqa

# Ensure that warnings are not shown to the end user, as they could
# cause confusion.  Eventually, we might want to interpret them like
# we do for Exceptions.
_warnings.simplefilter("ignore")
del _warnings


def exclude_file_from_traceback(full_path):
    """Exclude a file from appearing in a traceback generated by
    Friendly-traceback.  Note that this does not apply to
    the true Python traceback obtained using "debug_tb"
    """
    path_info.exclude_file_from_traceback(full_path)


def explain(redirect=None):
    """Deprecated: Use explain_traceback() instead."""
    # The reason for removing this is to avoid confusion with
    # explain() used in the console.
    print("explain() is deprecated; please use explain_traceback().")
    session.explain_traceback(redirect=redirect)


def explain_traceback(redirect=None):
    """Replaces a standard traceback by a friendlier one, giving more
    information about a given exception than a standard traceback.
    Note that this excludes ``SystemExit`` and ``KeyboardInterrupt``
    which are re-raised.

    By default, the output goes to ``sys.stderr`` or to some other stream
    set to be the default by another API call. However, if::

       redirect = some_stream

    is specified, the output goes to that stream, but without changing
    the global settings.

    If the string ``"capture"`` is given as the value for ``redirect``, the
    output is saved and can be later retrieved by ``get_output()``.
    """
    session.explain_traceback(redirect=redirect)


def get_output(flush=True):
    """Returns the result of captured output as a string which can be
    written anywhere desired.

    By default, flushes all the captured content.
    However, this can be overriden if desired.
    """
    return session.get_captured(flush=flush)


def install(lang=None, redirect=None, include="explain"):
    """
    Replaces ``sys.excepthook`` by friendly_traceback's own version.
    Intercepts, and provides an explanation for all Python exceptions except
    for ``SystemExist`` and ``KeyboardInterrupt``.

    The optional arguments are:

        lang: language to be used for translations. If not available,
              English will be used as a default.

        redirect: stream to be used to send the output.
                  The default is sys.stderr

        include: controls the amout of information displayed.
        See set_include() for details.
    """
    session.install(lang=lang, redirect=redirect, include=include)


def is_installed():
    """Returns True if Friendly-traceback is installed, False otherwise."""
    return session.installed


def uninstall():
    """Resets sys.excepthook to Python's default."""
    session.uninstall()


def run(
    filename,
    lang=None,
    include="friendly_tb",
    args=None,
    console=True,
    use_rich=False,
    style="dark",
    redirect=None,
):
    """Given a filename (relative or absolute path) ending with the ".py"
    extension, this function uses the
    more complex ``exec_code()`` to run a file.

    If console is set to ``False``, ``run()`` returns an empty dict
    if a ``SyntaxError`` was raised, otherwise returns the dict in
    which the module (``filename``) was executed.

    If console is set to ``True`` (the default), the execution continues
    as an interactive session in a Friendly console, with the module
    dict being used as the locals dict.

    Other arguments include:

    ``lang``: language used; currenly only ``en`` (default) and ``fr``
    are available.

    ``include``: specifies what information is to be included if an
    exception is raised.

    ``args``: strings tuple that is passed to the program as though it
    was run on the command line as follows::

        python filename.py arg1 arg2 ...

    ``use_rich``: set to ``True`` if Rich is available and the environment
    supports it.

    ``theme``: Theme to be used with Rich. Currently only ``dark``,
    the default, and ``light`` are available. ``light`` is meant for
    light coloured background and has not been extensively tested.
    """
    _ = current_lang.translate
    if args is not None:
        sys.argv = [filename]
        sys.argv.extend(list(args))
    else:
        filename = Path(filename)
        if not filename.is_absolute():
            frame = inspect.stack()[1]
            # This is the file from which run() is called
            run_filename = Path(frame[0].f_code.co_filename)
            run_dir = run_filename.parent.absolute()
            filename = run_dir.joinpath(filename)

        if not filename.exists():
            print(_("The file {filename} does not exist").format(filename=filename))
            return

    session.install(lang=lang, include=include, redirect=redirect)
    if use_rich:
        if rich_available:
            session.use_rich = True
            session.set_formatter("rich", style=style)

    module_globals = editors_helpers.exec_code(
        path=filename, lang=lang, include=include
    )
    if console:
        start_console(
            local_vars=module_globals, use_rich=use_rich, banner="", include=include
        )
    else:
        return module_globals


def set_formatter(formatter=None, **kwds):
    """Sets the default formatter. If no argument is given, the default
    formatter is used.

    A custom formatter must accept ``info`` as a required arguments
    as well an additional argument whose value is subject to change.
    See formatters.py for details.
    """
    session.set_formatter(formatter=formatter, **kwds)


def show_again():
    """Shows the previously recorded traceback info again, on the default stream.

    Primarily intended to be used when the user changes
    a verbosity level to view the last computed traceback
    in a given language.
    """
    session.show_traceback_info_again()


def start_console(
    local_vars=None, use_rich=False, include="friendly_tb", lang="en", banner=None
):
    """Starts a Friendly console."""
    from . import console

    console.start_console(
        local_vars=local_vars,
        use_rich=use_rich,
        include=include,
        lang=lang,
        banner=banner,
    )


# =========================================================================
# Below, we have many set_X()/get_X() pairs. The only reason why we include
# the get_X() type of functions is to make it possible to make some
# temporary changes, i.e.
#
#     saved = get_x()
#     set_X(something)
#     do_something()
#     set_X(saved)
# =========================================================================


def set_lang(lang):
    """Sets the language to be used for the display.

    If no translations exist for that language, the original
    English strings will be used.
    """
    session.set_lang(lang)


def get_lang():
    """Returns the current language that had been set for translations.

    Note that the value returned may not reflect truly what is being
    see by the end user: if the translations do not exist for that language,
    the default English strings are used.
    """
    return session.lang


def set_include(include):
    """Specifies the information to include in the traceback.

    Currently allowed values include "explain", "what", "where", "why",
    "hint", "friendly_tb", "python_tb", "debug_tb"

    This will likely change in the near future.
    """
    session.set_include(include)


def get_include():
    """Retrieves the value used to determine what to include in the
    traceback. See ``set_include()`` for details.
    """
    return session.get_include()


def set_stream(redirect=None):
    """Sets the stream to which the output should be directed.

    If the string ``"capture"`` is given as argument, the
    output is saved and can be later retrieved by ``get_output()``.

    If no argument is given, the default stream (stderr) is set.
    """
    session.set_redirect(redirect=redirect)


def get_stream():
    """Returns the value of the current stream used for output."""
    return session.write_err


# -----------------------------------------
#   Deprecated functions
# -----------------------------------------


def set_level(verbosity_level):
    """Deprecated. Details about new API to be provided later."""
    print("friendly-traceback set_level is deprecated; defaults will be used.")
    set_include("explain")
