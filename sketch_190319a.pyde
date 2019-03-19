#lista = [1,1,2]
#krotka = (1,1,2)
#slownik = {"klucz":"wartosc", "key":"value"}
#zbior = {3,1,2}

def setup():
    frameRate(60)
    rectMode(CENTER)
    size(400,400)
    krotkaKolorow=((255,0,0),(0,255,0),(0,0,255))
    fill (69,63,255)
    strokeWeight(8)
    stroke(*krotkaKolorow[0])
    global x
    global y
    x = 0
    y = 0
def draw():
    global x
    x=x+1
    global y
    y=y+1
    rect(height/2,width/2,x,y)
    if x > width:
        exit()
def mousePressed():
    #loop() start
    #noLoop() stop
    #redraw() odswiez
    pass
