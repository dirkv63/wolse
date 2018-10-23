"""
This script will take a backup of the neo4j database.
"""

import logging
import os
import subprocess as sp
from lib import my_env

cfg = my_env.init_env("wolse", __file__)

cmd = os.path.join(cfg["Graph"]["path"], cfg["Graph"]["adm"])
db = cfg["Graph"]["db"]
dbname = db.split(".")[0]
dumpname = "{dbname}.dump".format(dbname=dbname)
dumpffp = os.path.join(cfg["Graph"]["dumpdir"], dumpname)
args = [cmd, "dump", "--database={db}".format(db=db), "--to={dumpffp}".format(dumpffp=dumpffp)]

module = my_env.get_modulename(__file__)
sof = os.path.join(cfg["Main"]["logdir"], "{mod}_out.log".format(mod=module))
sef = os.path.join(cfg["Main"]["logdir"], "{mod}_err.log".format(mod=module))
so = open(sof, "w")
se = open(sef, "w")
logging.info("Command: {c}".format(c=args))
try:
    sp.run(args, stderr=se, stdout=so, check=True)
except sp.CalledProcessError as e:
    logging.error("Some issues during execution, check {sef} and {sof}".format(sof=sof, sef=sef))
else:
    logging.info("No error messages returned, see {sof}!".format(sof=sof))
se.close()
so.close()
