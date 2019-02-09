from math import *
def distanceeuclid(point1,point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    local = pow(x,2)+pow(y,2)
    return sqrt(local)

def voisins(point,listepointsrestants):
    # on suppose que la liste est non vide
    # liste des points de coordonnes
    # on renvoie une liste de deux elements
    # le premier element ce sont les voisins les plus proches
    # le deuxieme c la valeur de la distance
    listeVoisins = [listepointsrestants[0]]
    distance = distanceeuclid(point,listepointsrestants[0])
    for i in range(1,len(listepointsrestants)):
        if (distanceeuclid(point,listepointsrestants[i]) < distance and distanceeuclid(point,listepointsrestants[i]) != 0) :
            listeVoisins = [listepointsrestants[i]]
            distance = distanceeuclid(point,listepointsrestants[i])
        elif (distanceeuclid(point,listepointsrestants[i]) == distance) :
            listeVoisins.append(listepointsrestants[i])
    return[listeVoisins,distance]


def plusprochevoisin(pointinitial,listedepoints):
    # initialisation
    distance = 0
    parcours = list([pointinitial])
    output = [[parcours,distance,list(listedepoints)]]
    test = True
    while(test):
        #print("hello world")
        for i in range(0,len(output)):
            test = False
            #print(i)
            if len(output[i][2])> 0 :
                #print output[i][0][-1]
                Voisin = voisins(output[i][0][-1],output[i][2])
                if len(Voisin[0]) == 1:
                    output[i][0].append(Voisin[0][0]) # ajouter le point
                    output[i][1] += Voisin[1] # ajouter la distance
                    output[i][2].remove(Voisin[0][0]) # enlever le point de la liste restante
                else:
                    for j in range(1,len(Voisin[0])):
                        local = [list(output[i][0]),output[i][1],list(output[i][2])]
                        #print (local,"local")
                        
                        local[0].append(Voisin[0][j])
                        #print (output[i],"output[i] after appending voisin")
                        local[1] += Voisin[1]
                        local[2].remove(Voisin[0][j])
                        output.append(local)
                        
                    output[i][0].append(Voisin[0][0])
                    output[i][1] += Voisin[1]
                    output[i][2].remove(Voisin[0][0])
                    break
        for i in range(0,len(output)):
            if (len(output[i][2])>0):
                test = True
                break

    for i in range(0,len(output)):
        pointfinal = output[i][0][-1]
        output[i][1] += distanceeuclid(pointinitial,pointfinal)
        output[i][0].append(pointinitial)
    return output
                
                

    


# exemple
pointinitial = (0,0)
point0 = (0,1)
point1 = (2,0)
point2 = (2,2)
point3 = (3,2)
point4 = (2,4)
point5 = (1,6)
point6 = (0,6)
point7 = (0,7)
point8 = (2,7)
point9 = (4,6)
point10 = (5,5)
point11 = (5,7)
point12 = (4,8)
point13 = (4,9)
point14 = (1,9)
point15 = (0,10)
point16 = (6,10)
point17 = (8,9)
point18 = (8,6)
point19 = (10,5)
point20 = (10,4)
point21 = (9,3)
point22 = (10,3)
point23 = (11,3)
point24 = (8,1)
point25 = (7,0)
point26 = (8,0)
point27 = (9,0)
point28 = (15,10)
point29 = (15,8)
point30 = (14,8)
point31 = (14,7)
point32 = (13,5)
point33 = (13,3)
point34 = (14,2)
point35 = (14,1)
listedepoints = [point0,point1,point2,point3,point4,point5,point6,point7,point8,point9,point10,point11,point12,point13,\
                 point14,point15,point16,point17,point18,point19,point20,point21,point22,point23,point24,point25,\
                 point26,point27,point28,point29,point30,point31,point32,point33,point34,point35]


Resultat = plusprochevoisin(pointinitial,listedepoints)
print(len(Resultat))
##for i in range(0,len(plusprochevoisin(pointinitial,listedepoints))):
##    print plusprochevoisin(pointinitial,listedepoints)[i]
i = 0
distance = Resultat[i][1]
for i in range(0,len(Resultat)):
    if (distance > Resultat[i][1]):
        distance = Resultat[i][1]
        parcoursexo = Resultat[i][0]
print(parcoursexo)
print(distance,"distance point le plus proche")
print (len(parcoursexo))

def convexhull (convexe , pointsrestants):
    local = list(convexe)
    localrestant = list(pointsrestants)
    while(len(localrestant)>0):
    # trouver le point le plus proche a local
        distances_points = list([])
        for i in range(0,len(localrestant)):
            distances_points.append([voisins(localrestant[i],local)[1],localrestant[i]])
        pointlesplusproches = []
        distance = distances_points[0][0]
        for i in range(0,len(distances_points)):
            if (distance > distances_points[i][0]):
                distance = distances_points[i][0]
                pointlesplusproches = [distances_points[i][1]]
            elif(distance == distances_points[i][0]):
                pointlesplusproches.append(distances_points[i][1])
        #print(pointlesplusproches)
        cout = distanceeuclid(local[0],pointlesplusproches[0])+distanceeuclid(local[1],pointlesplusproches[0]) - \
               distanceeuclid(local[0],local[1])
        for j in range(0,len(pointlesplusproches)):
            for i in range(0,len(local)-1):
                if (distanceeuclid(local[i],pointlesplusproches[j])+distanceeuclid(local[i+1],pointlesplusproches[j]) - \
                    distanceeuclid(local[i],local[i+1]) < cout):
                    cout = distanceeuclid(local[i],pointlesplusproches[j])+distanceeuclid(local[i+1],pointlesplusproches[j]) - \
                           distanceeuclid(local[i],local[i+1])
                    icandidat = i
                    pointcandidat = pointlesplusproches[j]
        localrestant.remove(pointcandidat)
        local.insert(icandidat+1,pointcandidat)
        #print(pointcandidat)
        #print(cout)
    return local
                           
    
convexe = [pointinitial,point1,point25,point26,point27,point35,point29,point28,point16,point15,point7,point6,\
           point0,pointinitial]
pointsrestants = [point2,point3,point4,point5,point8,point9,point10,point11,point12,point13,point14,point17 ,\
                  point18,point19,point20,point21,point22,point23,point24,point30,point31,point32,point33,point34]
A = convexhull (convexe , pointsrestants)
distanceconvexe = 0
for i in range(0,len(A)-1):
    distanceconvexe += distanceeuclid(A[i],A[i+1])
print(distanceconvexe)
