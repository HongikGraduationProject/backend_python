from dataclasses import dataclass


@dataclass
class ShortsDownloaded:
    uuid: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str


@dataclass
class ShortsTextConverted:
    uuid: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str
    transcript: str


@dataclass
class ShortsSummarized:
    uuid: str
    title: str
    description: str
    keywords: list
    url: str
    summary: str
