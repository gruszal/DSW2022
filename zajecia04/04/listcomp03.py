from countries import countries

# Państwa o nazwie dłuższej niż 13 znaków
result1 = [name for name in countries if len(name) > 13]
print(result1)
