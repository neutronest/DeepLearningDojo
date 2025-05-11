import torch
import matplotlib.pyplot as plt
from transformers import BertForSequenceClassification, BertTokenizer, Trainer, TrainingArguments
from transformers.trainer_callback import TrainerCallback
from datasets import load_dataset

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    dataset = load_dataset("glue", "sst2")
    model_cache_path = "/mnt/e/HF_HOME/models/bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", cache_dir=model_cache_path)
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", cache_dir=model_cache_path)
    model.to(device)
    import pdb;pdb.set_trace()