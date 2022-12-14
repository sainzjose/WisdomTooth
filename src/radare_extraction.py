import r2pipe

def extract_json_cfg(exe_path):
    r2 = r2pipe.open(exe_path)
    r2.cmd('aaa')
    function_call_graph_json = r2.cmdj('adj')
    return function_call_graph_json
