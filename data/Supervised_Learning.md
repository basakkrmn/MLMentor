# Supervised Learning

Supervised learning is a type of machine learning where the model is trained using **labeled data**. 
This means that each input in the dataset has a corresponding correct output (label). 
The goal is for the model to learn the mapping from inputs to outputs and make accurate predictions on new data.

## Key Algorithms

### Linear Regression
- Predicts a continuous value based on input features.
- Formula: `y = β0 + β1x1 + β2x2 + ... + βnxn`
- Example: Predicting house prices based on size, location, and number of rooms.

### Logistic Regression
- Predicts a probability for classification tasks (binary outcomes).
- Formula: `P(y=1) = 1 / (1 + e^-(β0 + β1x1 + ... + βnxn))`
- Example: Email spam detection (spam or not spam).

### Decision Trees
- Splits the data into branches based on feature values.
- Each leaf node represents a prediction or class.
- Pros: Easy to interpret.
- Cons: Can overfit if tree is too deep.

### Random Forest
- Ensemble of multiple decision trees.
- Reduces overfitting and improves generalization.

### Support Vector Machines (SVM)
- Finds the hyperplane that best separates classes.
- Can handle linear and non-linear classification with kernels.

### K-Nearest Neighbors (KNN)
- Predicts based on the closest examples in the training set.
- Distance metrics like Euclidean or Manhattan are used.

## Concepts
- **Features:** Input variables used to make predictions.
- **Labels:** Correct outputs for training.
- **Training Set:** The data used to train the model.
- **Test Set:** The data used to evaluate performance.
- **Overfitting:** When the model fits the training data too well and fails on new data.
- **Underfitting:** When the model is too simple to capture patterns in the data.

## Applications
- Email spam detection
- Credit risk prediction
- Sales forecasting
- Medical diagnosis
- Stock price prediction

