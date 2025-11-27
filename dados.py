import pandas as pd

pontos_londrina = [
    {
        "nome": "Lago Igapó",
        "descricao": "Principal cartão-postal de Londrina, ideal para caminhadas, esportes ao ar livre e lazer.",
        "latitude": -23.3286925,
        "longitude": -51.1720691,
        "icon": "tree",
        "prefix": "fa",
        "color": "darkblue",
        "tipo": "ponto_turistico"
    },
    {
        "nome": "Catedral Metropolitana de Londrina",
        "descricao": "Catedral moderna dedicada ao Sagrado Coração de Jesus, localizada no centro da cidade.",
        "latitude": -23.312160,
        "longitude": -51.159634,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura"
    },
    {
        "nome": "Jardim Botânico de Londrina",
        "descricao": "Área de preservação ambiental com trilhas ecológicas e rica biodiversidade.",
        "latitude": -23.3621947,
        "longitude": -51.1751885,
        "icon": "tree",
        "prefix": "fa",
        "color": "darkblue",
        "tipo": "ponto_turistico"
    },
    {
        "nome": "Museu Histórico Padre Carlos Weiss",
        "descricao": "Museu localizado no antigo prédio da estação ferroviária, preserva a história de Londrina e da ocupação do norte do Paraná.",
        "latitude": -23.3083253,
        "longitude": -51.1596058,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura"
    },
    {
        "nome": "Zerão (Complexo Esportivo José Antônio Basso)",
        "descricao": "Complexo esportivo com campos, pistas de caminhada e áreas de lazer, bastante frequentado pela população.",
        "latitude": -23.3248245,
        "longitude": -51.1640618,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura"
    },
    {
        "nome": "Restaurante Barolo Londrina",
        "descricao": "Restaurante especializado em carnes e gastronomia italiana.",
        "latitude": -23.316432041628744,
        "longitude": -51.16654702217959,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante"
    },
    {
        "nome": "Restaurante La Gondola",
        "descricao": "Restaurante de culinária italiana, tradicional em Londrina.",
        "latitude": -23.33242434217021,
        "longitude": -51.172955087362304,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante"
    },
    {
        "nome": "Restaurante Galpão Nobre",
        "descricao": "Espaço gastronômico e de eventos.",
        "latitude": -23.317690395795655,
        "longitude": -51.165260846633686,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante"
    },
    {
        "nome": "Restaurante Coco Bambu Londrina",
        "descricao": "Restaurante especializado em frutos do mar e pratos brasileiros.",
        "latitude": -23.341679868144812,
        "longitude": -51.1848083889616,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante"
    },
    {
        "nome": "Restaurante Bangkok Garden",
        "descricao": "Restaurante de culinária tailandesa.",
        "latitude": -23.319935345583854,
        "longitude": -51.15744258896249,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante"
    },
    {
        "nome": "Bourbon Londrina Hotel",
        "descricao": "Hotel de padrão alto, localizado na região central de Londrina.",
        "latitude": -23.31167302508058,
        "longitude": -51.16100315588057,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel"
    },
    {
        "nome": "Slaviero Essential Londrina Flat Hotel",
        "descricao": "Hotel moderno com estrutura para estadias curtas e longas.",
        "latitude": -23.315551072168827,
        "longitude": -51.15998830430503,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel"
    },
    {
        "nome": "Hotel Boulevard",
        "descricao": "Hotel tradicional localizado no centro de Londrina.",
        "latitude": -23.311635001927584,
        "longitude": -51.16517949081201,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel"
    },
    {
        "nome": "Hotel Thomasi",
        "descricao": "Hotel acessível e funcional, próximo a vias importantes da cidade.",
        "latitude": -23.300876525825842,
        "longitude": -51.18452510245611,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel"
    }
]

df = pd.DataFrame(pontos_londrina)