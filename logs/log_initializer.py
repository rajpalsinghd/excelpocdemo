import os
import logging

_here=os.path.dirname(os.path.abspath('app.py'))+"/logs.log"
logging.basicConfig(filename=_here, level=logging.DEBUG)
