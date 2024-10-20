from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from schemas.category_schemas import CategorySchemas
from demo_data import category
from id_generater import generate_id

category_blp = Blueprint("category", __name__, description="Operations on category")

@category_blp.route("/category")
class Category(MethodView):
    @category_blp.response(200, CategorySchemas(many=True))
    def get(self):
        return category
    
    @category_blp.arguments(CategorySchemas)
    def post(self, requested_data):
        try:
            id = generate_id("category", requested_data["name"])
            
            new_cat = {
                "id" : id,
                **requested_data
            }
            category[id] = new_cat
            return new_cat
        except:
            abort(404, message = "Internal Server Error")

@category_blp.route("/category/<string:id>")
class Category_By_Id(MethodView):
    def get(self,id):
        return category[id]
    
    @category_blp.arguments(CategorySchemas)
    @category_blp.response(200, CategorySchemas)
    def put(self, requested_data, id):
        try:
            cat = category[id]
            
            cat.update({
                **requested_data
            })
            return cat
        except KeyError:
            abort(401, message="Category not found.")
    
    def delete(self, id):
        try:
            del category[id]
            return {"message": "Category Deleted"}
        except:
            abort(404, message = "Category not found")