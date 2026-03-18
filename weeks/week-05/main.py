from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional


@strawberry.type
class Item:
    id: int
    name: str
    sku: str



items_db: List[Item] = []



@strawberry.type
class Query:
    @strawberry.field
    def items(self) -> List[Item]:
        return items_db

    @strawberry.field
    def item(self, id: int) -> Optional[Item]:
        for item in items_db:
            if item.id == id:
                return item
        return None



@strawberry.type
class Mutation:
    @strawberry.mutation
    def createItem(self, name: str, sku: str) -> Item:
        new_item = Item(
            id=len(items_db) + 1,
            name=name,
            sku=sku
        )
        items_db.append(new_item)
        return new_item



schema = strawberry.Schema(query=Query, mutation=Mutation)



app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
