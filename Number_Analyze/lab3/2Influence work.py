import numpy as np
A = [['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
     ['Alice', 0, 1, 1, 0, 0, 0, 0, 0],
     ['Bob', 1, 0, 1, 0, 0, 0, 0, 0],
     ['Charlie', 1, 1, 0, 1, 0, 0, 0, 0],
     ['David', 0, 0, 1, 0, 1, 0, 0, 0],
     ['Eve', 0, 0, 0, 1, 0, 1, 0, 0],
     ['Frank', 0, 0, 0, 0, 1, 0, 1, 0],
     ['Grace', 0, 0, 0, 0, 0, 1, 0, 1],
     ['Hannah', 0, 0, 0, 0, 0, 0, 1, 0]]

individuals = [row[0] for row in A[1:]]
numeric_indices = {individuals[i]: i for i in range(len(individuals))}

numeric_matrix = np.zeros((len(individuals), len(individuals)))
for i in range(1, len(A)):
    for j in range(1, len(A[i])):
        numeric_matrix[i - 1][j - 1] = A[i][j]

eigenvalues, eigenvectors = np.linalg.eig(numeric_matrix)

dominant_index = np.argmax(eigenvalues)

dominant_eigenvalue = eigenvalues[dominant_index]
dominant_eigenvector = eigenvectors[:, dominant_index]

print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Corresponding Eigenvector:")
for i in range(len(individuals)):
    print(individuals[i], ":", dominant_eigenvector[i])
