from loader import dp
# from .is_admin import AdminFilter
from .successful_payment import SuccessfulPayment

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(SuccessfulPayment)
    pass
