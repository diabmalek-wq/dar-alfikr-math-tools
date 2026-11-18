"""SAT stays international: replace Saudi settings, currency and names in the SAT bank (mock page source)."""
import re,json,sys,random
P='/home/claude/v2/site/sat/mock/index.html'
R=[  # (regex, replacement) applied in order to every string
 (r'\\text\{SAR \}', r'\\$'), (r'\\text\{ SAR\}', r'\\text{ dollars}'),(r'\\text\{SAR\}', r'\\text{dollars}'),
 (r'\bSAR \$', r'$\\$'),
 (r'\$([^$]+)\$ SAR\b', r'$\\$\1$'),
 (r'(\d[\d,.]*) SAR\b', r'\1 dollars'),
 (r'\bthousand SAR\b','thousand dollars'),(r'\bmillion SAR\b','million dollars'),(r'\bmillions of SAR\b','millions of dollars'),
 (r'\bSAR\b','dollars'),(r'\bRiyals\b','Dollars'),(r'\briyals\b','dollars'),(r'\briyal\b','dollar'),(r'\bhalalas\b','cents'),(r'\bhalala\b','cent'),
 (r'\bSaudi VAT\b','a sales tax'),(r'\bVAT\b','sales tax'),
 (r'\bnon-Saudi\b','part-time'),(r'\bis Saudi\b','is full-time'),(r'\$ Saudi and\b','$ full-time and'),(r'\bSaudi employees\b','full-time employees'),(r'\bSaudi exchange\b','stock exchange'),
 (r'\bSaudi Pro League\b','national soccer league'),(r'\bSaudi league\b','national league'),(r'\bSaudi Arabian\b','national'),(r'\bSaudi Arabia\b','the country'),(r'\bin Saudi\b','in the country'),(r'\bSaudi\b','national'),
 (r'\bSaudi (?=[a-z])',''),
 (r'\bthe Kingdom\b','the country'),(r'\bKingdom\b','country'),
 (r'\bJeddah Corniche\b','city waterfront'),(r'\bJeddah corniche\b','waterfront'),(r'\b[Cc]orniche\b','waterfront'),
 (r'\b(a|A) (Riyadh|Jeddah) Season\b',r'\1 winter festival'),(r'\bRed Sea coastal\b','coastal'),(r'\ban (AlUla|Al-Ula)\b','a Canyon Ridge'),(r'\bA Haramain\b','An intercity'),(r'\ba Haramain\b','an intercity'),(r'\bthe Asir\b','the highland'),
 (r'\b(Riyadh|Jeddah) Season\b','the winter festival season'),
 (r'\bKing Abdulaziz International Airport\b','Lakeview International Airport'),(r'\bKing Abdullah Port\b','Bayside Port'),(r'\bKing Abdullah Sports City\b','City Stadium'),(r'\bKing Abdullah\b','Kingsley'),(r'\bKing Abdulaziz\b','Kingsley'),(r'\bKing Fahd\b','Kingsley'),
 (r'\bKAUST\b','a research university'),
 (r'\bHaramain\b','intercity'),
 (r'\bin NEOM\b','in a new smart city'),(r'\bat NEOM\b','at a new smart city'),(r'\bNEOM\'s\b',"the smart city's"),(r'\bfor NEOM\b','for a new smart city'),(r'\bof NEOM\b','of a new smart city'),(r'\bNEOM\b','smart-city'),
 (r'\bRed Sea giga-project\b','coastal mega-project'),(r'\bRed Sea coast\b','coast'),(r'\bRed Sea coastline\b','coastline'),(r'\bthe Red Sea\b','the sea'),(r'\ba Red Sea\b','a coastal'),(r'\bRed Sea\b','coastal'),
 (r'\bVision 2030\b','national'),
 (r'\bRamadan food\b','holiday food'),(r'\bShaaban\b','November'),(r'\bRamadan\b','December'),(r'\bHajj-season\b','holiday-season'),(r'\bHajj\b','holiday'),(r'\bUmrah\b','tourist'),(r'\bEid\b','holiday'),
 (r'\bpilgrims\b','visitors'),(r'\bpilgrim\b','visitor'),
 (r'\bmosque prayer hall\b','concert hall'),(r'\bmosque courtyard\b','museum courtyard'),(r'\bmosque survey\b','community-center survey'),(r'\bA mosque\b','A museum'),(r'\ba mosque\b','a museum'),(r'\bmosque\b','museum'),(r'\bprayer rug\b','rug'),(r'\bprayer hall\b','hall'),
 (r'\bmajlis\b','pavilion'),(r'\bthobe\b','jacket'),(r'\bqahwa\b','coffee'),(r'\bArabic coffee\b','coffee'),(r'\bSTC\b','TelcoNet'),
 (r'\bSukkari\b','Medjool'),(r'\bAjwa\b','Deglet Noor'),(r'\bKhalas\b','Barhi'),
 (r'\bJeddah\b','Bayview'),(r'\bRiyadh\b','Riverton'),(r'\bMakkah\b','Fairview'),(r'\bMecca\b','Fairview'),(r'\bMadinah\b','Oakdale'),(r'\bMedina\b','Oakdale'),(r'\bDammam\b','Westport'),(r'\bKhobar\b','Eastport'),(r'\bDhahran\b','Eastfield'),
 (r'\bYanbu\b','Harbor City'),(r'\bJubail\b','Portside'),(r'\bAbha\b','Highland'),(r'\bTaif\b','Hillcrest'),(r'\bTabuk\b','Northfield'),(r'\bJazan\b','Southport'),(r'\bAl-?Ula\b','Canyon Ridge'),(r'\bAlUla\b','Canyon Ridge'),(r'\bDiriyah\b','Old Town'),(r'\bQassim\b','Greenfield'),(r'\bAsir\b','the highland'),(r'\bAl Ahsa\b','Palm Valley'),
 # names (gender kept)
 (r'\bLayla\b','Lena'),(r'\bKhalid\b','Kevin'),(r'\bFaisal\b','Felix'),(r'\bYousef\b','Jason'),(r'\bOmar\b','Owen'),(r'\bNoura\b','Nora'),(r'\bSalma\b','Sophie'),(r'\bTariq\b','Tom'),(r'\bReem\b','Rachel'),(r'\bHuda\b','Hannah'),(r'\bSalem\b','Sam'),(r'\bHamad\b','Henry'),(r'\bFahad\b','Frank'),(r'\bZiad\b','Zack'),(r'\bMaha\b','Maya'),(r'\bAbdullah\b','Adam'),(r'\bHind\b','Helen'),(r'\bAbdulaziz\b','Alex'),
]
R=[(re.compile(a),b) for a,b in R]
LEFT=re.compile(r'\b(SAR|Saudi|Riyadh|Jeddah|Makkah|Madinah|NEOM|riyals?|halalas?|Ramadan|Hajj|Haramain|Kingdom|Vision 2030|Corniche|Sukkari|Ajwa|Khalas|majlis|thobe|mosque|Layla|Khalid|Faisal|Yousef|Noura|Salma|Tariq|Reem|Huda|Hamad|Fahad|Ziad|Abdullah|Shaaban|Eid)\b')
def fix(s):
    for a,b in R: s=a.sub(b,s)
    return s
def walk(o):
    if isinstance(o,str): return fix(o)
    if isinstance(o,list): return [walk(x) for x in o]
    if isinstance(o,dict): return {k:(walk(v) if k not in ('id','domain','skill','sub','lv') else v) for k,v in o.items()}
    return o
if __name__=='__main__':
    h=open(P,encoding='utf8').read()
    m=re.search(r'(<script type="application/json" id="bankdata">)(.*?)(</script>)',h,re.S)
    items=json.loads(m.group(2)); new=[walk(i) for i in items]
    changed=[(a,b) for a,b in zip(items,new) if a!=b]
    print('changed items',len(changed))
    left=[(b['id'],x) for b in new for x in LEFT.findall(json.dumps(b,ensure_ascii=False))]
    print('leftover',len(left),left[:20])
    random.seed(4)
    for a,b in random.sample(changed,12): print('\n',a['id'],'\n  -',a['q'][:220],'\n  +',b['q'][:220], '\n  opts', b.get('opts'))
    if 'write' in sys.argv:
        js=json.dumps(new,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
        open(P,'w',encoding='utf8').write(h[:m.start(2)]+js+h[m.end(2):]); print('written')
