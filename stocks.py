def get_orderby_criterias():
    orderby_criterias = [
                {
                    "id": "0",
                    "description": "Valor de mercado"
                },
                {
                    "id": "1",
                    "description": "Nome"
                },
                {
                    "id": "2",
                    "description": "Patrimônio líquido"
                },
                {
                    "id": "3",
                    "description": "Ano de fundação"
                },
                {
                    "id": "4",
                    "description": "Ano de IPO"
                },
                {
                    "id": "5",
                    "description": "Anos lucrativos"
                }
            ]    

    return orderby_criterias

def get_filters():
    filters = [
        {
            "id": "0",
            "description": "Setor",
            "options": 
                [ 
                    {
                        "id": "0",
                        "description": "Setor 1"
                    },
                    {
                        "id": "1",
                        "description": "Setor 2"
                    },
                    {
                        "id": "2",
                        "description": "Setor 3"
                    },
                    {
                        "id": "3",
                        "description": "Setor 4"
                    }                
                ]
        },
        {
            "id": "1",
            "description": "Sub-Setor",
            "options": 
                [
                    {
                        "id": "0",
                        "description": "Sub-Setor 1"
                    },
                    {
                        "id": "1",
                        "description": "Oleo e Gas"
                    },
                    {
                        "id": "2",
                        "description": "Sub-Setor 3"
                    },
                    {
                        "id": "3",
                        "description": "Sub-Setor 4"
                    }      
                ]          

        }
    ]

    return filters

def get_stock_list():
    stock_list = ["ABEV", "B3SA", "BBAS", "BBDC", "CIEL", "COGN", "CVCB", "EGIE", "ENBR"]

    return stock_list