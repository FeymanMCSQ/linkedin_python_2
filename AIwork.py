from dotenv import load_dotenv
import os
from openai import OpenAI


def AIwork(post_topic, deepseek): 
    print(f"Well the deepsek key here is: {deepseek}")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key= deepseek,
    )

    completion = client.chat.completions.create(
        model=  "openai/o3-mini-high",
        messages=[
            {
            "role": "user",
            "content": f"""Pretend you are a writer who specializes on writing in Linkedin.Write a LinkedIn post on a trending topic from the realms of futurism, science, or technology. Topic {post_topic}. Your post should:

                Tone & Style: Adopt a warm, yet professional tone with a human touch—feel free to include a fictional short story to make the content relatable. 
                Structure: Be succinct and well-organized, using clear sections or bullet points if needed.
                Emojis: Integrate a few sparse, well-placed emojis (e.g., 😊, 🚀) to add personality without overwhelming the text.
                Content Quality: Ensure the post is informative, accessible (minimizing excessive technical jargon), and invites thoughtful discussion.
                Generate a high-quality, engaging post that meets these criteria. Consider that the post is going to
                be directly posted.""",
            }
        ]
    )

    return completion
