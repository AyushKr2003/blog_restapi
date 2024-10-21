from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CategoryModel
from schemas.category_schemas import CategorySchemas

category_blp = Blueprint("category", __name__, description="Operations on category")

@category_blp.route("/category")
class Category(MethodView):
    @category_blp.response(200, CategorySchemas(many=True))
    def get(self):
        categories = CategoryModel.query.all()
        return categories
    
    @category_blp.arguments(CategorySchemas)
    @category_blp.response(201, CategorySchemas)
    def post(self, requested_data):
        category = CategoryModel(**requested_data)
        try:
            # id = generate_id("category", requested_data["name"])
            
            # new_cat = {
            #     "id" : id,
            #     **requested_data
            # }
            # category[id] = new_cat
            # return new_cat
            db.session.add(category)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(404, message = f"Internal Server Error. {e}")
        return category

@category_blp.route("/category/<int:id>")
class Category_By_Id(MethodView):
    def get(self,id):
        category = CategoryModel.query.get_or_404(id)
        return category
    
    @category_blp.arguments(CategorySchemas)
    @category_blp.response(200, CategorySchemas)
    def put(self, requested_data, id):
        # try:
        #     cat = category[id]
            
        #     cat.update({
        #         **requested_data
        #     })
        #     return cat
        # except KeyError:
        #     abort(401, message="Category not found.")
        category = CategoryModel.query.get(id)
        
        category.name = requested_data["name"]
        
        if not category:
            abort(404, message = "Category not found")
        
        try:
            db.session.add(category)
            db.session.commit()
            return category
        except SQLAlchemyError as e:
            abort(404, message = f"Internal Server Error. {e}")
    
    def delete(self, id):
        # try:
        #     del category[id]
        #     return {"message": "Category Deleted"}
        # except:
        #     abort(404, message = "Category not found")
        category = CategoryModel.query.get_or_404(id)
        raise NotImplementedError("Under Development")