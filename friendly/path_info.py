"""path_info.py

In many places, by default we exclude the files from this package,
thus restricting tracebacks to code written by the users.

If Friendly-traceback is used by some other program,
it might be desirable to exclude additional files.
"""
import os

EXCLUDED_FILE_PATH = set()
EXCLUDED_DIR_NAMES = set()


def exclude_file_from_traceback(full_path):
    """Exclude a file from appearing in a traceback generated by
    Friendly-traceback.  Note that this does not apply to
    the true Python traceback obtained using "debug_tb".
    """
    EXCLUDED_FILE_PATH.add(full_path)


def exclude_directory_from_traceback(dir_name):
    """Exclude all files found in a given directory, including sub-directories,
    from appearing in a traceback generated by Friendly.
    Note that this does not apply to the true Python traceback
    obtained using "debug_tb".
    """
    if dir_name[-1] != os.path.sep:
        dir_name += os.path.sep
    EXCLUDED_DIR_NAMES.add(dir_name)


dirname = os.path.dirname(__file__)
exclude_directory_from_traceback(dirname)


def is_excluded_file(full_path):
    """Determines if the file belongs to the group that is excluded from tracebacks."""
    if full_path.startswith("<frozen "):
        return True
    for dirs in EXCLUDED_DIR_NAMES:
        if full_path.startswith(dirs):
            return True
    return full_path in EXCLUDED_FILE_PATH


def include_file_in_traceback(full_path):
    """Reverses the effect of ``exclude_file_from_traceback()`` so that
    the file can potentially appear in later tracebacks generated
    by Friendly-traceback.

    A typical pattern might be something like::

         import some_module

         revert = not is_excluded_file(some_module.__file__)
         if revert:
             exclude_file_from_traceback(some_module.__file__)

         try:
             some_module.do_something(...)
         except Exception:
             friendly.explain_traceback()
         finally:
             if revert:
                 include_file_in_traceback(some_module.__file__)

    """
    EXCLUDED_FILE_PATH.discard(full_path)


class PathUtil:
    def __init__(self):
        self.python = os.path.dirname(os.__file__)
        this_dir = os.path.dirname(__file__)
        self.friendly_path = os.path.abspath(os.path.join(this_dir, ".."))
        self.tests = ""
        tests = os.path.join(self.friendly_path, "tests")
        if os.path.exists(tests):
            self.tests = tests
        self.home = os.path.expanduser("~")
        self.cwd = os.getcwd()

    def shorten_path(self, path):
        if path is None:  # can happen in some rare cases
            return path
        path = path.replace("'", "")  # We might get passed a path repr
        path = os.path.normpath(path)
        path_lower = path.lower()
        self.cwd = os.getcwd()  # make sure it is up to date
        if self.tests and path_lower.startswith(self.tests.lower()):
            path = "TESTS:" + path[len(self.tests) :]
        elif path_lower.startswith(self.friendly_path.lower()):
            path = "FRIENDLY:" + path[len(self.friendly_path) :]
        elif path_lower.startswith(self.cwd.lower()):
            path = "CWD:" + path[len(self.cwd) :]
        elif path_lower.startswith(self.python.lower()):
            path = "PYTHON_LIB:" + path[len(self.python) :]
        elif path_lower.startswith(self.home.lower()):
            path = "HOME:" + path[len(self.home) :]
        elif path.startswith("<ipython-input"):
            parts = path.split("-")
            path = "In [" + parts[-2] + "]"
        return path


path_utils = PathUtil()


def show_paths():
    """To avoid displaying very long file paths to the user,
    Friendly-traceback tries to shorten them using some easily
    recognized synonyms. This function shows the path synonyms
    currently used.
    """
    print("CWD =", path_utils.cwd)
    print("HOME =", path_utils.home)
    print("FRIENDLY =", path_utils.friendly_path)
    if path_utils.tests is not None:
        print("TESTS =", path_utils.tests)
    print("PYTHON_LIB =", path_utils.python)
