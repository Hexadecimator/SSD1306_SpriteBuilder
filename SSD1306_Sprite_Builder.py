import xlrd as xl

book = xl.open_workbook("spritebuilder.xls", formatting_info=True)

sheets = book.sheet_names()

print ("Sheets are: ", sheets)

for index, curr_sheet in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    print ("Sheet: ", sheet.name)
    rows, cols = sheet.nrows, sheet.ncols
    print ("\n\n")
    logo_height_str = "#define LOGO_HEIGHT " + str(rows)
    logo_width_str = "#define LOGO_WIDTH " + str(cols)
    print ("\n\n")
    
    
    if (rows%8 != 0 or cols%8 != 0):
        print ("ERROR - height and width must be a multiple of 8! Exiting")
        exit()

    bin_result_array = [] # hold the result
    #print ("# rows: ", rows, " / # cols: ", cols)
    for row in range(rows):
        bin_rep = "" #reset every new row
        bit_count = 1 #count to 8
        for col in range(cols):
            #cur_cell = sheet.cell(row, col)
            #print(thecell.value) 
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            #bgx = 8 = black background
            #bgx = 9 = white background
            bgx = xf.background.pattern_colour_index
            
            if (bit_count == 1):
                # start str with 0b
                if (str(bgx) == "8"):
                    bin_rep = "0b0"
                elif (str(bgx) == "9"):
                    bin_rep = "0b1"
                bit_count += 1
            elif (bit_count == 8):
                # end str and add bin_result_array.append(bin_rep)
                if (str(bgx) == "8"):
                    #
                    bin_rep = bin_rep + "0"
                    bin_result_array.append(bin_rep)
                elif (str(bgx) == "9"):
                    #
                    bin_rep = bin_rep + "1"
                    bin_result_array.append(bin_rep)
                bit_count = 1
            else:
                if (str(bgx) == "8"):
                    bin_rep = bin_rep + "0"
                elif (str(bgx) == "9"):
                    bin_rep = bin_rep + "1"
                bit_count += 1

    # array_width controls how many 8 bit numbers output per row
    array_width = cols / 8
    #print("Array width: " + str(array_width) + " Array size: " + str(len(bin_result_array)) + "\n\n")
    
    print(logo_height_str)
    print(logo_width_str)
    print("static const unsigned char PROGMEM logo_bmp[] =")
    print("{")

    count = 0
    row_contents = ""
    for i in range(0, len(bin_result_array)+1):
        if (count < array_width):
            row_contents += bin_result_array[i] + ", "
            count += 1
        elif (count == array_width):
            if ( i == len(bin_result_array)):
                # this is the end
                print(row_contents[:-2])
            else:
                print(row_contents)
                row_contents = bin_result_array[i] + ", "
            count = 1
    print("};")


        