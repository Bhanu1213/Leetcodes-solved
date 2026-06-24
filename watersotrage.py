tank=[int(x) for x in input().split()]
left,right=0,len(tank)-1
max_water=0
while left<right:
    height=min(tank[left],tank[right])
    width=right-left
    water=height*width
    max_water=max(max_water,water)
    if tank[left]<tank[right]:
        left+=1
    else:
        right-=1
print(max_water)
