class Bomb():

    def __init__(self, p):
        self.pos = p.get()
        self.fusivel = millis() + 3000

    def explodiu(self):
        if millis() > self.fusivel:
            return True
        else:
            return False

    def plot(self):
        fill(0)
        ellipse((self.pos.i + 0.5) * l,
                (self.pos.j + 0.5) * l, l, l)


class Tile():
    # 0: nada, 1: pedra(des) 2:pedra(ind)
    def __init__(self, t):
        self.tipo = t

    def atravessavel(self):
        return tipo == 0

    def plot(self):
        if self.tipo == 0:
            fill("#1CFF88")
        elif self.tipo == 1:
            fill("#FF831C")
        elif self.tipo == 2:
            fill("#5A5A5A")
        rect(0, 0, l, l)


class Index():

    def __init__(self, I, J):
        self.i = I
        self.j = J

    def get(self):
        return Index(i, j)
