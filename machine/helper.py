import os


def which(program):
    """
    Find a program on the system path

    Args:
        program (str): the program to be found
    Returns:
        if found the full path to the program, else None
    """

    def is_exe(f):
        return os.path.isfile(f) and os.access(f, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
