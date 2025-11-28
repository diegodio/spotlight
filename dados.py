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
        "tipo": "ponto_turistico",
        "historia": (
            "O Lago Igapó foi formado a partir do represamento do Ribeirão Cambé e "
            "inaugurado em 10 de dezembro de 1959, no Jubileu de Prata de Londrina. "
            "A obra resolveu problemas de drenagem na região e, com o tempo, o lago "
            "ganhou projeto paisagístico de Roberto Burle Marx, tornando-se um dos "
            "símbolos da cidade e polo de lazer e esportes."
        )
    },
    {
        "nome": "Catedral Metropolitana de Londrina",
        "descricao": "Catedral moderna dedicada ao Sagrado Coração de Jesus, localizada no centro da cidade.",
        "latitude": -23.312160,
        "longitude": -51.159634,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura",
        "historia": (
            "A história da catedral acompanha a própria formação de Londrina. "
            "A primeira igreja, em madeira, data de 1934. Com o crescimento da cidade, "
            "novos projetos foram sendo feitos até chegar à atual catedral em estilo moderno, "
            "projetada pelos arquitetos Edoardo Rosso e Yoshimasa Kimachi e inaugurada na década "
            "de 1970. O templo, dedicado ao Sagrado Coração de Jesus, tornou-se marco visual e "
            "religioso no coração da cidade."
        )
    },
    {
        "nome": "Jardim Botânico de Londrina",
        "descricao": "Área de preservação ambiental com trilhas ecológicas e rica biodiversidade.",
        "latitude": -23.3621947,
        "longitude": -51.1751885,
        "icon": "tree",
        "prefix": "fa",
        "color": "darkblue",
        "tipo": "ponto_turistico",
        "historia": (
            "O Jardim Botânico de Londrina foi criado como área de preservação e estudo da flora "
            "regional, reunindo espécies nativas e exóticas em um espaço voltado tanto para "
            "pesquisa quanto para educação ambiental. Com o tempo, tornou-se também um importante "
            "ponto de lazer, trilhas e contemplação para moradores e visitantes."
        )
    },
    {
        "nome": "Museu Histórico Padre Carlos Weiss",
        "descricao": "Museu localizado no antigo prédio da estação ferroviária, preserva a história de Londrina e da ocupação do norte do Paraná.",
        "latitude": -23.3083253,
        "longitude": -51.1596058,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura",
        "historia": (
            "O Museu Histórico de Londrina “Padre Carlos Weiss” começou suas atividades em 1970, "
            "nos porões do Colégio Hugo Simas, a partir da iniciativa de professores e estudantes "
            "do curso de História. Em 1974 passou a ser órgão suplementar da UEL e, em 1986, foi "
            "transferido para o prédio da antiga estação ferroviária. Hoje, guarda um grande acervo "
            "de documentos, objetos e fotografias que contam a história da cidade e da região norte do Paraná."
        )
    },
    {
        "nome": "Zerão (Complexo Esportivo José Antônio Basso)",
        "descricao": "Complexo esportivo com campos, pistas de caminhada e áreas de lazer, bastante frequentado pela população.",
        "latitude": -23.3248245,
        "longitude": -51.1640618,
        "icon": "map-marked",
        "prefix": "fa",
        "color": "red",
        "tipo": "cultura",
        "historia": (
            "Conhecido popularmente como Zerão, o Centro de Recreação e Lazer Luigi Borghesi se consolidou "
            "como um dos principais espaços de convivência de Londrina, reunindo esporte, lazer e cultura. "
            "O local abriga pistas de caminhada, quadras e o anfiteatro Jonas Dias Martins, que recebe eventos "
            "como o Festival Internacional de Londrina (FILO), apresentações musicais e atividades artísticas ao ar livre."
        )
    },
    {
        "nome": "Restaurante Barolo Londrina",
        "descricao": "Restaurante especializado em carnes e gastronomia italiana.",
        "latitude": -23.316432041628744,
        "longitude": -51.16654702217959,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante",
        "historia": (
            "O Barolo Londrina faz parte de uma tradicional casa de gastronomia inspirada na culinária italiana, "
            "que se destacou na cidade pela combinação de massas artesanais, cortes de carne selecionados e carta "
            "de vinhos robusta. Com ambiente sofisticado e atendimento voltado à experiência do cliente, tornou-se "
            "referência para comemorações e encontros de negócios."
        )
    },
    {
        "nome": "Restaurante La Gondola",
        "descricao": "Restaurante de culinária italiana, tradicional em Londrina.",
        "latitude": -23.33242434217021,
        "longitude": -51.172955087362304,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante",
        "historia": (
            "O La Gondola figura entre os restaurantes italianos mais tradicionais de Londrina, conhecido por "
            "sua atmosfera aconchegante e cardápio que reúne massas, risotos e pratos clássicos. Ao longo dos anos, "
            "acabou se tornando ponto de encontro de famílias e amigos, especialmente em datas comemorativas."
        )
    },
    {
        "nome": "Restaurante Galpão Nobre",
        "descricao": "Espaço gastronômico e de eventos.",
        "latitude": -23.317690395795655,
        "longitude": -51.165260846633686,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante",
        "historia": (
            "O Galpão Nobre surgiu como um espaço versátil, unindo restaurante e área para eventos sociais e corporativos. "
            "Sua proposta combina gastronomia com estrutura para festas, formaturas e confraternizações, o que o tornou "
            "uma opção recorrente para quem busca ambiente amplo e bem estruturado na cidade."
        )
    },
    {
        "nome": "Restaurante Coco Bambu Londrina",
        "descricao": "Restaurante especializado em frutos do mar e pratos brasileiros.",
        "latitude": -23.341679868144812,
        "longitude": -51.1848083889616,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante",
        "historia": (
            "O Coco Bambu Londrina integra uma cadeia nacional de restaurantes que se consolidou pela oferta de frutos do mar "
            "em porções generosas e pratos para compartilhar. Em Londrina, tornou-se um dos principais destinos gastronômicos "
            "em shoppings, atraindo famílias e grupos que buscam uma experiência completa de restaurante."
        )
    },
    {
        "nome": "Restaurante Bangkok Garden",
        "descricao": "Restaurante de culinária tailandesa.",
        "latitude": -23.319935345583854,
        "longitude": -51.15744258896249,
        "icon": "utensils",
        "prefix": "fa",
        "color": "purple",
        "tipo": "restaurante",
        "historia": (
            "O Bangkok Garden se destaca por trazer a culinária tailandesa para o cenário gastronômico de Londrina, "
            "com pratos marcados por sabores intensos, uso de especiarias e combinações típicas do sudeste asiático. "
            "O restaurante acabou se tornando referência local em gastronomia internacional."
        )
    },
    {
        "nome": "Bourbon Londrina Hotel",
        "descricao": "Hotel de padrão alto, localizado na região central de Londrina.",
        "latitude": -23.31167302508058,
        "longitude": -51.16100315588057,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel",
        "historia": (
            "O Bourbon Londrina Hotel integra uma rede hoteleira reconhecida nacionalmente e ocupa posição estratégica "
            "na região central da cidade. Ao longo do tempo, passou a receber viajantes de negócios, participantes de "
            "eventos e turistas, contribuindo para consolidar o centro de Londrina como polo de serviços e hospedagem."
        )
    },
    {
        "nome": "Slaviero Essential Londrina Flat Hotel",
        "descricao": "Hotel moderno com estrutura para estadias curtas e longas.",
        "latitude": -23.315551072168827,
        "longitude": -51.15998830430503,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel",
        "historia": (
            "O Slaviero Essential Londrina Flat Hotel faz parte de uma rede de hotéis focada em hospedagem urbana moderna. "
            "Com estrutura de flats e serviços voltados tanto a estadias curtas quanto longas, tornou-se opção prática para "
            "profissionais em trânsito e visitantes que buscam conforto com infraestrutura completa."
        )
    },
    {
        "nome": "Hotel Boulevard",
        "descricao": "Hotel tradicional localizado no centro de Londrina.",
        "latitude": -23.311635001927584,
        "longitude": -51.16517949081201,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel",
        "historia": (
            "Localizado em área central, o Hotel Boulevard se consolidou como uma das opções tradicionais de hospedagem de "
            "Londrina. Pela proximidade com comércio, serviços e pontos turísticos urbanos, costuma ser procurado por quem "
            "deseja se deslocar a pé pelo centro da cidade."
        )
    },
    {
        "nome": "Hotel Thomasi",
        "descricao": "Hotel acessível e funcional, próximo a vias importantes da cidade.",
        "latitude": -23.300876525825842,
        "longitude": -51.18452510245611,
        "icon": "bed",
        "prefix": "fa",
        "color": "orange",
        "tipo": "hotel",
        "historia": (
            "O Hotel Thomasi é conhecido por sua proposta funcional e acessível, atendendo principalmente viajantes de "
            "negócios e visitantes em trânsito pela região. Sua localização próxima a importantes vias de acesso facilita "
            "a chegada à zona sul da cidade e a rodovias que ligam Londrina a outros municípios."
        )
    }
]

df = pd.DataFrame(pontos_londrina)
