"""
Este é o código do clone de "Bomberman" criado na oficina de desenvolvimento de jogos
da Noite de Processing em 27/02/2018.
"""
from classes import *

mapa = []
bombs = []

def setup():
    global mapa, l, p1, p2, p1c, p2c
    size(400, 346)
    frameRate(15)
    mapa = [[None] * 13 for _ in range(15)]
    l = width / len(mapa)
    p1 = Index(1, 1)
    p2 = Index(13, 11)
    p1c = [False] * 5
    p2c = [False] * 5
    makeMapa()

def makeMapa():
    file = loadImage("mapa.png")
    for x in range(15):
        for y in range(13):
            t = 0
            c = file.get(x, y)
            if c == color(0):
                t = 2
            elif c == color(127):
                t = 1
            # elif c == color(195) )
            elif c == color(255):
                if abs(9 - dist(x, y, 7, 6)) * randomGaussian() > 1.2:
                    t = 1
            mapa[x][y] = t

def draw():
    # DESENHANDO O MAPA COM LOOPS ANINHADOS
    for x in range(15):
        for y in range(13):
            with pushMatrix():
                translate(x * l, y * l)
                s = mapa[x][y]
                if s == 0:
                    fill("#1CFF88")
                elif s == 1:
                    fill("#FF831C")
                elif s == 2:
                    fill("#5A5A5A")
                rect(0, 0, l, l)

    # EFETUANDO OS CONTROLES DO PLAYER 1
    if p1.i >= 0:
        if (p1c[0] and mapa[p1.i][p1.j - 1] == 0
                and nao_ha_bombas(p1.i, p1.j - 1)
                and not p2.equals(p1.i, p1.j - 1)):
            p1.j -= 1
        if (p1c[1] and mapa[p1.i][p1.j + 1] == 0
                and nao_ha_bombas(p1.i, p1.j + 1)
                and not p2.equals(p1.i, p1.j + 1)):
            p1.j += 1
        if (p1c[2] and mapa[p1.i - 1][p1.j] == 0
                and nao_ha_bombas(p1.i - 1, p1.j)
                and not p2.equals(p1.i - 1, p1.j)):
            p1.i -= 1
        if (p1c[3] and mapa[p1.i + 1][p1.j] == 0
                and nao_ha_bombas(p1.i + 1, p1.j)
                and not p2.equals(p1.i + 1, p1.j)):
            p1.i += 1

    if p1c[4] and nao_ha_bombas(p1.i, p1.j):
        bombs.append(Bomb(p1))

    # EFETUANDO OS CONTROLES DO PLAYER 2
    if p2.i >= 0:
        if (p2c[0] and mapa[p2.i][p2.j - 1] == 0
                and nao_ha_bombas(p2.i, p2.j - 1)
                and not p1.equals(p2.i, p2.j - 1)):
            p2.j -= 1
        if (p2c[1] and mapa[p2.i][p2.j + 1] == 0
                and nao_ha_bombas(p2.i, p2.j + 1)
                and not p1.equals(p2.i, p2.j + 1)):
            p2.j += 1
        if (p2c[2] and mapa[p2.i - 1][p2.j] == 0
                and nao_ha_bombas(p2.i - 1, p2.j)
                and not p1.equals(p2.i - 1, p2.j)):
            p2.i -= 1
        if (p2c[3] and mapa[p2.i + 1][p2.j] == 0
                and nao_ha_bombas(p2.i + 1, p2.j)
                and not p1.equals(p2.i + 1, p2.j)):
            p2.i += 1

    if p2c[4] and nao_ha_bombas(p2.i, p2.j):
        bombs.append(Bomb(p2))

    # DESENHANDO OS PLAYERS
    fill(0, 0, 255)
    ellipse((p1.i + 0.5) * l, (p1.j + 0.5) * l, l, l)
    fill(255, 0, 0)
    ellipse((p2.i + 0.5) * l, (p2.j + 0.5) * l, l, l)

    for b in bombs:
        # DESENHANDO AS BOMBAS
        b.plot(l)
        # CHECANDO SE A BOMBA DA EXPLODIU E...
        if b.explodiu():
            # CONFERINDO A AREA DA EXPLOSAO NAS QUATRO DIRECOES PARA...
            # para cima
            for e in range(b.pos.j - 1, b.pos.j - b.alcance - 1, -1):
                if mapa[b.pos.i][e] == 2:
                    break
                # DESTRUIR BLOCOS DESTRUTÍVEIS...
                if mapa[b.pos.i][e] == 1:
                    mapa[b.pos.i][e] = 0
                    continue
                # E JOGADORES QUE SE ENCONTREM NO CAMINHO.
                if p1.equals(b.pos.i, e):
                    p1.set(-1, -1)
                if p2.equals(b.pos.i, e):
                    p2.set(-1, -1)
                kaboom((b.pos.i + 0.5) * l, (e + 0.5) * l)
            # para baixo
            for e in range(b.pos.j + 1, b.pos.j + b.alcance + 1):
                if mapa[b.pos.i][e] == 2:
                    break
                if mapa[b.pos.i][e] == 1:
                    mapa[b.pos.i][e] = 0
                    continue

                if p1.equals(b.pos.i, e):
                    p1.set(-1, -1)
                if p2.equals(b.pos.i, e):
                    p2.set(-1, -1)
                kaboom((b.pos.i + 0.5) * l, (e + 0.5) * l)
            # para a esquerda
            for e in range(b.pos.i - 1, b.pos.i - b.alcance - 1, -1):
                if mapa[e][b.pos.j] == 2:
                    break
                if mapa[e][b.pos.j] == 1:
                    mapa[e][b.pos.j] = 0
                    continue
                if p1.equals(e, b.pos.j):
                    p1.set(-1, -1)
                if p2.equals(e, b.pos.j):
                    p2.set(-1, -1)
                kaboom((e + 0.5) * l, (b.pos.j + 0.5) * l)
            # para a direita
            for e in range(b.pos.i + 1, b.pos.i + 1 + b.alcance):
                if mapa[e][b.pos.j] == 2:
                    break
                if mapa[e][b.pos.j] == 1:
                    mapa[e][b.pos.j] = 0
                    continue

                if p1.equals(e, b.pos.j):
                    p1.set(-1, -1)
                if p2.equals(e, b.pos.j):
                    p2.set(-1, -1)
                kaboom((e + 0.5) * l, (b.pos.j + 0.5) * l)
            bombs.remove(b)  


