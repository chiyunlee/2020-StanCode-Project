"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    gap = (width-2*GRAPH_MARGIN_SIZE) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + gap*year_index
    return x_coordinate





def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,width = LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT- GRAPH_MARGIN_SIZE,width = LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),0,get_x_coordinate(CANVAS_WIDTH, i),CANVAS_HEIGHT,width = LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=YEARS[i],anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    for i in range(len(lookup_names)):
        color = COLORS[i % len(COLORS)]
        each_rank_y = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
        name = lookup_names[i]
        year_rank = name_data[name]  # take the value(type:dict) of the name and put into year_rank={year:rank}
        rank_list = []
        #check if name get value at each_year in YEARS
        for each_year in YEARS:
            if str(each_year) in year_rank:
                rank_list.append(year_rank[str(each_year)])  # 取year的value(rank值,type:dict)存到rank_list，沒有year的存'1001'
            else:
                rank_list.append('1001')

        if int(rank_list[0]) <= 1000:
            x1 = get_x_coordinate(CANVAS_WIDTH, 0)
            y1 = GRAPH_MARGIN_SIZE + int(rank_list[0])*each_rank_y
            canvas.create_text(x1 + TEXT_DX, y1, text=str(name) + str(' ') + str(rank_list[0]),anchor = tkinter.SW,fill=color)

        elif int(rank_list[0]) == 1001:
            x1 = get_x_coordinate(CANVAS_WIDTH, 0)
            y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_text(x1 + TEXT_DX, y1, text=str(name) + str(' ') + str('*'),anchor = tkinter.SW,fill=color)

        for j in range(1, len(YEARS)):
            if int(rank_list[j]) <= 1000:
                x2 = get_x_coordinate(CANVAS_WIDTH, j)
                y2 = GRAPH_MARGIN_SIZE + int(rank_list[j]) * each_rank_y
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                canvas.create_text(x2 + TEXT_DX, y2, text=str(name) + str(' ') + str(rank_list[j]),anchor = tkinter.SW,fill=color)
                x1 = x2
                y1 = y2
            elif int(rank_list[j]) == 1001:
                x2 = get_x_coordinate(CANVAS_WIDTH, j)
                y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                canvas.create_text(x2 + TEXT_DX, y2, text=str(name) + str(' ') + str('*'),anchor = tkinter.SW,fill=color)
                x1 = x2
                y1 = y2





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
