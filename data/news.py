
class News:
    def __init__(self, id, title, link, desc) -> None:
        self._id = id
        self._title = title
        self._link = link
        self._desc = desc

    def __str__(self) -> str:
        return f'id = {self.id}\ntitle = {self.title}\nlink = {self.link}\ndesc = {self.desc}'
        
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, News):
            return self.id == __o.id
        return False

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    @property
    def desc(self):
        return self._desc

    @id.setter
    def id(self, id):
        self._id = id

    @title.setter
    def title(self, title):
        self._title = title

    @link.setter
    def link(self, link):
        self._link = link

    @desc.setter
    def desc(self, desc):
        self._desc = desc

    