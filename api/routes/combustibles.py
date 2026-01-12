from flask import Blueprint
from api.services.data_loader import (
    get_combustibles_by_provincia,
    get_combustibles_by_empresa,
    get_promedio_combustible,
)
from api.utils.responses import success, error

combustibles_bp = Blueprint("combustibles", __name__, url_prefix="/api/combustibles")


@combustibles_bp.route("/provincia/<provincia>", methods=["GET"])
def combustibles_por_provincia(provincia):
    data = get_combustibles_by_provincia(provincia)
    if not data:
        return error("No se encontraron gasolineras para esa provincia", 404)
    return success(data)


@combustibles_bp.route("/empresa/<empresa>", methods=["GET"])
def combustibles_por_empresa(empresa):
    data = get_combustibles_by_empresa(empresa)
    if not data:
        return error("No se encontraron gasolineras para esa empresa", 404)
    return success(data)


@combustibles_bp.route("/promedio/<provincia>/<combustible>", methods=["GET"])
def promedio_combustible(provincia, combustible):
    promedio = get_promedio_combustible(provincia, combustible)

    if promedio is None:
        return error("No hay datos suficientes para calcular el promedio", 404)

    return success(
        {
            "provincia": provincia.lower(),
            "combustible": combustible.replace("-", " ").title(),
            "precio_promedio": promedio,
        }
    )
