"""
This script will find all Nodes in a graph and add a nid (uuid(4)) to it. The Neo4J unique identifier for nodes cannot
be used as the identifier will be reused when nodes are replaced. Also py2neo is not very good in supporting the Neo4J
unique identifier.
"""

from competition import neostore
from lib import my_env

if __name__ == "__main__":
    my_env.init_loghandler(__file__, "c:\\temp\\log", "info")
    ns = neostore.NeoStore()
    res = ns.get_nodes_no_nid()
    print("Nodes updated: {r}".format(r=res))
