import pygame
import random



pygame.init()

wymiar_szer = 800
wymiar_wys = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gamedisp = pygame.display.set_mode((wymiar_szer, wymiar_wys))
pygame.display.set_caption('jamnik w wannie')
zegar = pygame.time.Clock()

snek_faceN = pygame.image.load('snek_headN.png')
snek_faceE = pygame.image.load('snek_headE.png')
snek_faceS = pygame.image.load('snek_headS.png')
snek_faceW = pygame.image.load('snek_headW.png')
ogonN=pygame.image.load('ogonN.png')
ogonE=pygame.image.load('ogonE.png')
ogonS=pygame.image.load('ogonS.png')
ogonW=pygame.image.load('ogonW.png')
cialo21=pygame.image.load('Cialo21.png')
cialo22=pygame.image.load('Cialo22.png')
cialo23=pygame.image.load('Cialo23.png')
cialo24=pygame.image.load('Cialo24.png')
cialo31=pygame.image.load('cialo31.png')
cialo32=pygame.image.load('cialo32.png')

Background = pygame.image.load('Background.png')
Wall = pygame.image.load('Wall.png')
Groszek = pygame.image.load('Groszek.png')
#Cialo = pygame.image.load('Cialo.png')

czcionka=pygame.font.SysFont("comicsansms", 25)
czcionkaduza=pygame.font.SysFont("comicsansms", 100)

scianyx=[]
scianyy=[]
cialox=[]
cialoy=[]
kierunki=['N']
dlugosc=1

def snek_begin(x, y, kier):

    if kier == 'N':
        gamedisp.blit(snek_faceN, (x, y))
    elif kier == 'E':
        gamedisp.blit(snek_faceE, (x, y))
    elif kier == 'S':
        gamedisp.blit(snek_faceS, (x, y))
    else:
        gamedisp.blit(snek_faceW, (x, y))



def wczytaj_mape(plik):
    with open("mapa1.txt", "r") as zawart:
        linie = []
        for linia in zawart:
            linie.append(str.split(linia))

        return linie

def mapa(linie):
    for y in range(0,len(linie)):
        talinia=linie[y]
        for x in range(0,len(talinia)):
            kafelek=talinia[x]
            if(kafelek=='0'):
                gamedisp.blit(Background, ((x*40),(y*40)))


            if (kafelek == '1'):
                gamedisp.blit(Wall, ((x * 40), (y * 40)))
                scianyx.append((x * 40))
                scianyy.append((y * 40))

def zaginanie(kierunekprzed,kierunek,indexkierunku, dlugoscweza,x,y):


    if(indexkierunku==1):
        if(kierunek=='N'):
            #return "ogonN"
            gamedisp.blit(ogonN,((x,y)))
        if (kierunek == 'E'):
            #return "ogonE"
            gamedisp.blit(ogonE, ((x, y)))
        if (kierunek == 'S'):
            #return "ogonS"
            gamedisp.blit(ogonS, ((x, y)))
        if (kierunek == 'W'):
            #return "ogonW"
            gamedisp.blit(ogonW, ((x, y)))
    elif(kierunek==kierunekprzed):
        if(kierunek=='N' or kierunek=='S'):
            #return "cialo31"
            gamedisp.blit(cialo31, ((x, y)))
        else:
            #return "cialo32"
            gamedisp.blit(cialo32, ((x, y)))
    else:
        if(kierunek=='N'):
            if(kierunekprzed=='W'):
                #return "cialo23"
                gamedisp.blit(cialo23, ((x, y)))
            else:
                #return "cialo22"
                gamedisp.blit(cialo24, ((x, y)))
        elif(kierunek=='E'):
            if(kierunekprzed=='N'):
                #return "cialo21"
                gamedisp.blit(cialo21, ((x, y)))
            else:
                #return "cialo23"
                gamedisp.blit(cialo23, ((x, y)))
        elif (kierunek == 'S'):
            if (kierunekprzed == 'E'):
                #return "cialo21"
                gamedisp.blit(cialo22, ((x, y)))
            else:
                #return "cialo22"
                gamedisp.blit(cialo21, ((x, y)))
        else:
            if (kierunekprzed == 'N'):
                #return "cialo23"
                gamedisp.blit(cialo22, ((x, y)))
            else:
                #return "cialo24"
                gamedisp.blit(cialo24, ((x, y)))


def pokazwynik(wynik):
    punkty=czcionka.render("Wynik: "+str(wynik),1, black)
    gamedisp.blit(punkty, [0,0])


def ekranstart(pocz):

    while(pocz==True):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
    gamedisp.fill(white)
    napis=czcionkaduza.render("jamnik w wannie",1,black)
    napis2=czcionka.render("nacisnij jakikolwiek przycisk",1,black)
    gamedisp.blit(napis,(400,400))
    gamedisp.blit(napis2,(600,400))
    if event.type == pygame.KEYDOWN:
        pocz=False



