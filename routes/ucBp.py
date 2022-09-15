#importando o blueprint
from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

#instanciar o blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
#    return "Teste"

#    db.create_all()

#Adiciona o acesso a banco e a chamada do template
    ucs_query = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_query)
