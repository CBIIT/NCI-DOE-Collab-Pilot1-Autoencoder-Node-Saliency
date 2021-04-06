# NCI-DOE-Collab-Pilot1-Autoencoder-Node-Saliency

### Description
The purpose of Autoencoder Node Saliency (ANS) is to identify the saliency of hidded nodes in autoencoders. This is done by ranking hidden nodes in the latent layer of the autoencoder according to their capability of performing a learning task. ANS explains the unsupervised learning process in autoencoders.

### User Community
Experienced data scientists interested in understanding the mechanism of dimensionality reduction using autoencoder. 

### Usability
The repository contains two examples of scripts that process data from the popular public image classification datasets (MNIST &#x1F534;_**(Question: What does MNIST stand for? Will the audience already know?) G.Z. yes it is known**_), and preprocessed data from Genomics Data Common breast cancer cases.

### Uniqueness
The following paper discusses the novelty of this method: [Autoencoder node saliency: Selecting relevant latent representations](https://www.sciencedirect.com/science/article/pii/S0031320318304369?via%3Dihub). 
The uniqueness of this method lies in ranking hidden nodes in the autoencoder according to their capability of performing a learning task, identifying the specialty nodes that reveal explanatory input features, and suggesting possible nodes that can be trimmed down for a more concise network structure. 

&#x1F534;_**(Question: Does this part fit in the previous sentence: "To explain what the trained autoencoders have learned when being unsupervised"?)G.Z., I removed that sentence**_

### Components
* Preprocessed data sets
* Python scripts to reproduce plots in the paper 

&#x1F534;_**(Question: Would it be okay to replace "paper" throughout with "article" or "publication"?) G.Z. Yes**_ 

### Technical Details
Refer to this [README](./README-technical.md).
