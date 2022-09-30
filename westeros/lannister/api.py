from ninja import Router


router = Router()


@router.get("/home")
def home(request):
    return "A Lannister always pays their debts"

@router.get("/rock")
def rock(request, height):
    return f"Casterly Rock is {height}m tall"
