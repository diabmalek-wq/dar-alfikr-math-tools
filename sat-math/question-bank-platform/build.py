#!/usr/bin/env python3
"""Build the SAT Aceit question-bank platform into dist/index.html.
Usage: DESMOS_API_KEY=xxxx python3 build.py      (or: python3 build.py --desmos-key xxxx)
The Desmos key is never stored in the repo."""
import json,os,subprocess,sys,pathlib
here=pathlib.Path(__file__).resolve().parent; os.chdir(here)
key=os.environ.get('DESMOS_API_KEY','')
if '--desmos-key' in sys.argv: key=sys.argv[sys.argv.index('--desmos-key')+1]
subprocess.run([sys.executable,'mkbank.py'],check=True)       # tpl_src.html -> bank_template.html
t=open('bank_template.html').read()
assert '</style>' in t
t=t.replace('</style>',open('bld.css').read()+'</style>',1)
boot=("(function(){let p=PRESET;try{const h=location.hash.match(/^#x=(.+)$/);if(h)p=JSON.parse(unb64(h[1]))}catch(e){}\n"
      "  if(p){const ex=examFromPreset(p);if(ex.mods.length){EXAM=ex;resetState()}}})();\nrender();\n})();")
assert "\nrender();\n})();" in t
t=t.replace("\nrender();\n})();","\n"+boot,1)
items=json.load(open('data/bank_all.json'))
data=json.dumps(items,ensure_ascii=False).replace('</','<\\/').replace('<!--','<\\u0021--')
t=t.replace('/*BANK*/[]',data,1).replace('{{TITLE}}','SAT Aceit · Question Bank').replace('{{DESMOS_KEY}}',key)
out=here/'dist'; out.mkdir(exist_ok=True); (out/'index.html').write_text(t)
(out/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: no-referrer\n  X-Robots-Tag: noindex\n')
(out/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('built',len(items),'questions ->',out/'index.html',len(t),'bytes', '(Desmos key set)' if key else '(no Desmos key: set DESMOS_API_KEY)')
