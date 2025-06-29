import json
import ssl
from urllib.request import urlopen
import sys


def main():
    article_name = condense_page_name(input("Enter name of Wikipedia article: "))
    if article_name == "":
        print("Please provide an article name.")
        return sys.exit(1)
    json_dict = get_json_dict(article_name)
    display_information(json_dict)


def condense_page_name(page_name: str) -> str:
    condensed_page_name = page_name.strip()
    condensed_page_name = condensed_page_name.replace(" ", "_")
    return condensed_page_name


def get_json_dict(condensed_page_name: str) -> dict:
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&meta=siteinfo&titles={condensed_page_name}&rvprop=user|timestamp&continue=&redirects&rvlimit=30&format=json"
    context = ssl._create_unverified_context()
    try:
        response = urlopen(url, context=context)
    except:
        print("Sorry there is a network error.")
        return sys.exit(3)
    return json.loads(response.read())


def display_information(json_dict: dict) -> None:
    try:
        for item in json_dict["query"]["redirects"]:
            print(f"Redirected from {item['from']} to {item['to']}\n")
    except:
        pass
    try:
        for item in json_dict["query"]["pages"].values():
            for revision in item["revisions"]:
                print(f"{revision['timestamp']} {revision['user']}\n")
    except:
        print("No article found.")
        return sys.exit(2)


if __name__ == "__main__":
   main()
