#importando o blueprint
from flask import Blueprint
from ..extensions import db
from ..models.uc import Uc

#instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
#    return "Teste"

    db.create_all()
