# Jake McGhee

def jake_thanksgiving():
    canvas = makeEmptyPicture(1400,1000)
    
    grid = makeGrid(canvas, 3, 4)
    
    backgroundColor = makeColor(100, 0, 0)    
    for x in range (grid[0][1][0], grid[1][3][0]):
        for y in range (grid[0][1][1], grid[1][3][1]):
            p = getPixel(canvas, x, y)
            setColor(p, backgroundColor)
    
    textColor = makeColor(255, 180, 0)
    s1 = makeStyle(sansSerif, plain, 30)
    addTextWithStyle(canvas, grid[0][1][0] + 30, grid[0][1][1] + 50, "From manifest destiny...", s1, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 250, grid[0][1][1] + 110, "...to destructive neoliberal policy", s1, textColor)
    s2 = makeStyle(sansSerif, plain, 18)
    addTextWithStyle(canvas, grid[0][1][0] + 20, grid[0][1][1] + 150, "To the colonizers,", s2, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 30, grid[0][1][1] + 180, "Thanksgiving may be a celebration of family and a time to show gratitude", s2, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 20, grid[0][1][1] + 210, "But for many of the colonized,", s2, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 30, grid[0][1][1] + 240, "Thanksgiving is a time of grief and morning", s2, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 20, grid[0][1][1] + 270, "To me,", s2, textColor)
    addTextWithStyle(canvas, grid[0][1][0] + 30, grid[0][1][1] + 300, "Thanksgiving exemplifies American exceptionalism and historical whitewashing", s2, textColor)
       
    portrait = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\nintchdbpict000292467637.jpg')
    portrait = copyPictureToFitGrid(portrait, canvas, 3, 2, 0, 530)
    copyToTarget(portrait, canvas, grid[2][1][0], grid[2][1][1])
    
    dinner = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\o-THANKSGIVING-PRAYER-facebook.jpg')
    dinner = copyPictureToFitGrid(dinner, canvas, 3, 2, 120, 80)
    copyToTarget(dinner, canvas, grid[1][1][0], grid[1][1][1])
    
    natives = [makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\4tear44b.jpg'), 
    makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\t1larg.trail.of.tears.max.standley.courtesy.jpg'),
    makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\cultural-genocide.jpg'),
    makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\15959587_1478887651.488.jpg'),
    makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\protester-water-cops2000.jpg'),
    makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\defend-the-sacred.jpg')]
    
    addBorderImage(natives[0], canvas, 175, 80, grid[0][0][0], grid[0][0][1])
    addBorderImage(natives[1], canvas, 175, 100, grid[1][0][0], grid[1][0][1])
    addBorderImage(natives[2], canvas, 200, 125, grid[2][0][0], grid[2][0][1])
    addBorderImage(natives[3], canvas, 225, 0, grid[0][3][0], grid[0][3][1])
    addBorderImage(natives[4], canvas, 500, 100, grid[1][3][0], grid[1][3][1])
    addBorderImage(natives[5], canvas, 225, 75, grid[2][3][0], grid[2][3][1])

    writePictureTo(canvas, 'C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab7\\thanksgiving.jpg')
    
def addBorderImage(pic, canvas, beginX, beginY, targetX, targetY):
    """ helper function to add the surrounding images in Jake's thanksgiving card """
    
    pic = copyPictureToFitGrid(pic, canvas, 3, 4, beginX, beginY)
    pic = BnW(pic)
    copyToTarget(pic, canvas, targetX, targetY)
    return canvas

    
def copyToTarget(source, target, targetX, targetY):
    """ makes a copy of an image - same function as pyCopy except it does not show the result"""

    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source, x, y))
            setColor(getPixel(target, x+targetX, y+targetY), color)
    return target  
    

def makeGrid(canvas, row, col):
    """ creates a m x n list containing the [x,y] locations on the grid where pictures should be drawn 
        to use the grid use grid = makeGrid(canvas, row, col) and then grid[row][col][0] for the x positon and grid[row][col][1] for the y position"""

    grid = []
    i = -1
    for y in range (0, getHeight(canvas), getHeight(canvas) / row):
        grid.append([])
        i+=1
        for x in range (0, getWidth(canvas), getWidth(canvas) / col):
            grid[i].append([x,y])
    return grid
     
def copyPictureToFitGrid(pic, canvas, row, col, beginX, beginY):
    """ crops a picture so that it will fit on an m x n grid """
    
    # get size of the new picture
    width = getWidth(canvas) / col
    height = getHeight(canvas) / row
    
    #make sure picture is large enough to fit on the grid
    if getWidth(pic) < width:
        print("Error - image too small to fit on grid - %s" % pic) 
        return
    elif getHeight(pic) < height:
        print("Error - image too small to fit on grid - %s" % pic)
        return
    
    copy = makeEmptyPicture(width, height)
    
    # reduce size of the picture if it is significantly bigger than the grid size  
    while getWidth(pic) > width*2 and getHeight(pic) > height*2:
        pic = shrink(pic)
    
    # error check for out of bounds exception
    if getWidth(pic) - beginX < width:
         beginX = getWidth(pic) - width
    if getHeight(pic) - beginY < height:
         beginY = getHeight(pic) - height
        
    # paint new picture
    for x in range (0, width):
        for y in range (0, height):
            color = getColor(getPixel(pic, x+beginX, y+beginY))
            setColor(getPixel(copy, x, y), color)
    return copy
    
def shrink(pic):
  """ shrinks an image to 1/2 of its original size """

  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width/2, height/2)
  for x in range (0, width-1, 2):
    for y in range (0, height-1, 2):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x/2, y/2), color)
  return canvas    
  
  
def BnW(pic):
    """ Converts an image to gray-scale """
    
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    return pic
