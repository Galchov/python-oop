from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = [d for d in self.documents if d.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.categories = [c for c in self.categories if c.id != category_id]
        # Or
        # for category_obj in self.categories:
        #     if category_obj.id == category_id:
        #         self.categories.remove(category_obj)
        #         return None

    def delete_topic(self, topic_id: int) -> None:
        self.topics = [t for t in self.topics if t.id != topic_id]
        # Or
        # for topic_obj in self.topics:
        #     if topic_obj.id == topic_id:
        #         self.topics.remove(topic_obj)
        #         return None

    def delete_document(self, document_id: int) -> None:
        self.documents = [d for d in self.documents if d.id != document_id]
        # Or
        # for document_obj in self.documents:
        #     if document_obj.id == document_id:
        #         self.documents.remove(document_obj)
        #         return None

        # Or you can also
        # self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id: int) -> "Document":
        return [doc for doc in self.documents if doc.id == document_id][0]

    def __repr__(self) -> str:
        documents = [str(doc) for doc in self.documents]
        return "\n".join(documents)
