from dataclasses import dataclass


@dataclass
class ShortFormDownLoaded:
    uuid: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str


@dataclass
class ShortFormTextConverted:
    uuid: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str
    transcript: str


@dataclass
class ShortFormSummarized:
    uuid: str
    title: str
    description: str
    keywords: list
    url: str
    summary: str
