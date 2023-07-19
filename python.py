import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the pre-trained BERT model and tokenizer
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Define a function to predict the emotion from a given text
def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=1)
    predicted_label = torch.argmax(probabilities, dim=1)
    return predicted_label.item(), probabilities

# Test the function with sample text
sample_text = "I am feeling happy and excited!"
predicted_label, probabilities = predict_emotion(sample_text)

# Emotion labels for this model (0 to 4): very negative, negative, neutral, positive, very positive
emotion_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
print("Predicted Emotion:", emotion_labels[predicted_label])
print("Emotion Probabilities:", probabilities)