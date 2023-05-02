from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.crystal import Crystal

# class Crystal: 
#     def __init__(self, id, name, color, powers):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.powers = powers
        
# # create a list of crystals
# crystals = [
#     Crystal(1, "Amethyst", "Purple", "Infinit knowledge"), 
#     Crystal(2, "Tiger's Eye", "Gold", "Confidence, strength"), 
#     Crystal(3, "Rose Quartz", "Pink", "Love")
# ]

# responsible for validating and
# returning the instance of the crystal that is found
# def validate_crystal(crystal_id):
#     try: 
#         crystal_id = int(crystal_id)
#     except:
#         abort(make_response({"message" :f"crystal {crystal_id} is not a valid type ({type(crystal_id)}. Must be an integer.)"}, 400))

#     for crystal in crystals:
#         if crystal.id == crystal_id:
#             return crystal
    
#     abort(make_response({"message" :f"crystal {crystal_id} does not exist"}, 400))


# @crystal_bp.route("", methods = ["GET"])

# def handle_crystals():
#     crystal_response = []
    
#     for crystal in crystals:
#         crystal_response.append({
#             "id": crystal.id, 
#             "name": crystal.name, 
#             "color": crystal.color, 
#             "powers": crystal.powers
#         })
#     return jsonify(crystal_response)

    
    
    


crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# @crystal_bp.route("/<crystal_id>", methods = ["GET"])

# defining a route for creating a crystal resource
# def handle_crystal(crystal_id):
#     crystal = validate_crystal(crystal_id)
    
#     return {
#         "id": crystal.id,
#         "name": crystal.name, 
#         "color": crystal.color, 
#         "powers": crystal.powers
#     }


# responsible for validating and
# returning the instance of the crystal that is found
def validate_crystal(crystal_id):
    try: 
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message" :f"crystal {crystal_id} is not a valid type ({type(crystal_id)}. Must be an integer.)"}, 400))
    
    crystal = Crystal.query.get(crystal_id)
    
    if not crystal:
        abort(make_response({"message" :f"crystal {crystal_id} does not exist"}, 404))
        
    return crystal



# define a route for creating a crystal resource
@crystal_bp.route("", methods=['POST'])
def handle_crystals():
    request_body = request.get_json()
    
    new_crystal = Crystal(
        name = request_body["name"], 
        color = request_body["color"], 
        powers = request_body["powers"]
    )
    
    db.session.add(new_crystal)
    db.session.commit()
    
    return make_response(f"Yaaaayyy Crystal {new_crystal.name} successfully created!", 201)


# define a route for getting all crystals
@crystal_bp.route("", methods = ["GET"])
def read_all_crystals():
    crystals_response = []
    crystals = Crystal.query.all()
    
    for crystal in crystals: 
        crystals_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })
        
    return jsonify(crystals_response)
        
        
# define a route for getting a single crystal
# GET /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods = ["GET"])

def read_one_crystal(crystal_id):
    # query our db to grab the crystal that has the id we want
    # crystal = Crystal.query.get(crystal_id)
    crystal = validate_crystal(crystal_id)

    
    #  show a single crystal
    return {
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers, 
        "id": crystal.id
    }, 200
    
    
    
    # define a route for updating a crystal
    # PUT /CRYSTALS/<CRYSTAL_ID>
@crystal_bp.route("/<crystal_id>", methods = ["PUT"])
def update_crystal(crystal_id):
    # query our db to grab the crystal that has the id we want
    # crystal = Crystal.query.get(crystal_id)
    crystal = validate_crystal(crystal_id)

    
    request_body = request.get_json()
    
    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]
    
    db.session.commit()
    
    # send back the updated crystal
    return {
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers, 
        "id": crystal.id
        
    }, 200
    

# DEFINE A ROUTE FOR DELETING A CRYSTAL

@crystal_bp.route("/<crystal_id>", methods=["DELETE"])
def delete_crystal(crystal_id):
    # crystal = Crystal.query.get(crystal_id)
    crystal = validate_crystal(crystal_id)

    
    db.session.delete(crystal)
    db.session.commit()
    
    return make_response(f"Crystal #{crystal.id} successfully deleted")