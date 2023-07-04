class TreeStore:
    items: dict
    children: dict
    parent_ids: dict

    def __init__(self, items) -> None:
        self.items = {item['id']: item for item in items}
        self.children = {}
        self.parent_ids = {}
        for item in items:
            parent_id = item['parent']
            if parent_id is not None:
                self.children.setdefault(parent_id, []).append(item)
            self.parent_ids[item['id']] = parent_id

    def getAll(self) -> list:
        return list(self.items.values())

    def getItem(self, item_id, default=None) -> dict:
        return self.items.get(item_id, default)

    def getChildren(self, parent_id) -> list:
        return self.children.get(parent_id, [])

    def getAllParents(self, item_id) -> list:
        parent_id = self.parent_ids.get(item_id)
        parents = []
        while parent_id is not None:
            parent = self.items.get(parent_id)
            if parent is not None:
                parents.append(parent)
                parent_id = parent['parent']
            else:
                break
        return parents
