print("Sugu M/N?")
sugu=input()

# Collect multi-line input from the user
print("Enter your text (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":  # Stop collecting input when the user enters an empty line
        break
    lines.append(line)
 
# Join all lines into a single string
user_input = " ".join(lines)
 
# Split the input into words and store them in a list
a = user_input.split()

rvbase=0
rvbasex="PUUDU"
if (a.count("RVDd:")>0):
    rvbase=float(a[a.index("RVDd:")+1])
    if (rvbase<4.15):
        rvbasex="normaalse suurusega"
    else:
        rvbasex="dilateerunud"
 
seinapaksusx="PUUDU"
if (a.count("IVSd:")>0 and a.count("LVPWd:")>0):
    ivs=float(a[a.index("IVSd:")+1])
    pwt=float(a[a.index("LVPWd:")+1])
    seinapaksus=float(max(ivs, pwt))
    if (sugu=="m"):
        if (seinapaksus<1.1):
            seinapaksusx="normaalse paksusega"
        elif (seinapaksus<1.35):
            seinapaksusx="kergelt hüpertrofeerunud"
        elif (seinapaksus<1.61):
            seinapaksusx="keskmiselt hüpertrofeerunud"
        else:
            seinapaksusx="raskelt hüpertrofeerunud"
    else:
        if (seinapaksus<1):
            seinapaksusx="normaalse paksusega"
        elif (seinapaksus<1.25):
            seinapaksusx="kergelt hüpertrofeerunud"
        elif (seinapaksus<1.51):
            seinapaksusx="keskmiselt hüpertrofeerunud"
        else:
            seinapaksusx="raskelt hüpertrofeerunud"

edvi=0
edvix="PUUDU"
if (a.count("MODbp/BSA:")>0):
    if (a[a.index("MODbp/BSA:")-1]=="EDV"):
        edvi=float(a[a.index("MODbp/BSA:")+1])
        if (sugu=="m"):
            if (edvi<74.5):
                edvix="normaalse suurusega"
            elif (edvi<89.5):
                edvix="kergelt dilateerunud"
            elif (edvi<100.5):
                edvix="keskmiselt dilateerunud"
            else:
                edvix="raskelt dilateerunud"
        else:
            if (edvi<61.5):
                edvix="normaalse suurusega"
            elif (edvi<70.5):
                edvix="kergelt dilateerunud"
            elif (edvi<80.5):
                edvix="keskmiselt dilateerunud"
            else:
                edvix="raskelt dilateerunud"

lvef=60
lvefx="PUUDU"
if (a.count("EF(MOD-bp):")>0):
    lvef=float(a[a.index("EF(MOD-bp):")+1])
    if (sugu=="m"):
        if (lvef>51.4):
            lvefx="normaalne"
        elif (lvef>40.4):
            lvefx="kergelt langenud"
        elif (lvef>30.4):
            lvefx="keskmiselt langenud"
        else:
            lvefx="raskelt langenud"
    else:
        if (lvef>53.4):
            lvefx="normaalne"
        elif (lvef>40.4):
            lvefx="kergelt langenud"
        elif (lvef>30.4):
            lvefx="keskmiselt langenud"
        else:
            lvefx="raskelt langenud"

tapse=2
rvs=15
if (a.count("TAPSE:"))>0:
    tapse=float(a[a.index("TAPSE:")+1])
 
ivcex="PUUDU"
ivcix="normaalne"
rap=3
if (a.count("Exp:")>0):
    ivce=float(a[a.index("Exp:")+1])
    if (ivce<2.1):
        ivcex="normaalse diameetriga"
    else:
        ivcex="dilateerunud"
    if (a.count("Ins:")>0):
        ivci=float(a[a.index("Ins:")+1])
        if (ivci/ivce>0.5):
            ivcix="vähenenud"
    if (ivcex=="normaalse diameetriga" and ivcix=="normaalne"):
        rap=3
    elif (ivcex=="dilateerunud" and ivcix=="vähenenud"):
        rap=15
    else:
        rap=8
        
laesvi=0
laesvix="PUUDU"
bsa=1.85
if (a.count("Indexed:")>0):
    laesvi=float(a[a.index("Indexed:")+1])
    laesv=float(a[a.index("LAV(MOD-bp):")+1])
    bsa=round(laesv/laesvi, 2)
    if (laesvi<35):
        laesvix="normaalse suurusega"
    elif (laesvi<42):
        laesvix="kergelt dilateerunud"
    elif (laesvi<48):
        laesvix="keskmiselt dilateerunud"
    else:
        laesvix="raskelt dilateerunud"

raesvi=0
raesvix="PUUDU"
if (a.count("volume/BSA:")>0):
    raesvi=float(a[a.index("volume/BSA:")+1])
    if (sugu=="m"):
        if (raesvi<32.5):
            raesvix="normaalse suurusega"
        else:
            raesvix="dilateerunud"
    else:
        if (raesvi<27.5):
            raesvix="normaalse suurusega"
        else:
            raesvix="dilateerunud"
 
rvlongx="PUUDU"
trvel=0
spapx="ei ole hinnatav registreeritava trikuspidaalregurgitatsiooni puudumise tõttu"
vmax=0
pgmean=0
lvotvti=20
raarea=0
mrvc=0
mrpisa=0
mrero=0
mrvol=0
aipht=0
arvc=0
j=0
for i in a:
    if (i=="PG:" and a[j-1]=="mean" and a[j-2]=="Ao"):
        pgmean=float(a[j+1])
    if (i=="VTI:" and a[j-1]=="V1" and a[j-2]=="LV"):
        lvotvti=float(a[j+1])
    if (i=="max:" and a[j-1]=="V2" and a[j-2]=="Ao"):
        vmax=float(a[j+1])
    if (i=="area:" and a[j-1]=="RA"):
        raarea=float(a[j+1])
    if (i=="E'" and a[j-2]=="Lat"):
        elat=float(a[j+2])
    if (i=="E'" and a[j-2]=="Med"):
        emed=float(a[j+2])
    if (i=="vel:" and a[j-1]=="max" and a[j-2]=="TR"):
        trvel=float(a[j+1])
    if (i=="E" and a[j+1]=="max" and a[j-1]=="MV"):
        emax=float(a[j+3])
    if (i=="PG:" and a[j-1]=="max" and a[j-2]=="TR"):
        trpg=float(a[j+1])
        spap=float(trpg+rap)
        if (spap>35.5):
            spapx="arvutuslikult hinnatuna tõusnud, sPAP "+str(round(spap))+" mmHg (TR max PG "+str(round(trpg))+" mmHg + RAP "+str(round(rap))+" mmHg)"
        else:
            spapx="arvutuslikult hinnatuna normaalne, sPAP "+str(round(spap))+" mmHg (TR max PG "+str(round(trpg))+" mmHg + RAP "+str(round(rap))+" mmHg)"
    if (i=="RV" and a[j+1]=="Peak"):
        rvs=float(a[j+4])
        if (tapse>1.69 and rvs>9.4):
            rvlongx="normaalne"
        else:
            rvlongx="langenud"
    if (i=="VC_phl:" and a[j-1]=="MR"):
        mrvc=float(a[j+1])
    if (i=="ERO:" and a[j-1]=="MR"):
        mrero=float(a[j+1])
    if (i=="volume:" and a[j-1]=="MR"):
        mrvol=float(a[j+1])
    if (i=="PISA" and a[j-1]=="MR"):
        mrvol=float(a[j+2])
    if (i=="radius:" and a[j-1]=="PISA" and a[j-2]=="MR"):
        mrpisa=float(a[j+1])
    if (i=="P1/2t:" and a[j-1]=="AI"):
        aipht=float(a[j+1])
    if (i=="VC:" and a[j-1]=="AR"):
        arvc=float(a[j+1])
    j=j+1

k=0
mpapx=""
pvx=" funktsioon normis"
for i in a:
    if (i=="PG:" and a[k-1]=="max" and a[k-2]=="PI"):
        prpg=float(a[k+1])
        pvx="l kerge regurgitatsioon"
        if (spapx=="ei ole hinnatav registreeritava trikuspidaalregurgitatsiooni puudumise tõttu"):
            mpap=float(prpg+rap)
            if (mpap>20.5):
                mpapx="Kopsuringe keskmine rõhk tõusnud, mPAP "+str(round(mpap))+" mmHg (PR max PG "+str(round(prpg))+" mmHg + RAP "+str(round(rap))+" mmHg). "
            else:
                mpapx="Kopsuringe keskmine rõhk normaalne, mPAP "+str(round(mpap))+" mmHg (PR max PG "+str(round(prpg))+" mmHg + RAP "+str(round(rap))+" mmHg). "
    k=k+1

dvi=1
ava=2
if (a.count("DVI:")>0):
    dvi=float (a[a.index("DVI:")+1])
if (a.count("AVA(I,D):")>0):
    ava=float (a[a.index("AVA(I,D):")+1])

aort="Aort PUUDU"
if (a.count("asc")>0 and (a.count("sinus")>0 or (a.count("root")>0))):
    asc=float (a[a.index("asc")+3])
    if (a.count("root")>0):
        sinus=float(a[a.index("root")+2])
    if (a.count("sinus")>0):
        sinus=float (a[a.index("sinus")+2])
    if (asc>(0.727273*bsa + 2.65455) and sinus>(0.727273*bsa + 2.65455)):
        aort="Aordi bulbus ("+str(sinus)+" cm) ja astsendeeruv aort ("+str(asc)+" cm) on dilateerunud"
    elif (asc>(0.727273*bsa + 2.65455) and sinus<(0.727273*bsa + 2.65455)):
        aort="Aordi bulbus normaalse diameetriga, astsendeeruv aort on dilateerunud ("+str(asc)+" cm)"
    elif (asc<(0.727273*bsa + 2.65455) and sinus>(0.727273*bsa + 2.65455)):
        aort="Aordi bulbus dilateerunud ("+str(sinus)+" cm), astsendeeruv aort normaalse diameetriga"
    else:
        aort="Aordi bulbus ja astsendeeruv aort normaalse diameetriga"
if (a.count("asc")==0 and (a.count("sinus")>0 or (a.count("root")>0))):
    if (a.count("root")>0):
        sinus=float(a[a.index("root")+2])
    if (a.count("sinus")>0):
        sinus=float (a[a.index("sinus")+2])
    if (sinus>(0.727273*bsa + 2.65455)):
        aort="Aordi bulbus ("+str(sinus)+" cm) on dilateerunud, astsendeeruv aort adekvaatselt ei visualiseeru"
    else:
        aort="Aordi bulbus on normaalse diameetriga, astsendeeruv aort adekvaatselt ei visualiseeru"

facx="visuaalselt normis"
if (a.count("FAC:")>0):
    fac=float (a[a.index("FAC:")+1])
    if (fac<35):
        facx="langenud (FAC "+str(round(fac))+"%)"
    else:
        facx="normis (FAC "+str(round(fac))+"%)"
ea=0
if (a.count("E/A:")>0):
    ea=float (a[a.index("E/A:")+1])
 
diastx="PUUDU"
if (a.count("E/lat")>0 and a.count("E/med")>0):
    eelat=float (a[a.index("E/lat")+2])
    eemed=float (a[a.index("E/med")+2])
    eesuhe=(eelat+eemed)/2
    h= 0
    if (lvefx=="normaalne"):
        if (eesuhe>14):
            h=h+1
        if (elat<10 or emed<7):
            h=h+1
        if (trvel>280):
            h=h+1
        if (laesvi>34):
            h=h+1
        if (h<2):
            diastx="funktsioon normis"
        elif (h>2):
            diastx="düsfunktsioon"
        else:
            diastx="funktsioon ei ole hinnatav"
    else:
        if (ea>1.99):
            diastx="düsfunktsioon koos rõhu tõusuga vasakus kojas, viited restriktiivsele täitumisele"
        elif (ea<0.81 and ea>0 and emax<51):
            diastx="düsfunktsioon ilma rõhu tõusuta vasakus kojas"
        else:
            if (eesuhe>14):
                h=h+1
            if (trvel>280):
                h=h+1
            if (laesvi>34):
                h=h+1
            if (h>1):
                diastx="düsfunktsioon koos rõhu tõusuga vasakus kojas"
            elif (h<1):
                diastx="düsfunktsioon ilma rõhu tõusuta vasakus kojas"
            else:
                if (trvel>0):
                    diastx="düsfunktsioon ilma rõhu tõusuta vasakus kojas"
                else:
                    diastx="funktsioon ei ole hinnatav"

asx="klapi funktsioon normis"
if (vmax>399.9 or pgmean>39.9 or ava<1.0 or dvi<0.25):
    asx="klapil raske stenoos (v(max) "+str(round(vmax/100, 1))+" m/s, PGmean "+str(round(pgmean))+" mmHg, AVA "+str(ava)+" cm², DVI "+str(dvi)+")"
elif (vmax>299.9 or pgmean>19.9 or ava<1.51 or dvi<0.51):
    asx="klapil keskmise raskusega stenoos (v(max) "+str(round(vmax/100, 1))+" m/s, PGmean "+str(round(pgmean))+" mmHg, AVA "+str(ava)+" cm², DVI "+str(dvi)+")"
elif (vmax>254.9):
    asx="klapil kerge stenoos (v(max) "+str(round(vmax/100, 1))+" m/s, PGmean "+str(round(pgmean))+" mmHg, AVA "+str(ava)+" cm², DVI "+str(dvi)+")"

aix=""
if (aipht>0):
    if (asx=="klapi funktsioon normis"):
        if (aipht<200 or arvc>0.6):
            asx="klapil stenoosi ei esine, raske regurgitatsioon (VC laius "+str(arvc)+" cm, PHT "+str(round(aipht))+" ms)"
        elif (aipht<500 or arvc>0.3):
            asx="klapil stenoosi ei esine, keskmise raskusega regurgitatsioon (VC laius "+str(arvc)+" cm, PHT "+str(round(aipht))+" ms)"
        else:
            asx="klapil stenoosi ei esine, kerge tsentraalne regurgitatsioon"
    else:
        if (aipht<200 or arvc>0.6):
            aix=" ning raske regurgitatsioon (VC laius "+str(arvc)+" cm, PHT "+str(round(aipht))+" ms)"
        elif (aipht<500 or arvc>0.3):
            aix=" ning keskmise raskusega regurgitatsioon (VC laius "+str(arvc)+" cm, PHT "+str(round(aipht))+" ms)"
        else:
            aix=" ning kerge tsentraalne regurgitatsioon"

mrx="minimaalne regurgitatsioon"
if (mrvc>0.69 or mrpisa>0.99 or mrero>0.39 or mrvol>59.9):
    mrx="raske regurgitatsioon (VC laius "+str(mrvc)+" cm, PISAr "+str(mrpisa)+" cm, ERO "+str(mrero)+" cm²)"
elif (mrvc>0.30 or mrpisa>0.3 or mrero>0.19 or mrvol>29.9):
    mrx="keskmine regurgitatsioon (VC laius "+str(mrvc)+" cm, PISAr "+str(mrpisa)+" cm, ERO "+str(mrero)+" cm²)"

rrx="Kodade virvendusarütmia  x'"
if (a.count("R-R:")>0):
    rr=float (a[a.index("R-R:")+1])
    esimene=int(round(round(60/rr, -1)))
    if (esimene>60/rr):
        teine=int(esimene-5)
    else:
        teine=int(esimene+5)
    rrx="Siinusrütm "+str(min(esimene, teine))+"-"+str(max(esimene, teine))+" x'"

straintekst=""
glsx=""
if (a.count("GLS_Endo_Peak_Avg:")>0):
    gls=float (a[a.index("GLS_Endo_Peak_Avg:")+1])
    straintekst=straintekst+" + LV strain"
    if (gls<-18):
        glsx="Vasaku vatsakese globaalne longitudinaalne venitatavus ehk GLS on normis ("+str(gls)+"%). "
    elif (gls<-16):
        glsx="Vasaku vatsakese globaalne longitudinaalne venitatavus ehk GLS on kergelt langenud ("+str(gls)+"%). "
    else:
        glsx="Vasaku vatsakese globaalne longitudinaalne venitatavus ehk GLS on langenud ("+str(gls)+"%). "

rvstrainx=""
if (a.count("RVFWSL:")>0):
    rvstrain=float (a[a.index("RVFWSL:")+1])
    straintekst=straintekst+" + RV strain"
    if (rvstrain<-18):
        rvstrainx="Parema vatsakese vabaseina strain on normis ("+str(rvstrain)+"%)."
    elif (rvstrain<-16):
        rvstrainx="Parema vatsakese vabaseina strain on kergelt langenud ("+str(rvstrain)+"%)."
    else:
        rvstrainx="Parema vatsakese vabaseina strain on langenud ("+str(rvstrain)+"%)."
        
lastrainx=""
if (a.count("LASrED:")>0):
    lastrain=float (a[a.index("LASrED:")+1])
    straintekst=straintekst+" + LA strain"
    if (lastrain<20):
        lastrainx="Vasaku koja strain oluliselt langenud ("+str(lastrain)+"%)."
        diastx="düsfunktsioon koos rõhu tõusuga vasakus kojas"
    elif (lastrain<35):
        lastrainx="Vasaku koja strain on langenud ("+str(lastrain)+"%)."
        diastx="düsfunktsioon ilma rõhu tõusuta vasakus kojas"
    else:
        lastrainx="Vasaku koja strain on normis ("+str(lastrain)+"%)."
        
        
print("""Täismahus ehhokardiograafia"""+straintekst+""".
 
Suboptimaalne nähtavus. """+rrx+""".
 
Vasaku vatsakese õõs """ + edvix + """ (EDV MODbp/BSA """+str(round(edvi))+""" ml/m²), müokard """+seinapaksusx+""". Üldine süstoolne funktsioon on """ + lvefx + """, EF bp """ + str(round(lvef)) + """%, LVOT VTI """ + str(round(lvotvti)) + """ cm. """+ glsx +"""Segmentaarset kineetikahäiret ei tähelda.
Diastoolne """+diastx+""". """+lastrainx+"""
 
Parem vatsake on """+rvbasex+""", basaalne diameeter """+str(rvbase)+""" cm. Longitudinaalne süstoolne funktsioon """+rvlongx+""" (TAPSE """+str(round(tapse,1))+""" cm, RV S' """+str(rvs)+""" cm/s), tsirkulaarne süstoolne funktsioon """+facx+""". """+rvstrainx+"""
Kopsuringe süstoolne rõhk """+spapx+""". """+mpapx+"""
Alumine õõnesveen """+ivcex+""", respiratoorne reaktiivsus """+ivcix+""".
Vasak koda on """+laesvix+""" (LAESVi """+str(round(laesvi))+""" ml/m²). Parem koda on """+raesvix+""" (RAESVi """+str(round(raesvi))+""" ml/m², RA pindala """+str(round(raarea))+""" cm²).
Kodade vaheseinas šundivoolu ei visualiseeru.
 
Aordiklapp on trikuspiidne, struktuur iseärasusteta, """+asx+aix+""".
"""+aort+""".
Pulmonaalklapi"""+pvx+""".
Mitraalklapi struktuur iseärasusteta, """+mrx+""".
Trikuspidaalklapi struktuur iseärasusteta, minimaalne regurgitatsioon.
 
Perikardiõõnes liigset vedelikku ei ole.
""")