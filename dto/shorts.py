from dataclasses import dataclass


@dataclass
class ShortsDownloaded:
    id: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str


@dataclass
class ShortsTextConverted:
    id: str
    title: str
    description: str
    file_name: str
    keywords: list
    url: str
    transcript: str


