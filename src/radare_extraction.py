import r2pipe

import r2pipe
r2 = r2pipe.open("/bin/ls")
r2.cmd("aaa") # See radare.today/posts/analysis-by-default/
function_call_graph_json = r2.cmdj("agj")
