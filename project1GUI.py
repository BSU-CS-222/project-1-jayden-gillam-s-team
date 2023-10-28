import json
import ssl
from urllib.request import urlopen
import tkinter as tk


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Wikipedia Revisions")

        self.revisions = []
        self.articleTitleEntry = tk.Entry(root, width=50)
        self.queryButton = tk.Button(root, text="Query", command=self.query)
        self.revisionsList = tk.Listbox(root, width=50)

        self.articleTitleEntry.pack()
        self.queryButton.pack()
        self.revisionsList.pack()


    def query(self):
        entry = self.articleTitleEntry.get()
        if entry == "":
            entry = 1
        article_name = self.condense_page_name(entry)
        json_dict = self.get_json_dict(article_name)
        self.add_information(json_dict)
        self.UpdateList()


    def UpdateList(self):
        self.revisionsList.delete(0, tk.END)
        for revision in self.revisions:
            self.revisionsList.insert(tk.END, revision)
        self.revisions.clear()


    def get_json_dict(self, condensed_page_name):
        if condensed_page_name == 1:
            return 1
        url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&meta=siteinfo&titles={condensed_page_name}&rvprop=user|timestamp&continue=&redirects&rvlimit=30&format=json"
        context = ssl._create_unverified_context()
        try:
            response = urlopen(url, context=context)
        except:
            return 3
        return json.loads(response.read())


    def add_information(self, json_dict):
        if json_dict == 1:
            self.revisions.append("--NO ARTICLE NAME PROVIDED--")
            return
        elif json_dict == 3:
            self.revisions.append("--NETWORK ERROR--")
            return
        
        try:
            for item in json_dict["query"]["redirects"]:
                self.revisions.append(f"Redirected from {item['from']} to {item['to']}\n")
        except:
            pass
        try:
            for item in json_dict["query"]["pages"].values():
                for revision in item["revisions"]:
                    self.revisions.append(f"{revision['timestamp']} {revision['user']}\n")
        except:
            self.revisions.append("--ARTICLE NOT FOUND--")


    def condense_page_name(self, page_name):
        if page_name == 1:
            return 1
        
        condensed_page_name = page_name.strip()
        condensed_page_name = condensed_page_name.replace(" ", "_")
        return condensed_page_name



if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
