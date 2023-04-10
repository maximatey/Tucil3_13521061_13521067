def readFile(filename):
    with open('test/'+filename, 'r') as file:
  
        # Read the dimensions from the first line
        dimensions = file.readline().strip().split()
        rows = int(dimensions[0])
        cols = int(dimensions[1])

        # Read the matrix elements from the second line

        # Convert the matrix elements to integers
        matrix = []
        for i in range(rows):
            matrix_elements = file.readline().strip().split()
            row = []
            for j in range(cols):
                row.append(int(matrix_elements[j]))
            matrix.append(row)


        koordinat_elements = file.readline().strip().split()
        koordinat_elements = file.readline().strip().split()
        koordinat=[]
        
        for i in range(rows):
            tmpkoor=[]
            tmpkoor.append(int(koordinat_elements[0]))
            tmpkoor.append(int(koordinat_elements[1]))
            koordinat.append(tmpkoor)
            koordinat_elements=file.readline().strip().split()
        
        return matrix,koordinat
    
# matrix,koordinat = readFile("test1.txt")

# print(matrix)
# print()
# print(koordinat)