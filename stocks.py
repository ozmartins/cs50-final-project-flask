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
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "B3SA",
            "name": "B3",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "BBAS",
            "name": "Banco do Brasil",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "BBDC",
            "name": "Bradesco",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "CIEL",
            "name": "Cielo",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "COGN",
            "name": "COGNA",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "CVCB",
            "name": "CVC",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "EGIE",
            "name": "ENGIE",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "ENBR",
            "name": "Energias do Brasil",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "EZTC",
            "name": "Ezetec",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "FLRY",
            "name": "Fleury",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "GRND",
            "name": "Grendene",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        },
        {
            "ticker": "GUAR",
            "name": "Guararapes",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        }
        ,
        {
            "ticker": "HGTX",
            "name": "Hering",
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segmento",
            "description": "A Ambev é uma empresa brasileira dedicada à produção e distribuição de bebidas, entre as quais cervejas, refrigerantes, energéticos, sucos, chás e água. A empresa esta presente em países das Américas e 30 marcas de bebidas, dentre elas Skol, Brahma, Stella Artois e Budweiser. Apenas no Brasil a empresa dispõe de 32 cervejarias e 2 maltarias."
        }
    ]        

    return stock_list