x=160
y=320

przegranko = False
zebrano=True

score=0
kierunek='N'

tamapa="mapa1.txt"

mapa(wczytaj_mape(tamapa))

mapkax = []
mapkay = []

for i in range(0, len(wczytaj_mape(tamapa))):
    for j in range(0, len(wczytaj_mape(tamapa)[i])):
        mapkax.append(j * 40)
        mapkay.append(i * 40)
for i in range(0, len(mapkax)):
    for j in range(0, len(scianyx)):
        if (i < len(mapkax) and j < len(scianyx) and mapkax[i] == scianyx[j] and mapkay[i] == scianyy[j]):
            mapkax.pop(i)
            mapkay.pop(i)

print("dlx "+str(len(scianyx)))
print("dly "+str(len(scianyy)))
print("dlxm "+str(len(mapkax)))
print("dlym "+str(len(mapkay)))

pocz=True

while not przegranko:
    zmiana=False

    for event in pygame.event.get():



        if event.type == pygame.QUIT:
            przegranko = True
        if event.type == pygame.KEYDOWN:
            zmiana = True
            if event.key == pygame.K_LEFT:

                if kierunek== 'N':
                    kierunek = 'W'
                    kierunki.append('W')

                elif kierunek == 'E':
                    kierunek= 'N'
                    kierunki.append('N')
                elif kierunek == 'S':
                    kierunek = 'E'
                    kierunki.append('E')
                elif kierunek == 'W':
                    kierunek ='S'
                    kierunki.append('S')
            elif event.key == pygame.K_RIGHT:
                if kierunek== 'N':
                    kierunek='E'
                    kierunki.append('E')

                elif kierunek == 'E':
                    kierunek='S'
                    kierunki.append('S')
                elif kierunek == 'S':
                    kierunek='W'
                    kierunki.append('W')
                elif kierunek == 'W':
                    kierunek='N'
                    kierunki.append('N')
    print(event)
    print(kierunek)



    if (zmiana==False):
        kierunki.append(kierunki[len(kierunki)-1])

    gamedisp.fill(white)

    mapka=wczytaj_mape(tamapa)




    mapa(wczytaj_mape(mapka))





    if(kierunek== 'N'):
        y=y-40
    if(kierunek== 'E'):
        x=x+40
    if (kierunek == 'S'):
        y = y + 40
    if (kierunek == 'W'):
        x=x- 40

    if (x > 760):
        x = 0
    if (y > 760):
        y = 0
    if (x < 0):
        x = 760
    if (y < 0):
        y = 760
    print(str(x)+" "+str(y))

    # generacja groszka
    if (zebrano == True):

        score=score+1
        mapkaxteraz = mapkax[:]
        mapkayteraz = mapkay[:]



        for i in range(0, len(mapkaxteraz)):
            for j in range(0, len(cialox)):
                if (i < len(mapkaxteraz) and j < len(cialox) and mapkaxteraz[i] == cialox[j] and mapkayteraz[i] == cialoy[j]):
                    mapkaxteraz.pop(i)
                    mapkayteraz.pop(i)

        gengroszek = random.randint(0, (len(mapkaxteraz)-1))
        zebrano = False

    if (x == mapkaxteraz[gengroszek] and y == mapkayteraz[gengroszek]):
        zebrano = True

        dlugosc = dlugosc + 1

    gamedisp.blit(Groszek, ((mapkaxteraz[gengroszek]), (mapkayteraz[gengroszek])))







    for i in range(0,len(cialox)): #wjechanie w ogon
        if(cialox[i]==x and cialoy[i]==y):
            print(cialox)
            print(cialoy)
            pygame.quit()
            quit()
    for i in range(0,len(scianyx)): #wjechanie w sciane
        if(scianyx[i]==x and scianyy[i]==y):
            print("groszek "+str(mapkaxteraz[gengroszek])+" "+str(mapkayteraz[gengroszek]))
            print(str(len(mapkax)))
            print(str(len(mapkay)))
            pygame.quit()
            quit()

    if (len(cialox) > dlugosc):
        del cialox[0]
        del cialoy[0]
        del kierunki[0]

    snek_begin(x, y, kierunek)
    cialox.append(x)
    cialoy.append(y)



    for i in range(1,len(cialox)):
        '''gamedisp.blit(Cialo,((cialox[i]),(cialoy[i])))'''
        zaginanie(kierunki[i],kierunki[i+1],i,dlugosc,cialox[i-1],cialoy[i-1])

    snek_begin(x, y, kierunek)

    pokazwynik(score)







    pygame.display.update()
    zegar.tick(7)


pygame.quit()
quit()