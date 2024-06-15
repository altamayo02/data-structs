from services.JsonService import JsonService

class Exercises:
    @classmethod
    def inventory(cls):
        inventory: dict = {}

        def add(name, id, quantity, cost):
            inventory[name] = {
                "id": id,
                "cantidad_disponible": quantity,
                "costo_unitario": cost
            }
        
        def update_cost(name, new_cost):
            inventory[name]["costo_unitario"] = new_cost
        
        def remove(name):
            del inventory[name]
        
        def get_costiest():
            costiest = {
                "nombre": "Indefinido",
                "costo_unitario": math.inf
            }
            for product in inventory:
                if inventory[product]["costo_unitario"] < costiest["costo_unitario"]:
                    costiest = {
                        "nombre": product,
                        "costo_unitario": inventory[product]["costo_unitario"]
                    }
            return costiest

        print(20 * "-")
        add("Vino", 0, 20, 20000)
        add("Libra de arroz", 1, 120, 3000)
        add("Guaro", 2, 500, 0)
        
        print("Tiendita voltiarepas:", inventory)
        update_cost("Libra de arroz", 4000)
        print("Inflación:", inventory)
        print(inventory)
        print("Carero:", get_costiest())
        remove("Guaro")
        print("Adiós guaro:", inventory)
        print(20 * "-")

if __name__ == "__main__":
    Exercises.inventory()