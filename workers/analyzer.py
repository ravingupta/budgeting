# Currently its manually triggered, but it should be automated with queues
from transformers import pipeline

from models import db_get_categories

# Initialize the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define categories
labels = [c.name for c in db_get_categories()]

# Analyze transactions and assign categories
def define_category(description):
  result = classifier(description, labels)
  return result['labels'][0]
