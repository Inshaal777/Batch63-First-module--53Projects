from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20


rectangles = []

def erase_objects(win, eraser):
    
    eraser_x1 = eraser.getP1().getX()
    eraser_y1 = eraser.getP1().getY()
    eraser_x2 = eraser.getP2().getX()
    eraser_y2 = eraser.getP2().getY()

    
    for rect in rectangles:
        rect_x1 = rect.getP1().getX()
        rect_y1 = rect.getP1().getY()
        rect_x2 = rect.getP2().getX()
        rect_y2 = rect.getP2().getY()

        
        if (eraser_x1 < rect_x2 and eraser_x2 > rect_x1 and
            eraser_y1 < rect_y2 and eraser_y2 > rect_y1):
            rect.setFill('white')

def main():
    win = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            rect = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            rect.setFill('blue')
            rect.draw(win)
            rectangles.append(rect)

    win.getMouse()
    eraser = Rectangle(Point(0, 0), Point(ERASER_SIZE, ERASER_SIZE))
    eraser.setFill('pink')
    eraser.draw(win)

    while True:
        if win.checkMouse():
            mouse_x, mouse_y = win.getMouse().getX(), win.getMouse().getY()
            eraser.move(mouse_x - ERASER_SIZE / 2 - eraser.getP1().getX(), 
                        mouse_y - ERASER_SIZE / 2 - eraser.getP1().getY())

            erase_objects(win, eraser)

        if win.isClosed():
            break

    win.close()

if __name__ == '__main__':
    main()