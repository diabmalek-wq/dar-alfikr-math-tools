import zipfile,re,sys
src,dst=sys.argv[1],sys.argv[2]
T=('<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
'<mc:Choice xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main" xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" Requires="p159">'
'<p:transition spd="slow" p14:dur="1600"><p159:morph option="byObject"/></p:transition></mc:Choice>'
'<mc:Fallback><p:transition spd="slow"><p:fade/></p:transition></mc:Fallback></mc:AlternateContent>')
zi=zipfile.ZipFile(src); zo=zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED)
for it in zi.infolist():
    d=zi.read(it.filename); m=re.match(r'ppt/slides/slide(\d+)\.xml$',it.filename)
    if m and int(m.group(1))>=2:
        x=d.decode('utf8'); assert '</p:clrMapOvr>' in x; d=x.replace('</p:clrMapOvr>','</p:clrMapOvr>'+T,1).encode('utf8')
    zo.writestr(it,d)
zo.close()
