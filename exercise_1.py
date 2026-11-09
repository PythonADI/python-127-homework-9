phones = {"Natia": "566-1234", "Nika":"572-7883"}
print(f"Nika: {phones['Nika']}")
print(f"Lali: {phones.get('Lali', 'unknown')}")
phones["Lali"] = "598-1111"
phones["Natia"] = "555-0000"
print(f"Has Nika:{'Nika in phones'}")
removed_number = phones.pop("Nika")
print(f"Removed: {removed_number}")
print(phones)
print(f"{len(phones)} contacts")