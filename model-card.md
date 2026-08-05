# Model Card: Garbage Image Classification using ResNet50

## Model Details

| Field | Details |
|--------|---------|
| **Model Name** | Garbage Image Classification |
| **Architecture** | ResNet50 (Residual Network) |
| **Framework** | TensorFlow / Keras |
| **Model Type** | Deep Convolutional Neural Network (CNN) |
| **Task** | Multi-class Image Classification |
| **Input Size** | 180 × 180 × 3 RGB Images |
| **Number of Classes** | 12 |
| **Training Strategy** | Transfer Learning using pretrained ResNet50 backbone with custom classification head |

### Model Description

ResNet50 (Residual Network) is a deep convolutional neural network consisting of 50 layers that introduced **residual learning** through **skip connections**. These residual connections help alleviate the vanishing gradient problem, allowing significantly deeper neural networks to be trained effectively.

For this project, ResNet50 was fine-tuned using transfer learning to classify images of garbage into one of twelve waste categories.

---

# Intended Use

## Primary Use

This model is intended to automatically classify waste images into predefined categories to support waste segregation and recycling workflows.

Possible applications include:

- Smart waste management systems
- Automated recycling facilities
- Educational waste segregation tools
- Mobile applications for garbage identification
- Environmental sustainability projects

## Intended Users

- Environmental organizations
- Municipal waste management agencies
- Recycling centers
- Students and researchers
- Smart city applications

---

# Out-of-Scope Use

This model is **not intended** for:

- Object detection or localization
- Instance segmentation
- General object recognition
- Medical or safety-critical image classification
- Images containing multiple waste objects requiring separate predictions
- Classification of waste categories outside the 12 trained classes

---

# Training Data

## Dataset Summary

| Split | Images |
|--------|-------:|
| Training | 10,854 |
| Validation | 2,321 |
| Testing | 2,340 |
| **Total** | **15,515** |

### Image Specifications

- Resolution: **180 × 180**
- Color Space: RGB
- Number of Classes: **12**

---

## Class Distribution

| Class | Images |
|--------|-------:|
| Battery | 945 |
| Biological | 985 |
| Brown Glass | 607 |
| Cardboard | 891 |
| Clothes | 5,325 |
| Green Glass | 629 |
| Metal | 769 |
| Paper | 1,050 |
| Plastic | 865 |
| Shoes | 1,977 |
| Trash | 697 |
| White Glass | 775 |

---

# Model Performance

## Overall Metrics

| Metric | Score |
|---------|-------:|
| Accuracy | **0.9291** |
| Macro Precision | **0.9035** |
| Macro Recall | **0.8959** |
| Macro F1-score | **0.8978** |
| Weighted Precision | **0.9316** |
| Weighted Recall | **0.9291** |
| Weighted F1-score | **0.9290** |

---

## Performance Interpretation

### Accuracy (92.91%)

Approximately **93%** of test images were classified correctly.

### Macro Precision (90.35%)

The model maintains high precision across all classes by treating each class equally, regardless of its size.

### Macro Recall (89.59%)

The model successfully identifies most samples across all waste categories, though performance may vary for smaller classes.

### Macro F1-score (89.78%)

This indicates balanced classification performance across all categories, including minority classes.

### Weighted Metrics

The weighted precision, recall, and F1-score are all approximately **93%**, indicating strong overall performance while accounting for class frequency. These scores are influenced more heavily by larger classes, such as **Clothes**.

---

# Factors

Model predictions are influenced by:

- Object appearance
- Object shape
- Texture
- Color
- Lighting conditions
- Image quality
- Background clutter
- Camera angle
- Occlusion
- Similar visual characteristics between waste categories

---

# Evaluation Data

The model was evaluated on a held-out test dataset consisting of **2,340 images** spanning all **12 waste categories**.

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score

Both **macro** and **weighted** averages were reported to account for class imbalance.

---

# Limitations

- Dataset exhibits class imbalance, particularly for the **Clothes** class, which contains substantially more samples than other categories.
- Performance may decrease for images captured under poor lighting or low resolution.
- Similar-looking materials (e.g., different glass types or plastic vs. trash) may occasionally be confused.
- The model assumes a single dominant waste object per image.
- The model may not generalize well to waste categories that were not present during training.

---

# Ethical Considerations

- Incorrect predictions may lead to improper waste segregation.
- The model should be used as a decision-support tool rather than a fully autonomous system in critical waste processing environments.
- Performance should be periodically evaluated as new waste materials or image distributions emerge.

---

# Recommendations

- Collect additional images for underrepresented classes to reduce class imbalance.
- Apply data augmentation to improve robustness under varying environmental conditions.
- Retrain periodically with newer datasets to improve generalization.
- Evaluate the model on real-world deployment images before production use.
- Consider deploying a confidence threshold to flag uncertain predictions for manual review.

---

# Summary

The ResNet50-based garbage classification model achieves **92.91% accuracy** on a 12-class waste classification task. The model demonstrates strong overall performance, with balanced macro metrics indicating good capability across both majority and minority classes. While the model is suitable for automated waste classification applications, continued improvements in dataset balance and real-world validation can further enhance reliability.
