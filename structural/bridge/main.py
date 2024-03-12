from restorant import Restorant
from kitchen.ukraine_kitchen import UkrainianKitchen
from kitchen.japanese_kitchen import JapaneseKitchen
from kitchen.american_kitchen import AmericanKitchen


def client_code(restorant: Restorant):
    print("----"*30)
    print("First dish:", restorant.order_first())
    print("Second dish:", restorant.order_second())
    print("Third dish:", restorant.order_third())
    print("Desert dish:", restorant.order_desert())

ukrainian_restorant = Restorant(UkrainianKitchen())
client_code(ukrainian_restorant)

japanese_restorant = Restorant(JapaneseKitchen())
client_code(japanese_restorant)

american_restorant = Restorant(AmericanKitchen())
client_code(american_restorant)
    


