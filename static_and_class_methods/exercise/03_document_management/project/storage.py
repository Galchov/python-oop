from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for element in self.categories:
            if element.id == category_id:
                element.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for element in self.topics:
            if element.id == topic_id:
                element.topic = new_topic
                element.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for element in self.documents:
            if element.id == document_id:
                element.file_name = new_file_name

    def delete_category(self, category_id):
        for element in self.categories:
            if element.id == category_id:
                self.categories.remove(element)

    def delete_topic(self, topic_id):
        for element in self.topics:
            if element.id == topic_id:
                self.topics.remove(element)

    def delete_document(self, document_id):
        for element in self.documents:
            if element.id == document_id:
                self.documents.remove(element)

    def get_document(self, document_id):
        for element in self.documents:
            if element.id == document_id:
                return element

    def __repr__(self):
        return '\n'.join([f'{document}' for document in self.documents])


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
