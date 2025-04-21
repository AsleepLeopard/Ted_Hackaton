h = "#"
satır = 4
bosluk =" "
hs = 7
bs = 2
ff =3
for x in range(satır + 1):
    print(x*bosluk + hs * h)
    hs -= 2
    x += 2
for y in range(satır + 1):
    print(bs*bosluk + ff * h)
    bs-=1
    ff+= 2