from dataclasses import dataclass


@dataclass
class Shorts:
    id: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str
