import math,pygame,random



class snake(object):
    body=[]
    turns={}
    def __init__(self,color,position):
        self.color=color
        self.head=cube(position)
        self.body.append(self.head)
        self.to_x=0
        self.to_y=1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys=pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.to_x=1
                self.to_y=0
                self.turns[self.head.pos[:]] = [self.to_x,self.to_y]
            elif keys[pygame.K_RIGHT]:
                self.to_x = -1
                self.to_y = 0
                self.turns[self.head.pos[:]] = [self.to_x, self.to_y]
            elif keys[pygame.K_UP]:
                self.to_x = 0
                self.to_y = -1
                self.turns[self.head.pos[:]] = [self.to_x, self.to_y]
            elif keys[pygame.K_DOWN]:
                self.to_x = 0
                self.to_y = 1
                self.turns[self.head.pos[:]] = [self.to_x, self.to_y]
        for inex,cube in enumerate(self.body):
            p=cube.pos[:]
            if p in self.turns:
                turn=self.turns[p]
                cube.move(turn[0],turn[1])
                if inex ==len(self.body -1):
                    self.turns.pop(p)
            else:
                if cube.to_ ==-1 and cube.pos[0]<=0:
                    cube.pos= (cube.rows-1,cube.pos[1])
                elif cube.to_ == 1 and cube.pos[0] >=cube.rows -1:
                    cube.pos= (0,cube.pos[1])
                elif cube.to_ == 1 and cube.pos[1] >=cube.rows -1:
                    cube.pos= (cube.pos[0],0)
                elif cube.to_ == -1 and cube.pos[1] <=0:
                    cube.pos= (cube.pos[0],cube.rows-1)
                else:
                    cube.move(cube.to_x,cube.to_y)

    def restet(self,pas):
        pass

    def add_tail(self):
        pass

    def draw(self,surface):
        pass

def draw_grid(w,rows,surface):
    size_between=w//rows

    x=0
    y=0
    for l in range(rows):
        x=x+size_between
        y=y+size_between
        pygame.draw.line(surface,(0,0,0),(x,0),(x,w))
        pygame.draw.line(surface,(0,0,0),(0,y),(w,y))

def draw_window(surface):
    surface.fill((60, 186, 56))
    draw_grid(size,rows,surface)
    pygame.display.update()

def main():
    global size,rows
    size=500
    rows=20
    clock=pygame.time.Clock()

    window=pygame.display.set_mode((size,size))

    judas=snake((255,0,0),(10,10))

    flag=True
    while flag:

        pygame.time.delay(50)
        clock.tick(10)

        draw_window(window)

main()


