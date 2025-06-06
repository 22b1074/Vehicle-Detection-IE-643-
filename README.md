# Vehicle Detection using YOLOv5

This project is about detecting different types of vehicles using YOLOv5. It includes a Streamlit app where you can upload an image and see the detected vehicles.

---

## Dataset and Preprocessing

- The dataset I had gave **polygons instead of bounding boxes**, so I converted them by taking the min and max of x and y values.
- The dataset was **imbalanced**:
  - ~27,000 cars
  - ~6,000 bicycles
  - ~1,000 motorcycles, buses, and trucks

- To handle this:
  - I **removed images with more than 7 cars** to reduce the over-representation.
  - Then I did **data augmentation** (like flipping, brightness changes, cropping) on the images with fewer samples to get a more balanced dataset.

---

## Model Training

- I trained **YOLOv5** with 5 classes: `car`, `motorcycle`, `bicycle`, `bus`, and `truck`.
- For weather conditions like **fog and rain**, I followed a **few-shot approach**:
  - Took 3–4 images per condition
  - Used augmentation to make around 60 images per weather type
  - Then I fine-tuned the model with these

---

## Fine-tuning Strategy

- I **froze the early layers** of YOLOv5 since they already capture general features.
- I only trained the **later layers** to adapt to foggy/rainy conditions, which mostly affect high-level features.

---

## Streamlit Demo

You can try the model by running:

```bash
streamlit run Detect_Vehicles.py
