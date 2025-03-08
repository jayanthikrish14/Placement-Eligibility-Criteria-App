import CreateFakeData as cfd
import CreateTables as ct

# Create Students table
ct.createTable(ct.create_Students_tbl_query)

# Create Programming table
ct.createTable(ct.create_Programming_tbl_query)

# Create Soft Skills table
ct.createTable(ct.create_Soft_Skills_tbl_query)

# Create Placements table
ct.createTable(ct.create_Placements_tbl_query)

# Create and Insert fake data into above tables
# Pass Nof Students parameter1 and 
# Nof Programming records required for each student as parameter2
cfd.Create_Insert_Fake_Data(500,2)