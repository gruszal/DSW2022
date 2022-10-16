from datetime import datetime

konkretna_data = '2001-02-04'

# UWAGA! dostępne od wersji 3.7 Pythona
data = datetime.fromisoformat(konkretna_data)

print(data)
print(type(data))
