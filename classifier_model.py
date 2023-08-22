from transformers import BertForSequenceClassification, BertTokenizer
import torch
import torch.nn.functional as F
import streamlit as st


model_path = r'dhikaardianto/TiktokSentimentIndoBertTwitter'

# Function to load model and tokenizer just once
@st.cache
def load_model():
  return BertForSequenceClassification.from_pretrained(model_path)

@st.cache
def load_tokenizer():
  return BertTokenizer.from_pretrained(model_path)

# Load a trained model and vocabulary that you have fine-tuned
model = load_model()
tokenizer = load_tokenizer()

# Copy the model to the CPU.
model.to('cpu')

i2w = {0: 'positive', 1: 'neutral', 2: 'negative'}


def klasifikasi_tiktok(review):
  subwords = tokenizer.encode(review)
  subwords = torch.LongTensor(subwords).view(1, -1).to(model.device)

  logits = model(subwords)[0]
  label = torch.topk(logits, k=1, dim=-1)[1].squeeze().item()

  return i2w[label], f'{F.softmax(logits, dim=-1).squeeze()[label] * 100:.3f}%'
    

