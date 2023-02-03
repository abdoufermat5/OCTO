from transformers import pipeline
import torch

analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)

SENTIMENT_LABELS = {
    "1 star": "Très négatif",
    "2 stars": "Négatif",
    "3 stars": "Neutre",
    "4 stars": "Positif",
    "5 stars": "Très positif"
}


def predict(text):
    res = analyzer(text)
    # get the label with the highest score
    highest_score = max(res, key=lambda x: x['score'])
    label = highest_score['label']
    return SENTIMENT_LABELS[label]
