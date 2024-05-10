# Gotta use and run panda and os
import pandas as pd
import os

# In this blank you have to put the route from the file you need (Important: always change the "\"" to "/"), 
# Hint: use in the terminal the comand "pwd" to know where you are 
route_base = "./" 

# To store the information
information = []

# To process a file it use a function called "processing_archive"
def processing_archive(archive, carpet_name):
    line27_values = None
    with open(archive, 'r') as f:
        for num_line, line in enumerate(f, 1):
            if num_line == 27:
                line27_values = line.strip().split()  # Divide la línea en una lista de valores
                break                                       
    if line27_values is None or len(line27_values) != 4:
        return None  # Si no se encuentran valores o no hay exactamente 4 valores, retorna None
    return {"Value1": line27_values[0], "Value2": line27_values[1], "Value3": line27_values[2], "Value4": line27_values[3], "File Name": carpet_name}

for carpet, _, multiple_archive in os.walk(route_base):
    for archive in multiple_archive:
        if archive == "log.txt":
            full_route = os.path.join(carpet, archive)
            archive_dates = processing_archive(full_route, os.path.basename(carpet))
            if archive_dates:  # Verifica si se obtuvo un diccionario válido
                information.append(archive_dates)

# To convert the list to a DataFrame
df = pd.DataFrame(information)

# To save the DataFrame (Important: in this case is in excel, if you want
# other type of file you gotta change it)
directory_results = "./output/delta_g_results.xlsx"
df.to_excel (directory_results, index=False)
print ("your file is done")


