entries = ['146_Makowski', '181_Sobczak', '099_Malinowski', '048_Zając', '129_Krawczyk', '072_Kowalski',
           '188_Nowakowski', '002_Woźniak', '090_Czerwiński', '010_Kaczmarek', '106_Mazur', '053_Pietrzak']

dict_entries = {entry[:3]: entry[4:] for entry in entries}

print(dict_entries)
