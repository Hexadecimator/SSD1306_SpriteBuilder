# SSD1306_SpriteBuilder
Spreadsheet-based sprite builder for SSD1306 OLEDs

Necessary Python Dependencies:
  1. XLRD - package for reading excel sheets (only .XLS!! NOT .XLSX!!!)

Operating instructions:
  1. Create a .xls file in the same folder you placed the SSD1306_Sprite_Builder.py script
  2. Name this new .xls file "spritebuilder.xls" (exact name is very important)
  3. Inside spritebuilder.xls, Make an X by Y block of BLACK-colored cells.
    3a. NOTE THAT X and Y MUST BOTH BE SOME MULTIPLE OF 8.
    3b. ALSO NOTE THAT THE LARGEST SCREEN IS 128x64 pixels
  4. "Draw" your sprite using WHITE colored cells OVER the black colored cells. Any cell that appears white will be a white pixel on the SSD1306 screen
  5. When you are finished drawing the sprite in the excel file, save the .xls and close it
  6. With the python script and the .xls file in the same folder, run the python script.
  7. The python script will output in the terminal window the full code you will need to paste into your own SSD1306 code to create the sprite on the SSD1306 screen
    7a. Copy the code from the python terminal output to your code. Change the name of the sprite if you care to do so (default sprite name is logo_bmp[])
    
    
 Examples .xls files are included in the "finished sprites" folder of the repository
