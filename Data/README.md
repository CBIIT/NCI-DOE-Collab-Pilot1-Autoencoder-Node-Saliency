# Data description
## MNIST dataset 
The MNIST database is available at (http://yann.lecun.com/exdb/mnist/).

- A_mnist_01.npy 	
Activation values of each node on the MNIST dataset containing digits 0 and 1. Each row represent a sample that are projected into the hidden nodes. Each column represent the activation values of the samples in a node.

- L_mnist_01.npy
Class labels of the MNIST digits. 0 indicates digit 0, and 1 indicates digit 1.

## GDC cancer dataset
The large collection of gene expression data on cancer is obtained from [GDC data portal] (https://portal.gdc.cancer.gov/).

- A_c32.npy 	
Activation values of each node on the breast cell dataset. Each row represent a sample that are projected into the hidden nodes. Each column represent the activation values of the samples in a node.
    
- L_c32.npy 	
Class labels of the breast cell dataset. 0 indicates normal cells, and 1 indicates cancer cells.
  

# Load the data
To load the .npy data and see what are the raw values one should use the numpy module.

```
import numpy as np
Data = np.load('./Data/A_c32.npy')
Print Data
```
