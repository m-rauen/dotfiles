import numpy as np
import inspect 
from cli.out import output_onlyRMSD, output_onlyKabsch, output_fullResults


def calculateRMSD(matrix_P, matrix_Q): 
    if inspect.stack()[1][3] == 'inputFiles':
        result = round(np.sqrt(np.mean((matrix_P - matrix_Q) ** 2)), 4)
        output_onlyRMSD(result)
    elif inspect.stack()[1][3] == 'fullCalculation':
        result = round(np.sqrt(np.mean((matrix_P - matrix_Q) ** 2)), 4)
        return result
    
    
def calculateKabsch(matrix_P, matrix_Q): 
    if inspect.stack()[1][3] == 'inputFiles':
        #Calculate centroids to align coordinates at the center
        centroid1 = np.mean(matrix_P, axis=0)
        centroid2 = np.mean(matrix_Q, axis=0) 
        
        #Translate both matrices to the center (0,0,0)
        trans_matrixP = matrix_P -  np.tile(centroid1, (len(matrix_P),1)) 
        trans_matrixQ = matrix_Q - np.tile(centroid2, (len(matrix_Q),1))
        
        #Generate the covariance matrix
        matrix_H = np.matmul((np.transpose(trans_matrixQ)), matrix_P)
        
        #Calculate the SVD of the covariance matrix
        matrix_U, matrix_S, matrix_Vt = np.linalg.svd(matrix_H) 
        
        #Check for special reflection case in the covariance matrix
        #Then, based on the answer, calculate the proper rotation matrix
        if np.linalg.det(np.matmul(matrix_Vt, (np.transpose(matrix_U)))) < 0: 
            counter_identitiy = np.identity(len(matrix_Vt))
            matrix_Vt = np.matmul(counter_identitiy, matrix_Vt)
            matrix_R = np.matmul((np.transpose(matrix_U)), matrix_Vt)
        else:   
            matrix_R = np.matmul((np.transpose(matrix_U)), matrix_Vt)
            
        #Finally, calculate the rotated P matrix 
        rot_matrixP = np.matmul(matrix_P, matrix_R)
        
        
        output_onlyKabsch(matrix_R, rot_matrixP)
        
    elif inspect.stack()[1][3] == 'fullCalculation':
        #Calculate centroids to align coordinates at the center
        centroid1 = np.mean(matrix_P, axis=0)
        centroid2 = np.mean(matrix_Q, axis=0) 
        
        #Translate both matrices to the center (0,0,0)
        trans_matrixP = matrix_P -  np.tile(centroid1, (len(matrix_P),1)) 
        trans_matrixQ = matrix_Q - np.tile(centroid2, (len(matrix_Q),1))
        
        #Generate the covariance matrix
        matrix_H = np.matmul((np.transpose(trans_matrixQ)), matrix_P)
        
        #Calculate the SVD of the covariance matrix
        matrix_U, matrix_S, matrix_Vt = np.linalg.svd(matrix_H) 
        
        #Check for special reflection case in the covariance matrix
        #Then, based on the answer, calculate the proper rotation matrix
        if np.linalg.det(np.matmul(matrix_Vt, (np.transpose(matrix_U)))) < 0: 
            counter_identitiy = np.identity(len(matrix_Vt))
            matrix_Vt = np.matmul(counter_identitiy, matrix_Vt)
            matrix_R = np.matmul((np.transpose(matrix_U)), matrix_Vt)
        else:   
            matrix_R = np.matmul((np.transpose(matrix_U)), matrix_Vt)
            
        #Finally, calculate the rotated P matrix 
        rot_matrixP = np.matmul(matrix_P, matrix_R)
        

        return matrix_R, rot_matrixP

    
def fullCalculation(matrix_P, matrix_Q): 
    rmsd = calculateRMSD(matrix_P, matrix_Q)
    matrix_R, rot_matrixP = calculateKabsch(matrix_P, matrix_Q)
    output_fullResults(rmsd, matrix_R, rot_matrixP)
    
    
    
    
    
    
    
    
        

        
    
    
    
    
    
    
   
    

        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    