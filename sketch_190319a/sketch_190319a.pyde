#lista = [1,1,2]
#krotka = (1,1,2)
#slownik = {"klucz":"wartosc", "key":"value"}
#zbior = {3,1,2}

def setup():
    frameRate(60)
    rectMode(CENTER)
    size(1280,720)
    krotkaKolorow=((255,0,0),(0,255,0),(0,0,255))
    fill (69,63,255)
    strokeWeight(8)
    stroke(*krotkaKolorow[0])
    global a
    global b
    global c
    global d
    global Vx
    global dir
    a = 0
    b = 300 # program staje się wrażliwszy na zmianę, gdy te wartości są określone poprzez inne zmienne (wbudowane)
    c = 150
    d = 150
    Vx = 5
    dir = 1
def draw():
    global a,b,c,d,Vx,dir
    background(0)
    noStroke()
    rgb=[0,0,0]
    rgb[0] = random(0,255)
    rgb[1] = random(0,255)
    rgb[2] = random(0,255)
    fill(rgb[0], rgb[1], rgb[2])
    rect(a,b,c,d)
    if (a == 1160):
        dir = 0
    if (a == 0):
        dir = 1
    if (dir == 1):
        a = a+Vx
    else:
        a = a-Vx
        exit()
def mousePressed():
    #loop() start
    #noLoop() stop
    #redraw() odswiez
    pass
