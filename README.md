# NCI-DOE-Collab-Pilot1-Autoencoder-Node-Saliency

### Description:
The purpose of this software is to identify the saliency of hidded nodes in autoencoders. This is done by ranking hidden nodes in the latent layer of the autoencoder according to their capability of performing a learning task.

### User Community: 
Experienced data scientists interested in understanding the mechanism of dimensionality reduction using autoencoder. 

### Usability:  
The repo contains two examples of scripts that process data from the popular public image classification datasets (MNIST), and preprocessed data from Genomics Data Common breast cancer cases.

### Uniqueness: 
The novelty of this method is discussed in this [paper](https://www.sciencedirect.com/science/article/pii/S0031320318304369?via%3Dihub). 
To explain what the trained autoencoders have learned when being unsupervised, the uniqueness of this methods lies in ranking hidden nodes in the autoencoder according to their capability of performing a learning task, identifying the specialty nodes that reveal explanatory input features, and suggesting possible nodes that can be trimmed down for a more concise network structure.

### Components: 
* Preprocessed data sets
* Python scripts to reproduce plots in the paper

### Technical Details:
Refer to this [README](./README-technical.md)
