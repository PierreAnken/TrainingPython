
structure = \
    [
        {
            "nom": "Paulard",
            "prenom": "Paul",
            "telephones": [
                {"type": "domicile", "num": "123"},
                {"type": "prof", "num": "456"}
            ],
            "id": 2134567890,
            "contacts": [345678, 45678, 345678, 23456],
            "CV": {
                "date": "2023.02.12",
                "jobs": [
                    {
                    "debut": 2020,
                    "fin": 2021,
                    "description": "Vente au détail"
                    },
                    {
                        "debut": 2021,
                        "fin": "",
                        "description": "Gérante"
                    }
                ]
            }
        }
    ]

print(structure[0]["CV"]["jobs"][1]["debut"])