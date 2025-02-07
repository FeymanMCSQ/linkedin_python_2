from openai import OpenAI
from dotenv import load_dotenv
import os
from linkedin_poster import make_post
from github_commit import github_commit
from my_array import topics
import sys
from linkedin_markdown import convert_markdown_to_unicode
from AIwork import AIwork

def linkedinApp(): 
    load_dotenv()
    deepseek = os.getenv("MY_DEEP_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    URN = os.getenv("URN")

    print(f"Deepseek key: {deepseek}")

    file_path = os.path.join(os.path.dirname(__file__), "counter.txt")
    count = open(file_path, "r")
    counter = int(count.read(2))

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


    make_post(access_token=access_token, URN=URN, article=resulting_text)

    github_commit()


linkedinApp()