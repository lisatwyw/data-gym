# Extracting cell colors #

## xlsx  ##

```
import openpyxl
from openpyxl import load_workbook
excel_file = 'yuanyang2020/annot/LDH2020_mmc2.xlsx' 
wb = load_workbook(excel_file,keep_vba=True, data_only = False)
  
f=wb.sheetnames[0]
print('parsing sheet',f)
sh = wb[ f ]

for i in range(1,sh.max_row):

    ce=sh['D%d'%i]; color_in_hex=ce.fill.start_color.index; print(ce.value, color_in_hex ) # will hopefully print style at this cell


print('HEX =',color_in_hex) 
print('RGB =', tuple(int(color_in_hex[i:i+2], 16) for i in (0, 2, 4))) # Color in RGB

```



## xls only ##

```
import xlrd
book = xlrd.open_workbook("yuanyang2020/annot/LDH2020_mmc2.xlsx", formatting_info=True)
sheets = book.sheet_names()

for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    #print "Sheet:", sheet.name
    rows, cols = sheet.nrows, sheet.ncols
    #print "Number of rows: %s   Number of cols: %s" % (rows, cols)
    for row in range(rows):
        for col in range(cols):
            print("row, col is:", row+1, col+1,) 
            thecell = sheet.cell(row, col)      
            # could get 'dump', 'value', 'xf_index'
            print( thecell.value)
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            bgx = xf.background.pattern_colour_index
            print (bgx)
            
```            
