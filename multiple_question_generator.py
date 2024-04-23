from langchain_community.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

auth_token = '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'

model_name = 'ThomasGerald/mbart-multi-question-generation'
tokenizer = AutoTokenizer.from_pretrained(model_name, legacy=False, use_auth_token=auth_token)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=auth_token)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100
)

multiple_question_generator_pipeline = HuggingFacePipeline(pipeline=pipe)

def generate_multiple_questions(text):
    tokenized_text = tokenizer([text], return_tensors="pt")
    output =  model.generate(**tokenized_text, forced_bos_token_id=tokenizer.lang_code_to_id['en_XX'])
    delimited_string = tokenizer.batch_decode(output, skip_special_tokens=False)[0]
    delimited_string = delimited_string.replace('</s>', '')
    delimited_string = delimited_string.replace('en_XX ', '')
    return delimited_string.split('<question_sep> ')

# print(generate_multiple_questions('The dog is a pet animal. A dog has sharp teeth so that it can eat flesh very easily, it has four legs, two ears, two eyes, a tail, a mouth, and a nose. It is a very clever animal and is very useful in catching thieves. It runs very fast, barks loudly and attacks the strangers.'))