# SoC
## Week-1: Introduction to Python

This week's assignment will cover the fundamentals of Python and introduce you to the world of programming with this powerful and versatile language :snake:.


## Week-2: Data Analysis and Interpretation
### Packages Required
```
    pip install -r packages.txt
```
In this week will focus on data analysis and interpretation, where we'll leverage the power of **Pandas**, **NumPy**, **SciPy**, and **Matplotlib** to work with structured data, perform calculations, conduct statistical analysis, and create impressive visualizations. We have done many kind of plots like **scatterplot**, **histogram**, **boxplot**, **Q-Q plots** and **Heatmap**. We have used pandas to convert our dataset **Iris.csv** to dataframe and operate on that. 

## Week-3: Linear and Logistic Regression

Assuming python packages are installed in Week-2 we don't require any new packages. 
In this week, we delved into Linear and Logistic regression, two fundamental machine learning algorithms. The exciting part is that we will implement both models using only **NumPy**, a powerful numerical computing library and analysed the data values using plots generated from **Matplotlib**. We have divided implementation of model into many functions such as **cost** and **derivatives of parameters**.

## Week-4: K-Means and Hierarchical Clustering
### Packages Required
```
    pip install -r requirements.txt
```
### K-Means Clustering
We performed k-means clustering on a given dataset of data points. We need to determine an appropriate value of **k** and then apply the k-means algorithm to cluster the data points accordingly. The classified data points are plotted for visualization.

### Hierarchical Clustering
We performed agglomerative clustering on the same dataset of data points. We'll plot the **dendrogram** to visualize the hierarchy and divide the points into **3, 4, 5, 6, and 7** clusters. We will explore different linkage methods (**ward**, **single linkage**, and **complete linkage**) and analyze how they affect the dendrogram and the clustering results

### Image Segmentation
We will investigate the use of k-means clustering for image segmentation. With various k values, we'll apply k-means clustering on an example image. The image will be transformed into data so that k-means can cluster it. This will provide us with a fundamental grasp of image segmentation using clustering, even if there are more complex techniques utilising deep learning packages like **PyTorch**, **tensorflow**.

## Week-5: Deep Neural Network Model

This week's assignment is an exciting one as we'll dive into the world of deep learning. We will implement an N-layer neural network from scratch using only **NumPy** and **Matplotlib** for visualization. Our objective is to train the neural network on the **make_moons()** dataset from the **scikit-learn** library.

## Project: Face Detection and Recognition
### Packages Required
```
    pip install tensorflow
```
![Face Recognition](https://tse3.mm.bing.net/th?id=OIP.yjRcia-9tJ1GBVHL0PsXvQHaD3&pid=Api&P=0&h=180)

In the last two weeks, we have implemented a Face Recognition Model using Convolutional Neural Networks (**CNNs**) and Feedforward Neural Networks in **TensorFlow**. This project will demonstrate your expertise in Machine Learning and Deep Learning, culminating in a powerful model that can recognize **4** different celebrities. 

For the face recognition model, we collected images of four different celebrities from **google**, **pinterest**. Each celebrity have at least **100** images, with each image containing only their face. Ensuring the images are face-only will significantly improve the accuracy of the model. 

Once we have our dataset, we will split it into **training** and **testing** sets. The testing set will contain 100 images, with **25** images for each celebrity. We have achieved an average accuracy of **85%** on this test set, demonstrating the effectiveness of our face recognition model.

The core of our project lies in designing the architecture of our face recognition model. We have used the power of **CNNs** and Feedforward Neural Networks to create a robust and accurate model. With the architecture in place, We have trained our model on the preprocessed training dataset, optimizing it for performance and accuracy with required **optimizer** and **loss function**.

After acheiving the required accuracy of testing we now save the model using **models.save()** function which has the directory where model is saved as input parameter. 
