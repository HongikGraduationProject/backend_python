from dataclasses import dataclass, field
from typing import List


@dataclass
class ShortFormDownLoaded:
    video_code: str
    description: str
    file_name: str
    url: str
    title: str = ""
    keywords: List[str] = field(default_factory=list)


@dataclass
class ShortFormTextConverted:
    video_code: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str
    transcript: str


@dataclass
class ShortFormSummarized:
    video_code: str
    title: str
    description: str
    keywords: list
    url: str
    summary: str
    address: str
