#!/usr/bin/env python3
"""Add Tier 2 cities to city-data.json"""
import json

with open('city-data.json', 'r') as f:
    data = json.load(f)

tier2_cities = {
    "wejherowo": {
        "name": "Wejherowo", "locative": "Wejherowie", "genitive": "Wejherowa",
        "slug": "wejherowo", "distance": "40", "drive_time": "~45 min",
        "characteristics": {
            "climate": "Wejherowo leży w dolinie Redy, co oznacza zwiększoną wilgotność powietrza. Poranne mgły i bliskość lasów Trójmiejskiego Parku Krajobrazowego sprzyjają porastaniu budynków glonami.",
            "building_types": "Miasto łączy zabytkowe kamienice centrum z rozrastającymi się osiedlami domów jednorodzinnych na obrzeżach — Nanice, Gościcino, Bolszewo.",
            "problems": "Wilgotna dolina Redy + bliskość lasów = idealne warunki dla mchów i porostów. Domy na obrzeżach, otoczone drzewami, są szczególnie narażone na zielony nalot od strony północnej."
        },
        "challenges": {
            "1": {"icon": "🌫️", "title": "Dolina Redy", "desc": "Położenie w dolinie rzeki oznacza częste mgły i podwyższoną wilgotność — elewacje szybciej pokrywają się glonami."},
            "2": {"icon": "🌲", "title": "Otoczenie lasów", "desc": "Trójmiejski Park Krajobrazowy otacza miasto — spadające igliwie i liście zatykają rynny i tworzą podłoże dla mchów."},
            "3": {"icon": "🏗️", "title": "Nowe osiedla", "desc": "Dynamicznie rozbudowujące się osiedla domów jednorodzinnych — właściciele szukają profesjonalnej konserwacji."}
        }
    },
    "rumia": {
        "name": "Rumia", "locative": "Rumi", "genitive": "Rumi",
        "slug": "rumia", "distance": "35", "drive_time": "~40 min",
        "characteristics": {
            "climate": "Rumia to dynamicznie rozwijające się miasto między Gdynią a Wejherowem. Klimat umiarkowany morski z podwyższoną wilgotnością ze względu na bliskość Bałtyku i dolinę Zagórskiej Strugi.",
            "building_types": "Dominują domy jednorodzinne i szeregowe z lat 90. do współczesnych. Dzielnice Janowo, Szmelta i Zagórze to typowe osiedla willowe wymagające regularnej konserwacji.",
            "problems": "Szybki rozwój budownictwa jednorodzinnego oznacza, że wiele domów z lat 90. i 2000. wymaga pierwszego poważnego czyszczenia. Elewacje po 15-20 latach bez konserwacji pokrywają się glonami i szarzeją."
        },
        "challenges": {
            "1": {"icon": "🏠", "title": "Domy z lat 90.", "desc": "Wiele budynków w Rumi ma 20-30 lat — pierwsze poważne mycie i malowanie to konieczność, nie luksus."},
            "2": {"icon": "💧", "title": "Zagórska Struga", "desc": "Dolina rzeczna przecinająca miasto zwiększa wilgotność — domy w pobliżu potoku szybciej pokrywają się nalotem."},
            "3": {"icon": "📐", "title": "Gęsta zabudowa", "desc": "Ciasne osiedla szeregówek wymagają precyzyjnego sprzętu — nasz podnośnik 83 cm mieści się między budynkami."}
        }
    },
    "reda": {
        "name": "Reda", "locative": "Redzie", "genitive": "Redy",
        "slug": "reda", "distance": "38", "drive_time": "~42 min",
        "characteristics": {
            "climate": "Reda leży w dolinie rzeki Redy, otoczona wzgórzami morenowymi porośniętymi lasem. To sprawia, że powietrze jest wilgotne, a domy w cieniu drzew szybko pokrywają się nalotem biologicznym.",
            "building_types": "Małe, spokojne miasto z przewagą domów jednorodzinnych. Dzielnice Ciechocino, Pieleszewo i Rekowo to tereny willowe otoczone zielenią.",
            "problems": "Dolina Redy i otaczające lasy tworzą mikroklimat sprzyjający porostom. Domy na wzniesieniach mają dodatkowy problem z ekspozycją na wiatr i deszcz napędzany od morza."
        },
        "challenges": {
            "1": {"icon": "🏔️", "title": "Wzgórza morenowe", "desc": "Domy na wzniesieniach są bardziej wystawione na wiatr i deszcz — powłoki malarskie degradują się szybciej."},
            "2": {"icon": "🌿", "title": "Dolina rzeczna", "desc": "Rzeka Reda i otaczające tereny zielone utrzymują wysoką wilgotność — idealne warunki dla glonów i mchów."},
            "3": {"icon": "🏡", "title": "Tereny willowe", "desc": "Spokojne osiedla domów jednorodzinnych — właściciele cenią estetykę i dbają o wygląd posesji."}
        }
    },
    "tczew": {
        "name": "Tczew", "locative": "Tczewie", "genitive": "Tczewa",
        "slug": "tczew", "distance": "50", "drive_time": "~55 min",
        "characteristics": {
            "climate": "Tczew leży nad Wisłą — największą polską rzeką. Bliskość dużego zbiornika wodnego podnosi wilgotność powietrza. Zimą częste przymrozki, latem intensywne nasłonecznienie degraduje powłoki malarskie.",
            "building_types": "Miasto z bogatą historią — od ceglanych kamienic centrum po współczesne osiedla na obrzeżach. Dzielnice Suchostrzygi i Czatkowice to tereny z zabudową jednorodzinną.",
            "problems": "Wilgoć z Wisły + przemysłowe zanieczyszczenia powietrza (Tczew ma strefę przemysłową) = szybsze brudzenie elewacji. Ceglane budynki staromiejskie wymagają szczególnie delikatnych metod czyszczenia."
        },
        "challenges": {
            "1": {"icon": "🌊", "title": "Wisła", "desc": "Bliskość Wisły podnosi wilgotność i sprzyja rozwojowi glonów na elewacjach, szczególnie od strony rzeki."},
            "2": {"icon": "🏭", "title": "Strefa przemysłowa", "desc": "Zanieczyszczenia z pobliskich zakładów osadzają się na elewacjach — szary nalot wymaga specjalistycznego mycia."},
            "3": {"icon": "🧱", "title": "Zabudowa ceglana", "desc": "Zabytkowe kamienice wymagają delikatnych metod czyszczenia — dobieramy ciśnienie indywidualnie do materiału."}
        }
    },
    "starogard-gdanski": {
        "name": "Starogard Gdański", "locative": "Starogardzie Gdańskim", "genitive": "Starogardu Gdańskiego",
        "slug": "starogard-gdanski", "distance": "60", "drive_time": "~1h",
        "characteristics": {
            "climate": "Starogard Gdański to stolica Kociewia, położona w głębi lądu nad rzeką Wierzycą. Klimat bardziej kontynentalny niż w Trójmieście — ostrzejsze zimy i cieplejsze lata.",
            "building_types": "Mieszanka zabudowy — od staromiejskich kamienic, przez bloki z wielkiej płyty, po nowoczesne domy jednorodzinne na osiedlach Kokoszkowy i Łapiszewo.",
            "problems": "Większe amplitudy temperatur powodują pękanie tynków i farb. Rzeka Wierzyca utrzymuje wilgotność. Domy w starszych dzielnicach często mają elewacje zaniedbane od lat."
        },
        "challenges": {
            "1": {"icon": "🌡️", "title": "Amplitudy temperatur", "desc": "Ostrzejszy klimat kontynentalny — mrozy zimą i upały latem powodują szybsze pękanie powłok malarskich."},
            "2": {"icon": "🏚️", "title": "Zaniedbane elewacje", "desc": "Wiele budynków nie było czyszczonych od lat — wymagają kompleksowej renowacji, nie tylko mycia."},
            "3": {"icon": "🛤️", "title": "Odległość od morza", "desc": "Brak zasolenia to plus, ale mniejsza cyrkulacja powietrza oznacza wolniejsze schnięcie — planujemy z uwzględnieniem pogody."}
        }
    },
    "pruszcz-gdanski": {
        "name": "Pruszcz Gdański", "locative": "Pruszczu Gdańskim", "genitive": "Pruszcza Gdańskiego",
        "slug": "pruszcz-gdanski", "distance": "30", "drive_time": "~35 min",
        "characteristics": {
            "climate": "Pruszcz Gdański to jedno z najszybciej rozwijających się miast aglomeracji gdańskiej. Leży nad Radunią, w bliskim sąsiedztwie Żuław Wiślanych — terenu nizinnego o podwyższonej wilgotności.",
            "building_types": "Dynamiczny rozwój budownictwa — nowe osiedla domów jednorodzinnych i szeregowych na Straszynie, Rotmance i Borkowach. Wiele budynków ma 5-15 lat.",
            "problems": "Nizinny teren Żuław = wysoki poziom wód gruntowych i wilgotność. Nowe osiedla często budowane na terenach porolnych, gdzie gleba zatrzymuje wodę."
        },
        "challenges": {
            "1": {"icon": "💧", "title": "Żuławy Wiślane", "desc": "Nizinny teren z wysokim poziomem wód gruntowych — wilgoć podciąga z gruntu i przyspiesza degradację elewacji."},
            "2": {"icon": "🏗️", "title": "Nowe budownictwo", "desc": "Domy sprzed 5-15 lat wymagają pierwszej konserwacji — mycie + impregnacja teraz oszczędzi kosztowny remont za kilka lat."},
            "3": {"icon": "🌾", "title": "Tereny porolne", "desc": "Wiele osiedli powstało na byłych polach — gleba zatrzymuje wodę, co podnosi wilgotność wokół budynków."}
        }
    }
}

