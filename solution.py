image  = [[1,1,1],[1,1,0],[1,0,1]]

sr = int(input())
sc = int(input())
newColor = 2

rows = len(image)
cols = len(image[0])
oldColor = image[sr][sc]


def result (image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            print(image[i][j], end=' ')
        print()
    print()
result(image)



def way(image,  sr, sc,  newColor,oldColor, rows,  cols):
    if (sr>rows-1 or sr<0) or (sc>cols-1 or sc<0) or (image[sr][sc]==newColor) :
        return
    else:
        if(image[sr][sc]!=oldColor):
            return
        else:
            image[sr][sc]=newColor;
            way(image,sr+1,sc,newColor,oldColor,rows,cols)
            way(image,sr,sc+1,newColor,oldColor,rows,cols)
            way(image,sr,sc-1,newColor,oldColor,rows,cols)
            way(image,sr-1,sc,newColor,oldColor,rows,cols)


way(image,sr,sc,newColor,oldColor,rows,cols)
result(image)