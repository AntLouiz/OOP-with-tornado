from motor.motor_tornado import MotorCollection



class CollectionManager:
    def __init__(self, collection):
        self.collection = collection

    def filter(self, **kwargs):
        query_filter = {}
        return query_filter

    async def find(self, query_filter={}, many=False, *args, **kwargs):
        if many:
            result = await self.collection.find(query_filter)
        else:
            result = await self.collection.find_one(query_filter)
        return result

    async def create(self, *args, **kwargs):
        result = await self.collection.insert_one(kwargs)
        return result

    async def update(self, *args, **kwargs):
        result = await self.collection.update_one(kwargs)
        return result

    async def aggregate(self, *args, **kwargs):
        pass

    async def remove(self, *args, **kwargs):
        result = await self.collection.remove_one(kwargs)
        return result
