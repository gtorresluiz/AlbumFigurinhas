import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Cover text
content = content.replace('<p class="cover-footer-text">OS MARCOS DA NOSSA HISTÓRIA</p>', '<p class="cover-footer-text">PRESENTE DE 1 ANO DE NAMORO PARA DUDA</p>')
content = content.replace('<span>DESDE 18/10/2025</span>', '<span>18/10/25 - 18/10/26</span>')

# Replace Backcover text
content = content.replace('<span class="barcode-number">1 8102025 15072026</span>', '<span class="barcode-number">1 181025 181026</span>')
content = content.replace('O nosso álbum é um tributo interativo à nossa história — cada figurinha guarda um momento,\n                            uma piada ou uma data que só a gente entende.\n                            Juntando tudo o que já vivemos e o que ainda vem por aí.', 'O nosso álbum é um tributo à nossa história — cada figurinha guarda um momento,\n                            uma aventura ou uma data que só a gente entende.\n                            Feliz 1 ano de namoro, meu amor!')

# Now let's replace the slots
replacements = {
    1: ('O primeiro "oi"', 'No Instagram, WhatsApp ou onde tudo começou!', 'O Primeiro "Oi"', 'Onde nossa história começou'),
    2: ('Primeiro Encontro', 'Aquele lugar especial com o melhor frio na barriga', 'Primeiro Encontro', 'Aquele frio na barriga inesquecível'),
    3: ('O Pedido de Namoro', 'A frase e a data que oficializaram o nosso amor', 'O Pedido', 'Quando tudo se oficializou'),
    4: ('Primeiro Rolê Marcante', 'A nossa primeira aventura oficial juntos', 'Ipiranga', 'Passeio marcante pelo museu'),
    5: ('Timing Quase Errado', 'Aquele perrengue engraçado antes de darmos certo', 'Cinema', 'Nossa sessão com muita pipoca'),
    6: ('1º Show Juntos', 'O primeiro show que curtimos na mesma batida', '1º Buquê', 'As primeiras flores que te dei'),
    7: ('Show Marcante 2', 'Aquela noite cheia de energia e música boa', '2º Buquê', 'Mais flores para alegrar seu dia'),
    8: ('Nossa Música', 'O artista ou show que virou a nossa canção', 'LEGO', 'Nosso buquê montável e eterno'),
    9: ('Show 3', 'Mais uma apresentação inesquecível na nossa conta', 'Girassóis', 'Para iluminar como o seu sorriso'),
    10: ('Show/Festival Recente', 'O evento mais recente onde cantamos bem alto', 'O Buquê', 'O mais especial de todos'),
    11: ('Primeira Viagem', 'Nossa estreia na estrada e o que rolou por lá', 'Primeira Viagem', 'Nossa estreia colocando o pé na estrada'),
    12: ('Viagem 2', 'Descobrindo novos horizontes lado a lado', 'Aparecida', 'Abençoando o nosso caminho'),
    13: ('A Viagem Inesquecível', 'Aquela que rendeu a melhor história para contar', 'Cachoeira', 'Renovando as energias na natureza'),
    14: ('Viagem 3', 'Mais um destino inesquecível riscado do mapa', 'Ilhabela', 'Sol, mar e muita história pra contar'),
    15: ('Sonho de Viagem', 'O próximo destino que planejamos conquistar', 'Ubatuba', 'Mais um paraíso conquistado juntos'),
    16: ('1º Filme Juntos', 'A primeira vez dividindo a pipoca e o sofá', 'Cinesala', 'Aquele cinema aconchegante'),
    17: ('Filme/Série Favorita', 'Aquela que a gente maratona sem cansar', 'Morumbi', 'Torcendo juntos na arquibancada'),
    18: ('Clássico do Casal', 'O filme que vira maratona toda vez', 'Mamma Mia', 'Muita música e diversão no teatro'),
    19: ('Cinema Marcante', 'Uma estreia especial ou uma data marcante', 'Shrek', 'O nosso ogro favorito'),
    20: ('Franquia do Amor', 'Só um de nós gosta, mas assistimos juntinhos', 'Orquestra', 'Uma noite de muita classe e som incrível'),
    21: ('Primeiro Date', 'O restaurante onde nosso primeiro jantar aconteceu', 'Sorvete', 'A sobremesa perfeita pro casal'),
    22: ('Restaurante "Fixo"', 'Aquele lugar especial que é nossa segunda casa', 'Dia dos Namorados', 'Jantar romântico inesquecível'),
    23: ('Jantar Mais Especial', 'A data mais importante que comemoramos comendo bem', 'Old Man', 'Comida e momento sensacional'),
    24: ('Comida com Nossa Cara', 'O prato ou lanche que define a gente', 'Macarrão c/ Camarão', 'Um prato com a nossa cara'),
    25: ('Jantar Caseiro', 'Cozinhando juntos com direito a muita bagunça', 'Primeiro Rodízio', 'Comendo até não aguentar mais'),
    26: ('Apelido Dela', 'Como eu a chamo com todo o carinho do mundo', 'Rosa', 'Uma rosa para a minha rosa'),
    27: ('Apelido Seu', 'A forma fofa como ela me chama no dia a dia', 'Onix', 'Muitas memórias a bordo'),
    28: ('A Piada Interna', 'Aquela frase ou meme que só nós dois entendemos', 'Formatura', 'Conquistas celebradas lado a lado'),
    29: ('Momento Engraçado', 'Aquele perrengue ou cena hilária que passamos juntos', 'Casamento', 'Prestigiando o amor alheio juntinhos'),
    30: ('Você & Eu', 'Espaço reservado para o nosso futuro...', 'Harry', 'O bruxo mais querido do casal'),
}

# Fix slot 30 that had inverted role/name in index.html initially if that's the case. Wait, it didn't!
for k, v in replacements.items():
    content = content.replace(f'<div class="slot-name">{v[0]}</div>', f'<div class="slot-name">{v[2]}</div>')
    content = content.replace(f'<div class="slot-role">{v[1]}</div>', f'<div class="slot-role">{v[3]}</div>')

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
