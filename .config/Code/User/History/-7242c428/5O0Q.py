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
        trans_matrixP = matrix_P -  np.tile(centroid1, (3,1)) 
        trans_matrixQ = matrix_Q - np.tile(centroid2, (3,1))
        
        #Generate the covariance matrix
        matrix_H = (np.transpose(trans_matrixQ)) * trans_matrixP
        
        #Calculate the SVD of the covariance matrix
        matrix_U, matrix_S, matrix_Vh = np.linalg.svd(matrix_H) 
        
        #Check for special reflection case in the covariance matrix
        #Then, based on the answer, calculate the proper rotation matrix
        if np.linalg.det(matrix_Vh * (np.transpose(matrix_U))) < 0: 
            counter_identitiy = np.array([[1,0,0], [0,1,0], [0,0,-1]])
            matrix_R = (np.transpose(matrix_U)) * counter_identitiy * matrix_Vh
        else:   
            matrix_R = (np.transpose(matrix_U)) * matrix_Vh
            
        #Finally, calculate the rotated P matrix 
        rot_matrixP = matrix_R * matrix_P 
        
        output_onlyKabsch(matrix_R, rot_matrixP)
        
    elif inspect.stack()[1][3] == 'fullCalculation':
        #Calculate centroids to align coordinates at the center
        centroid1 = np.mean(matrix_P, axis=0)
        centroid2 = np.mean(matrix_Q, axis=0) 
        
        #Translate both matrices to the center (0,0,0)
        trans_matrixP = matrix_P -  np.tile(centroid1, (3,1)) 
        trans_matrixQ = matrix_Q - np.tile(centroid2, (3,1))
        
        #Generate the covariance matrix
        matrix_H = (np.transpose(trans_matrixQ)) * trans_matrixP
        
        #Calculate the SVD of the covariance matrix
        matrix_U, matrix_S, matrix_Vh = np.linalg.svd(matrix_H) 
        
        #Check for special reflection case in the covariance matrix
        #Then, based on the answer, calculate the proper rotation matrix
        if np.linalg.det(matrix_Vh * (np.transpose(matrix_U))) < 0: 
            counter_identitiy = np.array([[1,0,0], [0,1,0], [0,0,-1]])
            matrix_R = (np.transpose(matrix_U)) * counter_identitiy * matrix_Vh
        else:   
            matrix_R = (np.transpose(matrix_U)) * matrix_Vh
            
        #Finally, calculate the rotated P matrix 
        rot_matrixP = matrix_R * matrix_P 
        
        return matrix_R, rot_matrixP

    
def fullCalculation(matrix_P, matrix_Q): 
    rmsd = calculateRMSD(matrix_P, matrix_Q)
    matrix_R, rot_matrixP = calculateKabsch(matrix_P, matrix_Q)
    output_fullResults(rmsd, matrix_R, rot_matrixP)
    
    
    
    
    
    
    
    
        

        
    
    
    
    
    
    
   
    

        
       
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    