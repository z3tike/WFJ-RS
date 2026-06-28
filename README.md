# 🎯 Simple Neural Recommendation System

This project is a beginner-friendly machine learning recommendation system built with PyTorch.  
It demonstrates how a neural network can learn to recommend videos based on user preferences and video statistics.

---

## 👤 Author

Developed by: **Zeteny Sovago**

---

## 🚀 Project Goal

The goal of this project is to build a simple video recommendation system that learns:

- User preferences (topics)
- Video metadata (views, likes, shares)
- Relevance between users and videos

The model predicts how relevant a video is for a specific user.

---

## 🧠 How it works

The system learns from a dataset of:

- Users (favorite topic)
- Videos (topic + statistics)
- Labels (how relevant a video is for a user)

The neural network outputs a relevance score.

---

## 🔄 Pipeline Overview

Users + Videos
      │
      ▼
Dataset Builder
(create user-video pairs)
      │
      ▼
Feature Encoding
(topic → embedding / id)
(stats → normalized values)
      │
      ▼
Neural Network (PyTorch)
      │
      ▼
Prediction Score
      │
      ▼
Loss Function (MSE / BCEWithLogits)
      │
      ▼
Backpropagation (training)
      │
      ▼
Trained Recommendation Model
      │
      ▼
Recommendation Engine
(sort videos by score)

---

## 📦 Features

- Neural network-based recommendation model
- Topic encoding (embedding / ID mapping)
- Normalized video statistics (views, likes, shares)
- Custom dataset generator
- Ranking-based recommendation output

---

## 🏗️ Model Architecture

The model takes three inputs:

- User topic
- Video topic
- Video statistics

And outputs:

- A relevance score

---

## 📊 Example Output

===== RECOMMENDATIONS =====

Video 2 - gaming
Score: 0.77

Video 1 - football
Score: 0.69

Video 4 - football
Score: 0.08

---

## 🧪 Technologies Used

- Python
- PyTorch
- NumPy (optional)
- Basic feature engineering

---

## 📚 What I learned

- How embedding-based models work
- How recommendation systems are trained
- Difference between classification and ranking
- Importance of dataset design in ML

---

## 🚀 Future improvements

- Replace label-based training with pairwise ranking (A vs B)
- Add user history / watch time
- Improve embedding space for topics
- Add deeper neural architectures
- Build real-time recommendation API

---

## 🧠 Real-world analogy

This project is a simplified version of systems used in:

- YouTube recommendations
- TikTok feed ranking
- Instagram explore feed

---

## ⚠️ Note

This is an educational project and not a production system.  
It is designed to understand the fundamentals of recommendation systems.