# Intro templates per service × city
intros = {
    "mycie-elewacji": {
        "wejherowo": {
            "headline": "dolina Redy i jej wyzwania",
            "p1": "Elewacje budynków w Wejherowie narażone są na działanie wilgotnego mikroklimatu doliny Redy. Poranne mgły i bliskość lasów Trójmiejskiego Parku Krajobrazowego sprawiają, że zielony nalot glonów pojawia się na ścianach szybciej niż w miastach na wyżej położonych terenach.",
            "p2": "Szczególnie narażone są domy na obrzeżach — w Nanicach, Gościcinie i okolicach Bolszewa. Otoczone drzewami, z ograniczonym dostępem słońca, zaczynają szarzeć i porastać glonami już po 2-3 latach od ostatniego mycia. Centrum Wejherowa to z kolei kamienice wymagające delikatniejszego podejścia.",
            "p3": "Z naszej bazy w Goręczynie do Wejherowa jedziemy około 45 minut. Regularnie obsługujemy klientów w tym rejonie — znamy specyfikę lokalnej zabudowy i warunków. Nasz podnośnik gąsienicowy mieści się na wąskich podjazdach wejherowskich domów."
        },
        "rumia": {
            "headline": "domy, które dojrzały do pierwszego mycia",
            "p1": "Rumia to miasto, które dynamicznie rozbudowało się w latach 90. i 2000. Wiele domów jednorodzinnych na osiedlach Janowo, Szmelta i Zagórze ma dziś 20-30 lat — i widać to po elewacjach. Szary nalot, zielone glony od strony północnej, zacieki pod oknami.",
            "p2": "Dolina Zagórskiej Strugi przecinająca miasto utrzymuje podwyższoną wilgotność. Domy w jej sąsiedztwie są najbardziej narażone. Gęsta zabudowa szeregowa ogranicza cyrkulację powietrza, co pogarsza sytuację.",
            "p3": "Nasz sprzęt jest stworzony do pracy w gęstej zabudowie Rumi — podnośnik o szerokości 83 cm wjeżdża między szeregówki bez problemu. Nie potrzebujemy prądu ani rusztowań — przyjeżdżamy z własnym agregatem."
        },
        "reda": {
            "headline": "cisza, zieleń i... glony na elewacji",
            "p1": "Reda to spokojne, kameralne miasto otoczone wzgórzami morenowymi i lasami. Dolina rzeki Redy tworzy malowniczy krajobraz — ale też mikroklimat sprzyjający rozwojowi glonów i mchów na elewacjach domów.",
            "p2": "Domy w dzielnicach Ciechocino, Pieleszewo i Rekowo to typowa zabudowa willowa — często otoczona ogrodem i drzewami. Korony drzew blokują słońce, liście zatykają rynny, a wilgoć nie ma jak odparować.",
            "p3": "Z Goręczyna do Redy mamy nieco ponad 40 minut drogi. Znamy ten rejon doskonale — wielokrotnie pracowaliśmy na elewacjach domów nad Redą. Dobieramy ciśnienie i preparaty do rodzaju tynku."
        },
        "tczew": {
            "headline": "nad Wisłą — wilgoć i przemysł",
            "p1": "Tczew to historyczne miasto nad Wisłą — znane z zabytkowego mostu i bogatej architektury. Bliskość największej polskiej rzeki oznacza podwyższoną wilgotność, która w połączeniu z zanieczyszczeniami ze strefy przemysłowej szybko brudzi elewacje.",
            "p2": "W centrum dominują kamienice wymagające ostrożności przy czyszczeniu. Na obrzeżach rosną osiedla domów jednorodzinnych, które po kilkunastu latach potrzebują pierwszego profesjonalnego mycia.",
            "p3": "Mimo większej odległości (ok. 55 minut jazdy), regularnie realizujemy zlecenia w Tczewie. Wilgoć z Wisły i przemysłowy nalot wymagają dokładnego mycia z preparatami biobójczymi."
        },
        "starogard-gdanski": {
            "headline": "stolica Kociewia potrzebuje opieki",
            "p1": "Starogard Gdański, położony nad Wierzycą w sercu Kociewia, ma klimat bardziej kontynentalny niż Trójmiasto. Większe różnice temperatur oznaczają intensywniejsze pękanie tynków i szybszą degradację powłok malarskich.",
            "p2": "Zabudowa Starogardu to mieszanka — od kamienic staromiejskich po nowe osiedla na Kokoszkowach. Starsze budynki często nie były czyszczone od lat — wymagają kompleksowego podejścia: mycie, odgrzybianie, przygotowanie pod malowanie.",
            "p3": "Dojazd z Goręczyna to około godzina. Realizujemy zlecenia pakietowo — umawiamy kilku klientów w okolicy na jeden wyjazd, co pozwala zoptymalizować koszty dojazdu."
        },
        "pruszcz-gdanski": {
            "headline": "najszybciej rosnące miasto aglomeracji",
            "p1": "Pruszcz Gdański i okolice (Straszyn, Rotmanka, Borkowo) to jeden z najdynamiczniej rozwijających się obszarów aglomeracji gdańskiej. Tysiące nowych domów zbliża się do momentu pierwszej profesjonalnej konserwacji elewacji.",
            "p2": "Nizinny teren Żuław Wiślanych oznacza wysoki poziom wód gruntowych. Nowe osiedla na dawnych polach — gleba zatrzymuje wodę, co podnosi wilgotność wokół fundamentów. Efekt: szary nalot, zielone zacieki, grzybnia przy gruncie.",
            "p3": "Z Goręczyna do Pruszcza mamy zaledwie 35 minut — to jedno z najbliższych nam miast. Mycie elewacji po 5-10 latach + impregnacja to najlepsza inwestycja w ochronę domu."
        }
    },
    "mycie-dachu": {
        "wejherowo": {
            "headline": "dachy w cieniu wejherowskich lasów",
            "p1": "Dachy domów w Wejherowie mają ciężkie życie. Otoczone lasami, zasypywane igliwiem i liśćmi, pokrywają się grubą warstwą mchu szybciej niż w miastach z mniejszą ilością zieleni.",
            "p2": "Igliwie sosnowe tworzy kwaśne podłoże sprzyjające mchom i porostom. W połączeniu z wilgocią z doliny Redy, mech potrafi pokryć cały dach w 3-4 lata. Zatkane rynny to kolejny problem.",
            "p3": "Myjemy dachy w Wejherowie z podnośnika koszowego — bez chodzenia po dachówkach. Nasz podnośnik gąsienicowy wjeżdża na wąskie działki. Czyścimy dachówki, rynny i obróbki blacharskie w jednym podejściu."
        },
        "rumia": {
            "headline": "pierwsze mycie po 20 latach",
            "p1": "Wiele dachów w Rumi z lat 90. nigdy nie było profesjonalnie mytych. Blachodachówka po 20 latach bez konserwacji wygląda dramatycznie: mech, porosty, czarne zacieki, zatkane rynny.",
            "p2": "Dach, który wygląda na wymagający wymiany, często potrzebuje tylko profesjonalnego mycia i malowania. Usunięcie mchu przywraca dachówkom pierwotne właściwości ochronne — oszczędność dziesiątek tysięcy złotych.",
            "p3": "W gęstej zabudowie Rumi nasz podnośnik 83 cm to game-changer — wjeżdżamy między domy. Myjemy dach, rynny i obróbki w jednym podejściu."
        },
        "reda": {
            "headline": "mech z nadrzecznej wilgoci",
            "p1": "Reda, otoczona wzgórzami i lasami, z rzeką przez centrum — tu mchy na dachach rosną wyjątkowo bujnie. Wilgotne powietrze, cień od drzew i organiczny opad tworzą na dachówkach warstwę kompostu.",
            "p2": "Domy na wyżej położonych terenach narażone są na silniejszy wiatr napędzający deszcz pod dachówki. W dolinie dominuje wilgoć i mech. Obie sytuacje wymagają regularnego mycia co 3-5 lat.",
            "p3": "Pracujemy w Redzie z podnośnika koszowego. Nie chodzimy po dachu. Po myciu nakładamy preparat biobójczy spowalniający ponowne porastanie."
        },
        "tczew": {
            "headline": "ochrona przed nadwiślańską wilgocią",
            "p1": "Dachy w Tczewie narażone są na wilgoć z Wisły i zanieczyszczenia przemysłowe. Ciemny nalot, mech od strony północnej, korozja obróbek blacharskich — regularne mycie to ochrona konstrukcji dachu.",
            "p2": "Starsze domy w centrum mają dachówki ceramiczne wymagające konserwacji. Na obrzeżach dominuje blachodachówka, która po kilkunastu latach traci powłokę ochronną i zaczyna rdzewieć pod mchami.",
            "p3": "Realizujemy zlecenia w Tczewie pakietowo — kilku klientów w jednym rejonie. Zapytaj o termin, planujemy regularne wizyty w okolicy."
        },
        "starogard-gdanski": {
            "headline": "dachy kontra kociewski klimat",
            "p1": "Starogard Gdański, z bardziej kontynentalnym klimatem, stawia dachom dodatkowe wyzwania. Ostre zimy z przymrozkami i roztopami narażają dachówki na mikropęknięcia. Gorące lata przyspieszają degradację powłok.",
            "p2": "W Starogardzie wiele dachów nie było mytych od lat — gruba warstwa mchu, zatkane rynny, skorodowane obróbki. Kompleksowe mycie przywraca estetykę i funkcjonalność odprowadzania wody.",
            "p3": "Do Starogardu dojeżdżamy w godzinę. Realizujemy zlecenia pakietowo — umów się z sąsiadami, zoptymalizujemy koszty dojazdu."
        },
        "pruszcz-gdanski": {
            "headline": "nowe dachy, pierwsze problemy",
            "p1": "Pruszcz Gdański i okolice — tysiące nowych domów z dachami 5-15 lat. Na nizinnym, wilgotnym terenie Żuław pierwsze mchy pojawiają się po 3-4 latach od budowy.",
            "p2": "Blachodachówka na nowych osiedlach wymaga uwagi. Mech zatrzymuje wodę, która penetruje pod arkusze blachy i przyspiesza korozję. Wczesne mycie + impregnacja to najtańsze ubezpieczenie.",
            "p3": "Pruszcz to 35 minut od naszej bazy. Typowy dach 150m² z blachodachówki myjemy w jeden dzień z podnośnika."
        }
    },
    "malowanie-elewacji": {
        "wejherowo": {
            "headline": "nowy kolor w dolinie Redy",
            "p1": "Malowanie elewacji w Wejherowie wymaga farb o podwyższonej odporności na wilgoć. Dolina Redy oznacza stałą ekspozycję na wilgotne powietrze. Stosujemy farby silikonowe i siloksanowe, które odpychają wodę.",
            "p2": "Przed malowaniem każdą elewację myjemy i odgrzybiamy. W warunkach wejherowskich pominięcie tego kroku to gwarancja problemów — grzyb wróci pod nową farbę w ciągu roku.",
            "p3": "Malujemy z podnośnika koszowego — szybciej i równomierniej niż z rusztowań. Na wąskich działkach Wejherowa nasz podnośnik 83 cm to jedyna opcja bez rusztowań."
        },
        "rumia": {
            "headline": "metamorfoza rumiańskiego domu",
            "p1": "Domy w Rumi z lat 90. dojrzały do metamorfozy. Elewacje po 20 latach — wyblakłe kolory, szary nalot, odparzenia. Profesjonalne malowanie przywraca świeżość i podnosi wartość nieruchomości.",
            "p2": "W Rumi ważny jest dobór koloru odpornego na blaknięcie. Intensywne słońce od południa i wilgoć od północy to dwa różne wyzwania. Doradzimy optymalny wybór podczas oględzin.",
            "p3": "Na gęstych osiedlach Rumi malujemy z podnośnika — mniej hałasu, mniej zajętego miejsca i szybsza realizacja niż z rusztowań."
        },
        "reda": {
            "headline": "ochrona i estetyka nad Redą",
            "p1": "Malowanie elewacji w Redzie to przede wszystkim ochrona przed wilgocią. Dolina rzeczna i otaczające lasy utrzymują wysoką wilgotność, która penetruje niezabezpieczone tynki.",
            "p2": "W willowych dzielnicach Redy liczy się estetyka. Domy otoczone zielenią wyglądają najlepiej w stonowanych kolorach — ciepłe beże, szarości, przytłumione zielenie. Pomagamy w doborze.",
            "p3": "Malujemy natryskową metodą z podnośnika — równomierna warstwa bez śladów wałka. Pełne przygotowanie podłoża: mycie, odgrzybianie, gruntowanie, uzupełnienie ubytków."
        },
        "tczew": {
            "headline": "trwałe malowanie nad Wisłą",
            "p1": "Malowanie elewacji w Tczewie wymaga szczególnej uwagi na przygotowanie podłoża. Wilgoć z Wisły i zanieczyszczenia przemysłowe tworzą agresywne środowisko dla powłok malarskich.",
            "p2": "Stosujemy farby premium o podwyższonej odporności na zanieczyszczenia. W Tczewie tańsza farba to zmarnowane pieniądze — trzeba malować ponownie za 3-4 lata zamiast za 10.",
            "p3": "Realizujemy zlecenia kompleksowo — od mycia i naprawy tynku po dwuwarstwowe malowanie z podnośnika. Przyjeżdżamy z pełnym wyposażeniem."
        },
        "starogard-gdanski": {
            "headline": "kociewski dom jak nowy",
            "p1": "Elewacje w Starogardzie narażone na duże amplitudy temperatur — mroźne zimy i gorące lata. Stosujemy farby elastyczne, które pracują z tynkiem bez pękania.",
            "p2": "Wiele budynków wymaga nie tylko malowania, ale naprawy tynku — uzupełnienia ubytków, wyrównania powierzchni. Wykonujemy to kompleksowo — klient dostaje gotową elewację.",
            "p3": "Do Starogardu dojeżdżamy w godzinę. Planujemy realizacje, aby zminimalizować koszty dojazdu — łączymy zlecenia w regionie."
        },
        "pruszcz-gdanski": {
            "headline": "pierwsza farba na nowej elewacji",
            "p1": "Domy na nowych osiedlach Pruszcza często mają jedną warstwę farby deweloperskiej — najtańszej z dostępnych. Po 5-8 latach blaknie, szarzeje i przepuszcza wilgoć.",
            "p2": "Malowanie po 5-10 latach to idealna inwestycja — budynek nadal w dobrym stanie, a nowa farba premium ochroni go na dekadę. Czekanie dłużej oznacza droższą naprawę tynku.",
            "p3": "Pruszcz to 35 minut od bazy. Znamy nowe osiedla i specyfikę deweloperskich tynków. Malujemy natryskową metodą z podnośnika."
        }
    },
    "malowanie-dachu": {
        "wejherowo": {
            "headline": "dach odporny na wejherowską wilgoć",
            "p1": "Malowanie dachu w Wejherowie to ochrona przed korozją i wilgocią. Blachodachówki w warunkach doliny Redy — z mgłami i wilgotnością — rdzewieją szybciej niż w suchszych rejonach.",
            "p2": "Przed malowaniem dach myjemy ciśnieniowo, odgrzybiamy i gruntujemy antykorozyjnie. Dopiero na przygotowane podłoże nakładamy dwie warstwy farby dachowej.",
            "p3": "Pracujemy z podnośnika — nie chodzimy po dachu. Na wejherowskich działkach nasz kompaktowy podnośnik 83 cm jest niezastąpiony."
        },
        "rumia": {
            "headline": "nowy dach bez wymiany",
            "p1": "Dachy wielu domów w Rumi wyglądają, jakby wymagały wymiany — wyblakłe, pordzewiałe. W większości przypadków wystarczy profesjonalne mycie i malowanie za ułamek kosztu.",
            "p2": "Blachodachówka po 20 latach traci powłokę fabryczną. Malowanie antykorozyjne zatrzymuje rdzewienie i przedłuża żywotność pokrycia o 10-15 lat.",
            "p3": "Malujemy dachy w Rumi z podnośnika — bezpiecznie, bez chodzenia po blasze. Na gęstych osiedlach to jedyna sensowna metoda."
        },
        "reda": {
            "headline": "ochrona dachu w dolinie rzeki",
            "p1": "Dachy w Redzie narażone na wilgoć z doliny i organiczny opad z lasów. Farba antykorozyjna tworzy barierę zapobiegającą wnikaniu wody pod pokrycie.",
            "p2": "Ważny jest dobór koloru odpornego na UV — słońce na wzniesieniach jest intensywniejsze. Pomagamy dobrać optymalne rozwiązanie.",
            "p3": "Malujemy kompleksowo: mycie → odgrzybianie → gruntowanie → 2 warstwy farby. Wszystko z podnośnika."
        },
        "tczew": {
            "headline": "antykorozja nad Wisłą",
            "p1": "Dachy w Tczewie narażone na wilgoć z Wisły i zanieczyszczenia — agresywna mieszanka przyspieszająca korozję. Profesjonalna farba antykorozyjna to najskuteczniejsza ochrona.",
            "p2": "Dachówki ceramiczne w starszych częściach wymagają farby paroprzepuszczalnej i elastycznej. Stosujemy produkty dedykowane do każdego typu pokrycia.",
            "p3": "Realizujemy zlecenia pakietowo. Wspólne zlecenie sąsiadów to niższe koszty dojazdu dla każdego."
        },
        "starogard-gdanski": {
            "headline": "dach na kociewskie zimy",
            "p1": "Klimat Starogardu jest wymagający — ostre mrozy, obfite opady śniegu, gwałtowne roztopy. Farba dachowa musi być elastyczna i odporna na skrajne temperatury.",
            "p2": "Wiele dachów nie było malowanych od lat — warstwa fabryczna dawno straciła właściwości. Im wcześniej malowanie, tym mniej kosztuje przygotowanie podłoża.",
            "p3": "Jesteśmy w Starogardzie w godzinę. Malowanie typowego dachu 150-200m² to 2-3 dni pracy z podnośnika."
        },
        "pruszcz-gdanski": {
            "headline": "młody dach, dojrzały do malowania",
            "p1": "Blachodachówki na nowych osiedlach Pruszcza mają 5-15 lat — fabryczna powłoka zaczyna blaknąć. To idealny moment na malowanie — podłoże w dobrym stanie.",
            "p2": "Na nizinnym terenie Żuław farba hydrofobowa tworzy dodatkową barierę. Woda spływa zamiast wnikać pod blachę — szczególnie ważne przy wysokich wodach gruntowych.",
            "p3": "Pruszcz to 35 minut od bazy. Typowy dach 150m² malujemy w 1-2 dni z podnośnika."
        }
    },
    "impregnacja": {
        "wejherowo": {
            "headline": "tarcza ochronna w wilgotnej dolinie",
            "p1": "W Wejherowie, z wilgotnym mikroklimatem doliny Redy, impregnacja to konieczność. Bez hydrofobowej powłoki elewacja umyta dziś zacznie porastać za 2 lata. Z impregnacją — spokojnie 5-7 lat.",
            "p2": "Preparat impregnujący tworzy niewidoczną barierę. Woda spływa po elewacji zamiast wnikać w pory — brud i mikroorganizmy nie mają za co się chwycić.",
            "p3": "Wykonujemy impregnację bezpośrednio po myciu — gdy tynk jest czysty i suchy. Pakiet mycie + impregnacja = podwójna cena mycia, wieloletnia ochrona."
        },
        "rumia": {
            "headline": "ochrona po pierwszym myciu",
            "p1": "Jeśli zdecydowałeś się na mycie elewacji w Rumi po 20 latach — nie pomijaj impregnacji. Czysty tynk bez ochrony hydrofobowej brudzą się szybciej niż przed myciem.",
            "p2": "Gęsta zabudowa Rumi ogranicza cyrkulację powietrza — elewacje schną wolniej. Impregnacja sprawia, że woda nie wnika w tynk — spływa po powierzchni zabierając brud. Efekt lotosowy.",
            "p3": "Najczęstszy pakiet w Rumi: mycie elewacji + impregnacja + mycie kostki wokół domu. Kompleksowe podejście = jeden wyjazd, niższe koszty."
        },
        "reda": {
            "headline": "bariera przed nadrzeczną wilgocią",
            "p1": "Reda, z rzeką przez centrum i otaczającymi lasami, to środowisko o stale podwyższonej wilgotności. Impregnacja po myciu to najskuteczniejszy sposób na wydłużenie efektu czystości.",
            "p2": "W willowych dzielnicach Redy impregnacja jest szczególnie ważna od strony północnej i zachodniej — tam wilgoć utrzymuje się najdłużej i glony pojawiają się najszybciej.",
            "p3": "Nakładamy preparat natryskową metodą bezpośrednio po myciu. Czas schnięcia 2-4 godziny. Polecamy odnawianie co 5 lat."
        },
        "tczew": {
            "headline": "ochrona przed wilgocią i zanieczyszczeniami",
            "p1": "W Tczewie elewacje narażone na podwójne zagrożenie — wilgoć z Wisły i zanieczyszczenia przemysłowe. Impregnacja hydrofobowa chroni przed obydwoma.",
            "p2": "Szczególnie polecamy impregnację nowych osiedli — domy 5-15 lat w dobrym stanie, impregnacja zabezpieczy je na lata. Wielokrotnie tańsze niż naprawa uszkodzonego tynku.",
            "p3": "Impregnację wykonujemy po myciu, w jednym podejściu. W Tczewie łączymy zlecenia pakietowo."
        },
        "starogard-gdanski": {
            "headline": "ochrona przed kociewskimi mrozami",
            "p1": "W Starogardzie impregnacja chroni przede wszystkim przed wnikaniem wody, która zamarzając zimą rozsadza tynk. Ostry klimat sprawia, że niezaimpregnowany tynk pęka szybciej.",
            "p2": "Preparat hydrofobowy zmniejsza nasiąkliwość tynku o 95%. Woda nie wnika — nie ma czego zamrażać. Dłuższa żywotność elewacji, mniejsze koszty napraw.",
            "p3": "Impregnujemy elewacje, dachy, cokoły i kostki. W Starogardzie polecamy szczególnie impregnację cokołów — wilgoć podciągająca z gruntu to częsty problem."
        },
        "pruszcz-gdanski": {
            "headline": "zabezpieczenie nowego domu",
            "p1": "Nowe domy na osiedlach Pruszcza stoją na nizinnym, wilgotnym terenie Żuław. Impregnacja elewacji i cokołu to pierwsza linia obrony przed wilgocią podciągającą z gruntu.",
            "p2": "Wielu właścicieli nie wie, że elewacja powinna być zaimpregnowana w ciągu 2-3 lat od budowy. Deweloperzy tego nie robią — tynk bez ochrony szarzeje i nasiąka.",
            "p3": "Z Goręczyna do Pruszcza 35 minut. Oferujemy pakiet nowy dom: przegląd elewacji + impregnacja profilaktyczna + zabezpieczenie cokołu."
        }
    }
}

# Merge cities
data['cities'].update(tier2_cities)

# Merge intros
for service_slug, city_intros in intros.items():
    for city_slug, intro in city_intros.items():
        data['services'][service_slug]['intro_templates'][city_slug] = intro

with open('city-data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Total cities: {len(data['cities'])}")
print(f"✅ Total pages: {len(data['cities']) * len(data['services'])}")
for s in data['services']:
    print(f"   {s}: {len(data['services'][s]['intro_templates'])} intros")
