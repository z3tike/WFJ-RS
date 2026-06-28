# Neural Recommendation System (PyTorch)

This project implements a simple neural network–based recommendation system using PyTorch.  
The model learns to predict how relevant a video is for a specific user based on topic matching and video engagement statistics.

---

## Author

Developed by: **z3tike**

---

## Project Overview

The system learns from user–video interaction pairs and predicts a relevance score for ranking videos.

It combines:

- User preferences (favorite topic)
- Video metadata (topic, views, likes, shares)
- Engineered features (normalized statistics)

The output is a continuous score used for recommendation ranking.

---

## System Architecture
                +------------------+
                |     USERS        |
                | favorite_topic   |
                +--------+---------+
                         |
                         v
                +------------------+
                |  DATASET BUILDER |
                | user-video pairs |
                +--------+---------+
                         |
                         v
    +------------------------------------------+
    |            FEATURE ENGINEERING           |
    |                                          |
    |  - Topic encoding (ID / embedding)       |
    |  - Normalize views                       |
    |  - Normalize likes                       |
    |  - Normalize shares                     |
    +------------------+-----------------------+
                         |
                         v
                +------------------+
                |  NEURAL NETWORK  |
                |   (PyTorch MLP)  |
                +--------+---------+
                         |
                         v
                +------------------+
                |  SCORE PREDICTION|
                |  relevance score |
                +--------+---------+
                         |
                         v
                +------------------+
                |      LOSS        |
                | MSE / BCEWithLogits |
                +--------+---------+
                         |
                         v
                +------------------+
                | BACKPROPAGATION  |
                | optimizer step   |
                +--------+---------+
                         |
                         v
                +------------------+
                |  TRAINED MODEL   |
                +--------+---------+
                         |
                         v
                +------------------+
                | RECOMMENDATIONS  |
                | sort by score    |
                +------------------+

---

## Input Representation

Each training sample contains:

- Encoded user topic
- Encoded video topic
- Normalized statistics:
  - views
  - likes
  - shares

These are concatenated into a single feature vector.

---

## Model Output

The model outputs a single scalar:

This score is used to rank videos for each user.

---

## Training Process

1. Create user–video pairs
2. Compute features
3. Compute label (relevance signal)
4. Forward pass through neural network
5. Compute loss
6. Backpropagation
7. Update weights using optimizer

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
- Neural Networks (MLP)
- Feature engineering

---

## Key Concepts

- Recommendation systems
- Ranking models
- Embedding / encoding
- Feature normalization
- Supervised learning (pointwise ranking)

---

## Future Improvements

- Pairwise ranking (A vs B training)
- User history / sequential modeling
- Embedding-based topic representation
- Attention-based models
- Real-time recommendation API
- Logging + evaluation metrics (NDCG, Recall@K)

---

## Notes

This project is an educational implementation of a recommendation system inspired by real-world platforms like YouTube and TikTok, simplified for learning purposes.
