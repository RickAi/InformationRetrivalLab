class Article:
    def __init__(self, index="", title="", author="", bubble="", content=""):
        self.content = content
        self.bubble = bubble
        self.author = author
        self.title = title
        self.index = index

    def generate_file_name(self):
        return str(self.index) + ".txt"

    def generate_file_content(self):
        return self.content
