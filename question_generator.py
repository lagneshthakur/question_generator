from langchain_community.llms import HuggingFacePipeline
import torch
from transformers import T5Config, T5ForConditionalGeneration, T5Tokenizer
from transformers import pipeline

model_name = 'allenai/t5-small-squad2-question-generation'
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100
)

question_generator_pipeline = HuggingFacePipeline(pipeline=pipe)
# print(question_generator_pipeline.invoke('Paris is the capital of the country of France. It has long been one of western Europe\'s major centers of culture and business. Some of the world\'s greatest artists, writers, scholars, fashion designers, and chefs have lived in Paris.'))