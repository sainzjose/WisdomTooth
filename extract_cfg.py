###############################################################################
# USAGE
# python3 extract_cfg.py path_to_executable 

import r2pipe
import sys 

def extract_cfg(exe_path):
    r2 = r2pipe.open(exe_path)
    r2.cmd('aaa')
    r2.cmd('agCd > output.dot')
    r2.cmd('!!dot -Tpng -o callgraph.png output.dot')

if __name__ == '__main__':
    extract_cfg(sys.argv[1])