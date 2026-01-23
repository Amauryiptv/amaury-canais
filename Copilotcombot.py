import random

# Lista com ~500 nomes brasileiros (250 masculinos + 250 femininos)
nomes = [
    # Masculinos (250 exemplos)
    "joao","jose","antonio","francisco","carlos","paulo","pedro","lucas","marcos","rafael",
    "gabriel","rodrigo","thiago","bruno","andre","roberto","fernando","daniel","vinicius","gustavo",
    "felipe","diego","leonardo","eduardo","mateus","caio","samuel","vitor","ricardo","alessandro",
    "claudio","sergio","alberto","osvaldo","julio","miguel","arthur","enzo","davi","caetano",
    "murilo","joaquim","nicolas","henrique","lauro","everton","wellington","silvio","elias","cristiano",
    "adriano","alexandre","alan","alvaro","bernardo","cesar","domingos","douglas","emerson","fabio",
    "gilberto","guilherme","humberto","ivan","jair","jorge","kleber","leandro","luiz","manoel",
    "marcelo","mario","mauricio","nelson","otavio","ronaldo","rubens","sebastiao","tadeu","valter",
    "wanderlei","wilson","yuri","zeca","arnaldo","augusto","benjamin","caue","celso","dener",
    "edson","eliezer","flavio","genival","helder","israel","jadson","kelvin","lisandro","marcio",
    "natal","orlando","patrick","renan","sidnei","tomas","ulisses","valdir","washington","xavier",
    "yan","zacarias","adailton","adilson","agnaldo","airton","alencar","altair","americo","anibal",
    "aparecido","aristides","arno","aroldo","aurélio","bartolomeu","benicio","bento","bonifacio","cicero",
    "cleber","clemente","crispim","dalton","damiao","darlan","delcio","dirceu","dorival","edgar",
    "eder","egidio","elcio","elio","emanuel","ernesto","eugenio","everaldo","fabiano","fausto",
    "fidelis","floriano","genaro","geraldo","gilmar","givanildo","heraldo","hercules","hugo","ignacio",
    "ismael","italo","ivanildo","ivo","janio","jean","jefferson","jonas","jonatas","josue",
    "juarez","jurandir","juvenal","lazaro","lindomar","lorival","luciano","luizinho","manoelito","marciano",
    "mauro","moises","nelio","nivaldo","norberto","odair","olavo","onofre","orivaldo","osmar",
    "otacilio","oziel","pablo","paulinho","pericles","radames","raul","reginaldo","remi","ricardinho",
    "romario","romeu","ronan","rubinho","sabino","salvador","samir","sandro","saulo","serafim",
    "silas","tarcisio","teodoro","timoteo","tobias","valdemar","valmir","vicente","vilson","wagner",
    "wander","wilmar","zeferino","zeno","zezinho",

    # Femininos (250 exemplos)
    "maria","ana","juliana","camila","fernanda","patricia","aline","carla","marcia","eliane",
    "claudia","debora","fabiana","leticia","renata","simone","talita","vanessa","beatriz","luana",
    "sofia","isabela","carolina","gabriela","amanda","daniela","flavia","helena","lorena","natalia",
    "priscila","sara","tatiane","viviane","yasmin","bianca","bruna","cecilia","estela","joana",
    "laura","melissa","monica","raquel","regina","rosangela","solange","sueli","veronica","valeria",
    "zuleide","adriana","alice","antonia","barbara","bernadete","clara","cristina","diana","edna",
    "evelyn","fabiola","geovana","helga","iris","janaina","karina","lara","lilian","marlene",
    "nadia","olga","pamela","rafaela","sabrina","tereza","ursula","valquiria","wanda","xuxa",
    "yara","zilda","agnes","beth","cintia","dalva","elisa","francisca","giovana","hortencia",
    "inez","jacira","katia","leila","magda","nelma","odete","penelope","quiteria","rosana",
    "silvana","tainara","ulla","vitoria","wilma","xenia","yasmim","zara","abigail","adalice",
    "adelina","alessandra","alma","altina","amalia","amelia","anastacia","andrea","angelica","anita",
    "aparecida","arlete","aurora","benedita","berta","branca","candida","celia","cilene","dalila",
    "damiana","darlene","delma","dilma","dina","dirce","divina","dulce","edite","elaine",
    "eloisa","emilia","erica","esther","eugenia","eva","fatima","filomena","frida","genoveva",
    "gerusa","gilma","gloria","graciela","hilda","ilda","ines","iracema","ivana","ivone",
    "jandira","josefa","judite","julia","julieta","lais","lidia","liliane","lourdes","lucia",
    "luciana","luiza","madalena","maite","manuela","marcela","mariana","marta","mirian","neide",
    "noemia","norma","odilia","paula","quiteria","regiane","rosalia","rosilda","rosineide","sandra",
    "selma","silvia","sonia","stefany","suellen","tania","teresinha","valentina","vera","vilma",
    "yasmin","zelia"
]

# Lista de senhas fixas
senhas_base = [
    "123456","12345678","123456789","102030","10203040",
    "senha123","brasil2024","abcd1234","qwerty","000000",
    "111111","123123"
]

combos = []

# Gera combinações fixas
for nome in nomes:
    for senha in senhas_base:
        combos.append(f"{nome}:{senha}")
    combos.append(f"{nome}:{nome}")
    combos.append(f"{nome}:{nome}123")
    combos.append(f"{nome}:{nome}2025")

# Gera variações aleatórias até chegar em 100.000 combinações
while len(combos) < 100000:
    nome = random.choice(nomes)
    numero = random.randint(1000, 9999)
    combos.append(f"{nome}:{nome}{numero}")

# Salva no arquivo combo.txt
with open("combo.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(combos))

print("combo.txt com 100.000 combinações gerado com sucesso!")
