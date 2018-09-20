# https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d

# Pack
from test1 import *

#Grid
from test2 import *

# Login
from test3 import *

# Class
from test4.test4 import test4

# Menu
from test5 import *

# Toolbar
from test6 import *

# Statusbar
from test7 import *

# MessageBox
from test8 import *

# Shapes and Graphics
from test9 import *


def main():
    choice = 9
    fname = 'test' + str(choice) + '()'
    eval(fname)


main()
