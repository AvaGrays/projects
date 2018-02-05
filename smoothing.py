###SMOOTHING###

#drawn=list of tuples
#a=degree of smoothing(with 0 being perfectly smooth)
def smooth(drawn, a):
    #Finding starting and ending x and y
    start=drawn[0]
    end=drawn[len(drawn)-1]

    start1=start[0]
    start2=start[1]
    end1=end[0]
    end2=end[1]

    #Perfectly smooth
    num_of_points=len(drawn)-1
    nums=num_of_points
    perfect_x=[]
    perfect_y=[]
    smoothed_points=[]
    #Getting perfect points
    while nums>-1:
        perfx=int((start1*nums+end1*(num_of_points-nums))/num_of_points)
        perfy=int((start2*nums+end2*(num_of_points-nums))/num_of_points)
        perfect_x.append(perfx)
        perfect_y.append(perfy)
        nums-=1
    #Getting smoothed points
    if a==0:
        drawn=[]
        drawn.append(start)
        drawn.append(end)
    else:
        for i in range(len(drawn)):
            pointx=drawn[i][0]
            smoothedx=int((a*perfect_x[i]+pointx)/(a+1))
            pointy=drawn[i][1]
            smoothedy=int((a*perfect_y[i]+pointy)/(a+1))
            smoothed_points.append((smoothedx, smoothedy))
        drawn=smoothed_points
    return drawn