def nao_ha_bombas(I, J):
    for b in bombs:
        if b.pos.equals(I, J):
            return False
    return True
#

def kaboom(x, y):
    fill(random(160, 255), random(160, 255), 0)
    N = int(random(5.501, 8.499))
    N *= 2
    beginShape()
    t = TWO_PI / N
    d = l * 0.8
    q = False
    for i in range(N):
        a = random(i * t, (i + 1) * t)
        d += random(-3, 2)
        vertex(d * cos(a) + x, d * sin(a) + y)
        if q:
            d = l * 0.8
        else:
            d = l * 0.4
    endShape(CLOSE)

def keyPressed():
    global p1c, p2c
    if key == 'w':
        p1c[0] = True
    elif key == 's':
        p1c[1] = True
    elif key == 'a':
        p1c[2] = True
    elif key == 'd':
        p1c[3] = True
    elif key == 'c':
        p1c[4] = True
    elif key == '.':
        p2c[4] = True

    if keyCode == UP:
        p2c[0] = True
    if keyCode == DOWN:
        p2c[1] = True
    if keyCode == LEFT:
        p2c[2] = True
    if keyCode == RIGHT:
        p2c[3] = True


def keyReleased():
    global p1c, p2c
    if key == 'w':
        p1c[0] = False
    elif key == 's':
        p1c[1] = False
    elif key == 'a':
        p1c[2] = False
    elif key == 'd':
        p1c[3] = False
    elif key == 'c':
        p1c[4] = False
    elif key == '.':
        p2c[4] = False

    if keyCode == UP:
        p2c[0] = False
    if keyCode == DOWN:
        p2c[1] = False
    if keyCode == LEFT:
        p2c[2] = False
    if keyCode == RIGHT:
        p2c[3] = False