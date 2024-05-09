from fastapi import APIRouter

router = APIRouter(prefix="")


@router.get("/")
async def root():
    """Empty method, just for test is app running"""

    return {"message": "Hi! For test, you should send POST request to the `/predict` endpoint, "
                       "with following parameters:",
            "body": {
                "longitude": 1.2,
                "latitude": 1.2,
                "housing_median_age": 1.2,
                "total_rooms": 1.2,
                "total_bedrooms": 1.2,
                "population": 1.2,
                "households": 1.2,
                "median_income": 1.2,
                "median_house_value": 1.2,
                "ocean_proximity": 'test',
            }}
