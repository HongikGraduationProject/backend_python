from openai import OpenAI
from env import settings
from dataclasses import asdict
from resources.static.prompts import PROMPT, SHORTS_EXAMPLE
from dto.shortform import ShortFormSummarized
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
            {"role": "system", "content": PROMPT["SHORTS_SUMMARIZE_KOR_TEST"]}
        ]
    )
    summary_json = json.loads(completion.choices[0].message.content)
    print(summary_json)
    return ShortFormSummarized(
        uuid=text_converted.uuid,
        title=summary_json["title"],
        description=text_converted.description,
        keywords=summary_json["keywords"],
        url=text_converted.url,
        summary=summary_json["summary"],
        address=summary_json["address"]
    )

