from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
deepseek = os.getenv("DEEPSEEK_KEY")

from my_array import topics
import sys
from linkedin_markdown import convert_markdown_to_unicode
from AIwork import AIwork

file_path = os.path.join(os.path.dirname(__file__), "counter.txt")
count = open(file_path, "r")
counter = int(count.read(1))

post_topic = topics[counter]
print(post_topic)

if counter > 99: 
    sys.exit(0)


completion = AIwork(post_topic=post_topic, deepseek=deepseek)

counter = counter + 1
with open(file_path, "w") as file:
    file.write(f"{counter}")

resulting_text = convert_markdown_to_unicode(completion.choices[0].message.content)
print(resulting_text)

with open(f"{os.path.dirname(__file__)}//posts//{post_topic}.txt", "w", encoding="utf-8") as file_2:
    file_2.write(resulting_text)


