from openai import OpenAI
from env import settings
from dataclasses import asdict
from resources.static.prompts import PROMPT, SHORTS_EXAMPLE
from dto.shorts import ShortsSummarized
import json

API_KEY = settings.API_KEYS['OPENAI']

client = OpenAI(api_key=API_KEY)


def summarize_short(text_converted):
    shorts_json = json.dumps(asdict(text_converted), ensure_ascii=False)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": shorts_json},
            {"role": "system", "content": PROMPT["SHORTS_SUMMARIZE_KOR"]}
        ]
    )
    summary_json = json.loads(completion.choices[0].message.content)
    print(summary_json)
    return ShortsSummarized(
        uuid=text_converted.uuid,
        title=text_converted.title,
        description=text_converted.description,
        keywords=summary_json["keywords"],
        url=text_converted.url,
        summary=summary_json["summary"]
    )
    # return completion.choices[0].message.content


def summarize_short_tmp():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "user", "content": SHORTS_EXAMPLE["JAPAN_TRAVEL"]},
            {"role": "system", "content": PROMPT["SHORTS_SUMMARIZE_KOR"]}
        ]
    )
    print(completion)


# summarize_short_tmp()
