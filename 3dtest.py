import pygame,sys,math

# (0,1) : (sin,cos)
# (1,0) : (cos,-sin)
# (0,-1) : (-sin,-cos)
# (-1,0) : (-cos,sin)
# x = x*cos - y*sin
# y = y*cos + x*sin
def rotate2d(pos,rad):
    x,y=pos
    s,c=math.sin(rad),math.cos(rad)
    return x*c-y*s,y*c+x*s


class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    def events(self,event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x/=200; y/=200
            self.rot[0] += y; self.rot[1] += x
    def update(self,dt,key):
        s = dt * 10

        if key[pygame.K_q]: self.pos[1] -= s
        if key[pygame.K_e]: self.pos[1] += s

        x,y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

        if key[pygame.K_w]: self.pos[0] += x; self.pos[2] += y
        if key[pygame.K_s]: self.pos[0] -= x; self.pos[2] -= y

        if key[pygame.K_a]: self.pos[0] -= y; self.pos[2] += x
        if key[pygame.K_d]: self.pos[0] += y; self.pos[2] -= x
class Cube:
    verts = (1,1,1,),(1,1,-1,),(1,-1,1,),(1,-1,-1,),(-1,1,1,),(-1,1,-1,),(-1,-1,1,),(-1,-1,-1)
    faces = (0,1,3,2),(4,0,2,6),(4,5,7,6),(1,3,7,5),(0,1,5,4),(2,3,7,6)
    colors = (255,0,0),(255,128,0),(255,255,0),(255,255,255),(0,0,255),(0,255,0)

    def __init__(self,pos=(0,0,0)):
        x,y,z = pos
        self.verts = [(x+X/2,y+Y/2,z+Z/2) for X,Y,Z in self.verts]






pygame.init()
w,h = 800,800
cx,cy = w//2, h//2

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

        



cam = Cam((0,0,-5))

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)


cubes = []
for i in range(3):
    for j in range(3):
        for q in range(3):
            cubes.append(Cube((q*1.1,j*1.1,i*1.1)))



while True:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        cam.events(event)
    screen.fill((0,128,128))
    #       we started by drawing points

    # for x,y,z in verts:
    #     z += 5
    #     f = 200/z
    #     x,y = x*f,y*f
    #     pygame.draw.circle(screen,(0,0,0),(cx+int(x),cy + int(y)),3)

    #       than we commented that and began to draw edges

    # for edge in edges:
    #     points = []
    #     for x,y,z in (verts[edge[0]],verts[edge[1]]):
    #         x-=cam.pos[0]
    #         y-=cam.pos[1]
    #         z-=cam.pos[2]

    #         x,z = rotate2d((x,z),cam.rot[1])
    #         y,z = rotate2d((y,z),cam.rot[0])

    #         f = 200/z
    #         x,y = x*f,y*f
    #         points += [(cx+int(x),cy+int(y))]
    #     pygame.draw.line(screen,(0,0,0),points[0],points[1],1)

    #       finally commenting the edges and now simply drawing faces
    face_list = []
    face_color = []
    depth = []
    for obj in cubes:     
        vert_list = []
        screen_coords = []
        for x,y,z in obj.verts:
            x-=cam.pos[0]
            y-=cam.pos[1]
            z-=cam.pos[2]

            x,z = rotate2d((x,z),cam.rot[1])
            y,z = rotate2d((y,z),cam.rot[0])
            vert_list += [(x,y,z)]
            f = 200/z
            x,y = x*f,y*f
            screen_coords += [(cx+int(x),cy+int(y))]

        
    

        for f in range(len(obj.faces)):

            face = obj.faces[f]

            on_screen = False
            for i in face:
                x,y = screen_coords[i]
                if vert_list[i][2]>0 and x>0 and x<w and y>0 and y<h: on_screen = True; break
            if on_screen:
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [obj.colors[f]]

                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]



    # final.... blah blah comment
    order = sorted(range(len(face_list)),key=lambda i: depth[i],reverse=1)

    for i in order:
        try: pygame.draw.polygon(screen,face_color[i],face_list[i])
        except: pass


    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt,key)