import sys,json
from collect import collect,key
from mathgen import render
cfg=json.load(open(sys.argv[1])); out=sys.argv[2] if len(sys.argv)>2 else "m_"+cfg["id"]
E=collect(cfg); render(E,"t_"+cfg["id"],out); print(len(E),"expressions")
