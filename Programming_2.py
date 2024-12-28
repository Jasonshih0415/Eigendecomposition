import cmath
#initial matrix
A = [[1,  6],
     [5,  2]]

B = [[2,  3],
     [3, -6]]

C = [[7,  2],
     [-4, 1]]

D = [[1,  1],
     [-1,  1]]

E = [[0,  0],
     [0,  0]]

class matrix_compute:
     def __init__(self):
          pass
     def set_matrix(self, matrix):
          self.matrix = matrix
          self.a = 1
          self.b = -(self.matrix[0][0] + self.matrix[1][1])
          self.c = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
          self.compute_eigenvalue()
     
     def compute_eigenvalue(self):
          if self.matrix == [[0, 0], [0, 0]]:
               print("lambda_1: 0")
               print("eigenvector_1: [0, 1]")
               print("lambda_2: 0")
               print("eigenvector_2: [1, 0]")
               return
          lambda_1 = (-(self.b)+cmath.sqrt(self.b**2-4*self.a*self.c))/2
          lambda_2 = (-(self.b)-cmath.sqrt(self.b**2-4*self.a*self.c))/2
          print("lambda_1:",lambda_1)
          self.compute_eigenvector(lambda_1)
          print("lambda_2:",lambda_2)
          self.compute_eigenvector(lambda_2)

     def compute_eigenvector(self,lambda_number):
          eigenvector=[]
          x1 = 1  
          if self.matrix[0][1] != 0:  
               scaler = -(self.matrix[0][0] - lambda_number) / self.matrix[0][1]
               x2 = x1 * scaler
               eigenvector.append(x1)
               eigenvector.append(x2)
          else:  
            eigenvector = [1, 0] if self.matrix[0][0] - lambda_number == 0 else [0, 1]
          print("eigenvector:", eigenvector)

def main():
     eigen=matrix_compute()
     print("matrixA:")
     eigen.set_matrix(A)
     print(" ")
     print("matrixB:")
     eigen.set_matrix(B)
     print(" ")
     print("matrixC:")
     eigen.set_matrix(C)
     print(" ")
     print("matrixD:")
     eigen.set_matrix(D)
     print(" ")
     print("matrixE:")
     eigen.set_matrix(E)


if __name__ == '__main__':
     main()