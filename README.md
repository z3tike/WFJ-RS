# Neural Recommendation System (PyTorch)

This project is a machine learning-based recommendation system built with PyTorch.  
It demonstrates how a neural network can learn to rank and recommend videos based on user preferences and video statistics.

---

## Author

Developed by: **Zeteny Sovago**

---

## Project Goal

The goal of this project is to build a simple recommendation system that learns relationships between:

- User preferences (favorite topic)
- Video attributes (topic, views, likes, shares)
- Relevance score between a user and a video

The model outputs a score that can be used to rank videos for recommendation.

---

## System Overview

The system is trained on a dataset of user–video pairs.

Each training sample contains:

- User topic (encoded)
- Video topic (encoded)
- Video statistics (normalized features)
- Label (relevance score)

The neural network learns to predict how relevant a video is for a given user.

---

## Pipeline

Users + Videos
      |
      v
Dataset Construction
(user-video pairs)
      |
      v
Feature Encoding
- Topic encoding (ID / embedding)
- Normalized statistics (views, likes, shares)
      |
      v
Neural Network (PyTorch MLP)
      |
      v
Relevance Score Prediction
      |
      v
Loss Function (MSE / BCEWithLogits)
      |
      v
Backpropagation + Optimization
      |
      v
Trained Model
      |
      v
Recommendation Engine
(sort videos by predicted score)

---

## Model Input

The model receives three inputs:

- User topic
- Video topic
- Video statistics (views, likes, shares)

These inputs are combined and processed by a neural network to produce a single relevance score.

---

## Example Output

RECOMMENDATIONS

Video 2 - gaming
Score: 0.77

Video 1 - football
Score: 0.69

Video 4 - football
Score: 0.08

---

## Technologies Used

- Python
- PyTorch
- NumPy (optional)

---

## Key Concepts Learned

- Neural network-based recommendation systems
- Embedding vs one-hot encoding
- Feature normalization
- Ranking vs classification
- Dataset design for machine learning

---

## Future Improvements

- Replace pointwise training with pairwise ranking (A vs B)
- Add user history and sequential behavior
- Improve embedding representation of topics
- Introduce deeper architectures (MLP, attention-based models)
- Build a real-time recommendation API

---

## Notes

This is an educational project focused on understanding the fundamentals of recommendation systems. It is not intended for production use.
