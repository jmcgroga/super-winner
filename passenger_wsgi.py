import sys, os

VENV='/home/sage/venv3'

if VENV is not None:
    INTERP = os.path.join(VENV, 'bin', 'python')
    if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)

from aggredit import app as application
