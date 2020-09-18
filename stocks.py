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
    stock_list = [
        {
            "ticker": "ABEV",
            "name": "AMBEV",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segment",
            "description": "Faz cervejas e bebidas e afins. Faz cervejas e bebidas e afins. Faz cervejas e bebidas e afins. Faz cervejas e bebidas e afins. Faz cervejas e bebidas e afins."
        },
        {
            "ticker": "B3SA",
            "name": "B3",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "Intermedia a venda de ações e outros ativos. Intermedia a venda de ações e outros ativos. Intermedia a venda de ações e outros ativos. Intermedia a venda de ações e outros ativos."
        },
        {
            "ticker": "BBAS",
            "name": "Banco do Brasil",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "Banco mais antigo do Brasil. Banco mais antigo do Brasil. Banco mais antigo do Brasil. Banco mais antigo do Brasil. Banco mais antigo do Brasil. Banco mais antigo do Brasil. "
        },
        {
            "ticker": "BBDC",
            "name": "Bradesco",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. Bancão. "
        }
    ]        

    return stock_list