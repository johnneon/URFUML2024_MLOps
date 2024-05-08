from fastapi import APIRouter
from app.schemas.HouseInfo import HouseInfo
from app.services.predict import predict as predict_fn

router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("")
async def predict(request: HouseInfo):
    """Method for predicting house price"""

    def prepare(data):
        res = {
            'longitude': data.longitude,
            'latitude': data.latitude,
            'housing_median_age': data.housing_median_age,
            'total_rooms': data.total_rooms,
            'total_bedrooms': data.total_bedrooms,
            'population': data.population,
            'households': data.households,
            'median_income': data.median_income,
            'median_house_value': data.median_house_value,
            'ocean_proximity': data.ocean_proximity,
        }

        return res

    result = predict_fn(prepare(request))
    return {'result': result}
