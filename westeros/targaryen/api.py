from ninja import Router
from targaryen.schemas import DragonOut


router = Router()


@router.get("/dragons", response=list[DragonOut])
def dragons(request):
    data = [
        DragonOut(name="Drogon", birth_year=298),
        DragonOut(name="Rhaegal", birth_year=298),
    ]

    return data
