from ninja import Router


router = Router()


@router.get("/home")
def home(request):
    return "A Lannister always pays their debts"
