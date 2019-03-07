#The gentle Giant








myname=input('Eu sunt Povestitorul, cum te numesti?')
    
       
    
print('In aceasta calatorie, '+myname+' va pleca spre taramul gigantilor')
          
print('Dupa o lunga catarare pe vrejul de fasole ai ajuns in \"Orasul Norilor\"')

print('In fata se vede un castel, la stanga este o coliba, iar la dreapta este o padure')

print('Pentru a merge spre castel apasa "a"')

print ('Pentru a merge spre coliba apasa "b"')

print('Pentru a merge in padure apasa "c"')

opt1=input()

if opt1=='a':
    print('Ai ales sa mergi spre castel... dupa urcarea celor 201 trepte te uimeste marimea castelului')

if opt1=='b':
    print('Coliba pare mult mai mare de aproape decat de la distanta si incepi sa te intrebi ce inaltime ar putea avea locuitorii ei')

if opt1=='c':
    print('In padure se aud tot felul de zgomote ciudate parca de pe alta lume')

while opt1=='a':
    print('Usile imense sunt interdeschise si te-ai putea strecura printre ele, sau ai putea sa cercetezi mai bine intrarea')
    opta2=input('Tasteaza "da" pentru a intra in castel, sau "nu" pentru a cerceta imprejurimile')

    if opta2=='da':
        print('Bogatiile castelului se vad inca de al intrare')
        opta3=input('Vrei sa faci o baie de monezi de aur si nestemate/(da/nu)')

        if opta3=='da':
            print('Aruncandu-te in marea de bogatii nu ti-ai dat seama ca nu stii sa inoti si te-ai inecat')
            break

        if opta3=='nu':
            print('Auzi niste pasi venind spre tine. Ce faci, fugi? (da/nu)')
            opta4=input()

        if opta4=='nu':
            print('Stand tintuit observi cu groaza cum un gigant flamand vine spre tine...\nTe inhata intre degete si te haleste dintr-o inghititura')
            break

        if opta4=='da':
                print('Ai reusit sa gasesti o patura sub care sa te ascunzi si prin care poti vedea un pic ce se intampla in camera')
                print('Pasii se aud din ce in ce mai aproape si incepe sa se contureze silueta unui gigant')
                opta5=input('Nu-ti vine sa crezi ca-ti vine sa stranuti, ce faci te tii de nas?(da/nu)')
        if opta5=='da':
            print('Tinandu-te de nas nu mai poti sa respiri si incepi sa te sufoci...')
            print('Tragi aer in piept dar te ineci si incepe o tuse zgomotoasa')
            print('Gigantul te aude si ridica patura si te MANANCA !!!\n:))))')
            break

        if opta5=='nu':
            print('Ai stranutat si gigantul te-a prins si te-a macat...\nDAR, cred ca te asteptai la asta')
            break
            

    if opta2=='nu':
        print('Cercetand indeaproape locul in care te aflii ai observat intr-un colt o cusca de dimensiunea unui om in care se afla o roata de cascaval')
        opta6=input('Iti dai seama ca nu ai mancat de cand ai plecat spre acest taram\nVrei sa ciugulesti ceva inainte de a merge mai departe?(da/nu)')

    if opta6=='da':
        print('Rupand o bucata din cascaval s-a declansat o capcana care te-a tras in teapa\nFinal tragic varianta 1')
        break
    
    if opta6=='nu':
        print('Nu mai este nimic altceva in jur poti sa mergi mai departe')
        continue

while opt1=='b':
    print("Usa colibei este inchisa cu cheia.")
    optb2=input('Tasteaza da pentru a bate la usa sau nu pentru a cerceta imprejur.')

    if optb2=='da':
        print("Batand la usa alarmezi stapanii casei, niste giganti infricosatori care te prind si te mananca.")
        break

    if optb2=='nu':
        print("Cautand imprejurimile te impiedici de o piatra din pavaj si observi sub ea o cheie.")
        optb3=input("Deschizi usa si in coliba sta intr-o colivie de aur o rata salbatica gigant. Te duci sa o eliberezi? da/nu")

        if optb3=="da":
            print("Ajungand la rata observi ca ea sta pe niste oua de aur. Le indesi in tolba si nu te poti abtine sa chiui de fericire.")
            optb4=input("Pe usa intra un gigant inebunit ca vrei sa-i furi rata.Fugi printre picioarele lui? da/nu?")

        if optb4=="da":
            print("Fiindca gigantul se apleca incet resesti sa te strecori printre picioarele lui.")
            print("Rata salbatica cum vazu lumina zilei incepe sa-si ia avant sa zboare.")
            print("Te apuci de picioarele ei si porniti in zbor spre casa.")
            print("Ai castigat Rata cu Ouale de Aur!!!")
            break

        if optb4=="nu":
            print("Alergi prin coliba incercand sa te ascunzi de gigant dar acesta este mult mai iute de picior decat tine si te prinde si te arunca in oala cu ciorba de legume de pe foc.")
            break
    
while opt1=='c':
    print('In padure se aud zgomote ciudate de animale si este foarte intunecat.')
    print('Te sperie o perfeche de ochi infircosatori care se uita la tine si fugi spre un luminis unde gasesti o coliba.')

    print("Usa colibei este inchisa cu cheia.")
    optb2=input('Tasteaza da pentru a bate la usa sau nu pentru a \n cerceta imprejur.')

    if optb2=='da':
        print("Batand la usa alarmezi stapanii casei, niste giganti infricosatori care te prind si te mananca.")
        break

    if optb2=='nu':
        print("Cautand imprejurimile te impiedici de o piatra din pavaj si observi sub ea o cheie.")
        optb3=input("Deschizi usa si in coliba sta intr-o colivie de aur o rata salbatica gigant. Te duci sa o eliberezi?\n da/nu")

        if optb3=="nu":
            print("Povestitorul nu prea se baga in actiune, \n dar acuma o sa intervin... \n Esti nebun? \n Cum sa nu eliberezi rata?\n Gata te scot din povestea mea. \n Povestitorul te-a sters din poveste deci in traducere libera nu mai am idei cum sa te omor.")
            break
        if optb3=="da":
            print("Ajungand la rata observi ca ea sta pe niste oua de aur. Le indesi in tolba si nu te poti abtine sa chiui de fericire.")
            optb4=input("Pe usa intra un gigant inebunit ca vrei sa-i furi rata.Fugi printre picioarele lui? da/nu?")

        if optb4=="da":
            print("Fiindca gigantul se apleca incet resesti sa te strecori printre picioarele lui.")
            print("Rata salbatica cum vazu lumina zilei incepe sa-si ia avant sa zboare.")
            print("Te apuci de picioarele ei si porniti in zbor spre casa.")
            print("Ai castigat Rata cu Ouale de Aur!!!")
            break

        if optb4=="nu":
            print("Alergi prin coliba incercand sa te ascunzi de gigant dar acesta este mult mai iute de picior decat tine si te prinde si te arunca in oala cu ciorba de legume de pe foc.")
            break


        
