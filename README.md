## Phishing Attack Domain Detection with Machine Learning
Enter any URL and our Machine Learning model will scan the URL and tell you if its malicious or not.
## Project Workflow
The project will follow the same approach as used in all ML project. We'll go through different stages of data collection,feature extraction,training and finally deployment of trained model.

- Data Collection
- Feature Extraction
- Model training & evaluation
- Deployment


## Data Collection

For this project we'll need bunch of legitimate and phishing url's,each categorised by (0) and (1). We'll use [this](https://www.kaggle.com/siddharthkumar25/malicious-and-benign-urls) dataset.

It contains 450k domain url's out of which 345k are legitimate and 104k are malicious. The Imbalanced dataset is oversampled using the SOMTE technique,which increases the total number of samples to around 600k.


## Feature Extraction

The dataset till now consist of only legit and malicious urls,in this stage we extract some useful features from these urls and further improve our dataset to make it more suitable for training ML models.

The below mentioned category of features are extracted from the URL data :
- Length based Features ( 5 features extracted)
- Count based Features ( 11 features extracted)
- Binary Features  ( 2 features extracted)


 All together 18 features are extracted from each url of the dataset.


## Model Training

The problem that we are trying to solve is a classification problem,more specifically a 'binary' classification problem. Classification problem comes under supervised machine learning. After feature extraction we'll train multiple ML models using our data and choose the model which gives us best accuracy.

The machine learning models considered to train the dataset in this project are :
- Decision Tree
- Random Forest
- Multilayer Perceptron




