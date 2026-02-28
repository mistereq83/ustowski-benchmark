#!/usr/bin/env python3
"""Add Tier 3 cities to city-data.json"""
import json

with open('city-data.json', 'r') as f:
    data = json.load(f)

tier3_cities = {
    "kartuzy": {
        "name": "Kartuzy", "locative": "Kartuzach", "genitive": "Kartuz",
        "slug": "kartuzy", "distance": "15", "drive_time": "~20 min",
        "characteristics": {
            "climate": "Kartuzy to serce Kaszub — miasto otoczone jeziorami i lasami Pojezierza Kaszubskiego. Wilgotność znad jezior i gęste lasy tworzą mikroklimat sprzyjający porostom i glonami na elewacjach.",
            "building_types": "Zabudowa Kartuz to mieszanka — od starych kamienic centrum, przez osiedla z lat PRL, po dynamicznie rosnące nowe osiedla domów jednorodzinnych na obrzeżach miasta.",
            "problems": "Jeziora otaczające miasto (Karczemne, Klasztorne) podnoszą wilgotność. Lasy Kaszubskie dostarczają organiczny opad. Domy na wzgórzach narażone na wiatr, w dolinach na wilgoć — obie sytuacje degradują elewacje."
        },
        "challenges": {
            "1": {"icon": "🏞️", "title": "Pojezierze Kaszubskie", "desc": "Jeziora otaczające miasto podnoszą wilgotność powietrza — elewacje i dachy porastają szybciej niż w miastach bez zbiorników wodnych."},
            "2": {"icon": "🌲", "title": "Lasy Kaszubskie", "desc": "Gęste lasy wokół miasta dostarczają igliwie i liście, które zatykają rynny i tworzą podłoże dla mchów na dachach."},
            "3": {"icon": "⛰️", "title": "Teren pagórkowaty", "desc": "Kaszubska Szwajcaria to wzgórza i doliny — domy na szczytach narażone na wiatr, w dolinach na wilgoć i mgły."}
        }
    },
    "zukowo": {
        "name": "Żukowo", "locative": "Żukowie", "genitive": "Żukowa",
        "slug": "zukowo", "distance": "12", "drive_time": "~15 min",
        "characteristics": {
            "climate": "Żukowo leży na granicy Trójmiasta i Kaszub — to jedno z najbliższych nam miast. Teren lekko pagórkowaty, z licznymi lasami i strumieniami, co utrzymuje podwyższoną wilgotność.",
            "building_types": "Gmina Żukowo to przede wszystkim zabudowa jednorodzinna — od historycznego centrum po nowe osiedla w Baninie, Chwaszczynie i Leźnie, będące sypialniami Trójmiasta.",
            "problems": "Dynamiczny rozwój budownictwa w Baninie i Chwaszczynie oznacza tysiące nowych domów na byłych terenach leśnych i rolnych. Gleba zatrzymuje wodę, okoliczne lasy utrzymują wilgoć — elewacje szarzą szybko."
        },
        "challenges": {
            "1": {"icon": "🏘️", "title": "Sypialnia Trójmiasta", "desc": "Tysiące nowych domów w Baninie, Chwaszczynie i Leźnie — wiele zbliża się do momentu pierwszej konserwacji elewacji."},
            "2": {"icon": "🌳", "title": "Dawne tereny leśne", "desc": "Nowe osiedla na wykarczowanych lasach — pnie i korzenie zatrzymują wodę, pozostałe drzewa tworzą cień sprzyjający glonami."},
            "3": {"icon": "📍", "title": "Najbliżej naszej bazy", "desc": "Żukowo to zaledwie 15 minut od Goręczyna — najkrótszy dojazd ze wszystkich obsługiwanych miast."}
        }
    },
    "koscierzyna": {
        "name": "Kościerzyna", "locative": "Kościerzynie", "genitive": "Kościerzyny",
        "slug": "koscierzyna", "distance": "35", "drive_time": "~40 min",
        "characteristics": {
            "climate": "Kościerzyna to stolica Kaszub, położona wśród lasów i jezior. Klimat umiarkowany z wyraźnym wpływem jezior — podwyższona wilgotność, częste mgły poranne, intensywne opady w sezonie jesiennym.",
            "building_types": "Miasto z długą historią — od zabytkowych budynków centrum po osiedla z lat 70-80. i nowe budownictwo jednorodzinne na obrzeżach. Okoliczne wsie (Łubiana, Nowa Karczma) to typowa zabudowa kaszubska.",
            "problems": "Jeziora (Kościerskie, Garczyn) i lasy utrzymują wysoką wilgotność. Starsze budynki w centrum często zaniedbane od lat. Nowe domy na obrzeżach narażone na wilgoć z okolicznych zbiorników wodnych."
        },
        "challenges": {
            "1": {"icon": "🌊", "title": "Jeziora kościerskie", "desc": "Liczne jeziora wokół miasta podnoszą wilgotność — poranne mgły i rosa przyspieszają rozwój glonów na elewacjach."},
            "2": {"icon": "🏛️", "title": "Zabytkowe centrum", "desc": "Stare budynki wymagają delikatnych metod czyszczenia — dobieramy ciśnienie i preparaty indywidualnie do wieku i materiału."},
            "3": {"icon": "🌲", "title": "Puszcza Kaszubska", "desc": "Otoczenie lasów oznacza stały opad organiczny — igliwie, liście i pyłki tworzą na elewacjach podłoże dla porostów."}
        }
    },
    "bytow": {
        "name": "Bytów", "locative": "Bytowie", "genitive": "Bytowa",
        "slug": "bytow", "distance": "75", "drive_time": "~1h 15min",
        "characteristics": {
            "climate": "Bytów leży na południowych Kaszubach, w otoczeniu lasów Borów Tucholskich i jezior. Klimat bardziej kontynentalny — chłodniejsze zimy, cieplejsze lata, mniejszy wpływ morza.",
            "building_types": "Miasto z gotyckim zamkiem krzyżackim i historyczną zabudową centrum. Na obrzeżach — osiedla z lat PRL i nowe budownictwo jednorodzinne. Okolice to typowa kaszubska wieś.",
            "problems": "Oddalenie od morza oznacza ostrzejszy klimat — przymrozki uszkadzają tynki, a wilgoć z okolicznych jezior i lasów sprzyja porostom. Wiele budynków w centrum nie było remontowanych od dekad."
        },
        "challenges": {
            "1": {"icon": "🏰", "title": "Historyczna zabudowa", "desc": "Zabytkowe budynki przy zamku krzyżackim wymagają szczególnej ostrożności — delikatne metody czyszczenia i konserwacji."},
            "2": {"icon": "🌡️", "title": "Klimat kontynentalny", "desc": "Ostrzejsze zimy i większe amplitudy temperatur przyspieszają degradację tynków i powłok malarskich."},
            "3": {"icon": "🛣️", "title": "Większa odległość", "desc": "75 km od naszej bazy — planujemy wyjazdy pakietowo, łącząc kilka zleceń w regionie dla optymalizacji kosztów."}
        }
    },
    "lebork": {
        "name": "Lębork", "locative": "Lęborku", "genitive": "Lęborka",
        "slug": "lebork", "distance": "65", "drive_time": "~1h 10min",
        "characteristics": {
            "climate": "Lębork leży w dolinie Łeby, między Pojezierzem Kaszubskim a wybrzeżem Bałtyku. Wpływ morski jest tu odczuwalny — wilgotne powietrze, częste opady, wiatry z północy.",
            "building_types": "Miasto z gotycką zabudową centrum (mury obronne, kościoły) i osiedlami z różnych epok. Na obrzeżach — nowe budownictwo jednorodzinne. Okolice to wsie i małe miejscowości.",
            "problems": "Dolina Łeby utrzymuje wilgotność. Wpływ morski przynosi zasolenie i wilgoć. Starsze budynki w centrum wymagają kompleksowej renowacji — mycie to często pierwszy krok przed malowaniem."
        },
        "challenges": {
            "1": {"icon": "💨", "title": "Wpływ morski", "desc": "Bliskość Bałtyku oznacza zasolone powietrze i wilgoć — elewacje degradują się szybciej niż w głębi lądu."},
            "2": {"icon": "🏛️", "title": "Gotyckie centrum", "desc": "Zabytkowe budynki z cegły i kamienia wymagają specjalistycznych metod czyszczenia — bez agresywnych ciśnień."},
            "3": {"icon": "🌊", "title": "Dolina Łeby", "desc": "Rzeka Łeba i okoliczne mokradła utrzymują wilgotność — domy w dolinie porastają mchem i glonami intensywniej."}
        }
    },
    "goreczyno": {
        "name": "Goręczyno", "locative": "Goręczynie", "genitive": "Goręczyna",
        "slug": "goreczyno", "distance": "0", "drive_time": "na miejscu",
        "characteristics": {
            "climate": "Goręczyno to nasza baza — znamy każdy dom w okolicy. Gmina leży w sercu Kaszub, otoczona lasami i polami. Typowy kaszubski mikroklimat — wilgotne lasy, poranne mgły, obfite opady.",
            "building_types": "Gmina wiejska z dominującą zabudową jednorodzinną i zagrodową. Domy od tradycyjnych kaszubskich po nowoczesne. Okoliczne wsie: Kamienica Szlachecka, Niestępowo, Szarłata.",
            "problems": "Otoczenie lasów i pól oznacza stałą ekspozycję na wilgoć i opad organiczny. Tradycyjne kaszubskie domy z cegły i tynku wymagają regularnej konserwacji. Nowe domy na dawnych polach narażone na wilgoć z gleby."
        },
        "challenges": {
            "1": {"icon": "🏠", "title": "Nasza baza", "desc": "Goręczyno to nasz dom — zero kosztów dojazdu, najszybszy czas reakcji. Znamy każdą okolicę jak własną kieszeń."},
            "2": {"icon": "🌲", "title": "Serce Kaszub", "desc": "Otoczenie lasów i pól utrzymuje wilgotność — elewacje domów porastają glonami, szczególnie od strony północnej i zachodniej."},
            "3": {"icon": "🏡", "title": "Zabudowa kaszubska", "desc": "Tradycyjne domy ceglane i nowe budownictwo — każdy typ wymaga indywidualnego doboru metody czyszczenia i malowania."}
        }
    }
}

intros = {
    "mycie-elewacji": {
        "kartuzy": {
            "headline": "serce Kaszub nad jeziorami",
            "p1": "Kartuzy, otoczone jeziorami Karczemnym i Klasztornym, to miasto o podwyższonej wilgotności. Para wodna znad jezior osiada na elewacjach, tworząc idealne warunki dla glonów. Domy blisko zbiorników wodnych porastają najszybciej.",
            "p2": "Pagórkowaty teren Kartuz sprawia, że domy na wzniesieniach narażone są na wiatr i deszcz, a te w dolinach — na mgły i wilgoć. Każda lokalizacja wymaga innego podejścia do mycia i doboru preparatów biobójczych.",
            "p3": "Z Goręczyna do Kartuz mamy zaledwie 20 minut — to jedno z najbliższych nam miast. Znamy kaszubską specyfikę budowlaną i klimatyczną. Regularnie obsługujemy klientów w Kartuzach i okolicznych wsiach."
        },
        "zukowo": {
            "headline": "15 minut od naszej bazy",
            "p1": "Żukowo i okolice (Banino, Chwaszczyno, Leźno) to jedne z najdynamiczniej rozwijających się terenów pod Trójmiastem. Tysiące nowych domów, które wyrosły w ostatniej dekadzie na dawnych polach i terenach leśnych, zbliżają się do momentu pierwszej poważnej konserwacji.",
            "p2": "Charakterystyka terenu — dawne lasy, gliniasta gleba zatrzymująca wodę, pozostałe drzewa tworzące cień — sprawia, że elewacje szarzeją i porastają szybko. Szczególnie widoczne to jest od strony północnej i w miejscach, gdzie drzewa blokują słońce.",
            "p3": "Żukowo to zaledwie 15 minut od naszej bazy w Goręczynie — najkrótszy dojazd ze wszystkich obsługiwanych miast. To oznacza najniższe koszty dojazdu i najszybszy czas reakcji. Znamy te osiedla jak własną kieszeń."
        },
        "koscierzyna": {
            "headline": "stolica Kaszub w otoczeniu jezior",
            "p1": "Kościerzyna, stolica Kaszub, leży wśród lasów i jezior — piękne otoczenie, ale wymagające dla elewacji. Jeziora Kościerskie i Garczyn podnoszą wilgotność powietrza, a otaczające lasy dostarczają organiczny opad tworzący podłoże dla porostów.",
            "p2": "W centrum Kościerzyny wiele budynków ma elewacje zaniedbane od lat — szare, pokryte nalotem, z widocznymi ubytkami. Na obrzeżach rosną nowe osiedla, których właściciele szukają profesjonalnej konserwacji profilaktycznej.",
            "p3": "Z Goręczyna do Kościerzyny dojeżdżamy w około 40 minut. Realizujemy zlecenia w tym rejonie regularnie — znamy kaszubską specyfikę. Łączymy zlecenia w regionie, aby zoptymalizować koszty dojazdu."
        },
        "bytow": {
            "headline": "południowe Kaszuby — zamek i lasy",
            "p1": "Bytów, z gotyckim zamkiem krzyżackim i malowniczym otoczeniem, to miasto o bogatej historii i specyficznym klimacie. Położenie na południowych Kaszubach, z dala od morza, oznacza ostrzejsze zimy i większe wahania temperatur.",
            "p2": "Zabudowa Bytowa to mieszanka — od historycznych kamienic centrum wymagających delikatnego podejścia, po osiedla z lat PRL i nowe domy na obrzeżach. Każdy typ budynku wymaga innej metody mycia i doboru ciśnienia.",
            "p3": "Bytów to nasz najdalszy punkt obsługi (ok. 75 km). Planujemy wyjazdy pakietowo — łączymy kilka zleceń w regionie bytowskim. Zapytaj o termin, możliwe że planujemy wizytę w Twoich okolicach."
        },
        "lebork": {
            "headline": "między morzem a Kaszubami",
            "p1": "Lębork leży w dolinie Łeby — między Pojezierzem Kaszubskim a wybrzeżem Bałtyku. Wpływ morski jest tu odczuwalny: wilgotne powietrze, zasolenie i wiatry z północy przyspieszają degradację elewacji.",
            "p2": "Gotyckie centrum Lęborka z ceglanymi budynkami wymaga szczególnej ostrożności przy czyszczeniu. Na obrzeżach — nowoczesne domy jednorodzinne, których elewacje po kilkunastu latach potrzebują pierwszego profesjonalnego mycia.",
            "p3": "Dojazd z Goręczyna do Lęborka to ok. 1h 10min. Realizujemy zlecenia pakietowo — umawiamy kilku klientów w regionie na jeden wyjazd. Profesjonalny sprzęt wart ponad 350 000 zł gwarantuje skuteczność."
        },
        "goreczyno": {
            "headline": "u nas w domu — zero dojazdu",
            "p1": "Goręczyno to nasza baza — tu stoi nasz sprzęt, tu mieszka nasz zespół. Dla klientów z Goręczyna i okolic (Kamienica Szlachecka, Niestępowo, Szarłata) oznacza to jedno: zero kosztów dojazdu i najszybszy możliwy termin realizacji.",
            "p2": "Znamy każdy dom w okolicy — wiemy, które elewacje porastają najszybciej (te od strony lasu), które dachy zbierają najwięcej igliwia i gdzie gleba jest najbardziej wilgotna. Ta wiedza pozwala nam dobrać optymalną metodę od pierwszej wizyty.",
            "p3": "Jako lokalna firma zależy nam na reputacji w naszej gminie. Każda realizacja w Goręczynie to nasza wizytówka — dlatego traktujemy je ze szczególną starannością. Sąsiedzi polecają sąsiadom — i to najlepsza reklama."
        }
    },
    "mycie-dachu": {
        "kartuzy": {
            "headline": "dachy nad kaszubskimi jeziorami",
            "p1": "Dachy w Kartuzach mierzą się z podwójnym wyzwaniem — wilgocią znad jezior i opadem organicznym z okolicznych lasów. Mech rośnie tu wyjątkowo bujnie, pokrywając dachówki grubą warstwą w ciągu 3-4 lat.",
            "p2": "Na pagórkowatym terenie Kartuz dachy domów na wzniesieniach są dodatkowo wystawione na wiatr i deszcz, który wnika pod dachówki. Regularne mycie co 3-5 lat to minimum, aby utrzymać dach w dobrym stanie.",
            "p3": "Z Goręczyna do Kartuz — 20 minut. Myjemy dachy z podnośnika koszowego, bez chodzenia po dachówkach. Czyścimy kompleksowo: dachówki, rynny, obróbki blacharskie."
        },
        "zukowo": {
            "headline": "nowe dachy w starym lesie",
            "p1": "Tysiące nowych domów w gminie Żukowo (Banino, Chwaszczyno, Leźno) mają dachy, które nigdy nie były mytye. Po 5-10 latach na dawnych terenach leśnych — mech jest nieunikniony.",
            "p2": "Blachodachówka na nowych osiedlach pokrywa się mchem szybciej niż na terenach otwartych — cień od pozostawionych drzew i wilgoć z gliniastej gleby tworzą idealne warunki. Wczesne mycie + impregnacja to najlepsza profilaktyka.",
            "p3": "15 minut od naszej bazy — zero problemu z dojazdem. Znamy te osiedla doskonale. Typowy dach 150m² myjemy w jeden dzień."
        },
        "koscierzyna": {
            "headline": "kaszubskie dachy wśród lasów",
            "p1": "Dachy w Kościerzynie i okolicach porastają mchem wyjątkowo szybko — otoczenie jezior i Puszczy Kaszubskiej utrzymuje wilgotność przez cały rok. Igliwie sosnowe osiadające na dachówkach tworzy kwaśne podłoże idealne dla mchów.",
            "p2": "Starsze dachówki ceramiczne w centrum Kościerzyny wymagają delikatnego mycia — zbyt agresywne ciśnienie może je uszkodzić. Na obrzeżach dominuje blachodachówka, która po kilkunastu latach traci powłokę ochronną.",
            "p3": "Do Kościerzyny dojeżdżamy w 40 minut. Łączymy zlecenia w regionie — jeśli sąsiad też potrzebuje, obniżamy koszty dojazdu."
        },
        "bytow": {
            "headline": "dachy pod kaszubskim niebem",
            "p1": "Bytów, z ostrzejszym klimatem kontynentalnym, stawia dachom dodatkowe wyzwania. Mrozy, roztopy i duże wahania temperatur powodują mikropęknięcia dachówek, przez które wnika woda.",
            "p2": "Wiele dachów w Bytowie — szczególnie na starszych budynkach — nie było mytych od lat. Grube warstwy mchu zatrzymują wilgoć, która zimą zamarza i rozsadza pokrycie. Mycie teraz to zapobieganie kosztownej wymianie za kilka lat.",
            "p3": "Bytów to ok. 75 km. Realizujemy zlecenia pakietowo w regionie. Przyjeżdżamy z pełnym wyposażeniem — podnośnik, agregat, zapas preparatów."
        },
        "lebork": {
            "headline": "morski wiatr na kaszubskim dachu",
            "p1": "Dachy w Lęborku narażone na wilgoć z doliny Łeby i wiatry morskie z północy. Ta kombinacja sprzyja szybkiemu rozwojowi mchu i korozji obróbek blacharskich.",
            "p2": "Dachówki na starszych budynkach w centrum Lęborka wymagają delikatnego podejścia. Na nowych osiedlach — blachodachówka, którą trzeba myć regularnie, aby zapobiec korozji pod warstwą mchu.",
            "p3": "Dojazd ok. 1h 10min. Łączymy zlecenia w regionie lęborskim. Myjemy z podnośnika — bezpiecznie, bez chodzenia po dachu."
        },
        "goreczyno": {
            "headline": "twój sąsiad myje dachy",
            "p1": "W Goręczynie dachy porastają mchem jak wszędzie na Kaszubach — lasy, wilgoć, igliwie. Różnica? Twój wykonawca mieszka za rogiem. Zero dojazdu, najszybszy termin, najniższe koszty.",
            "p2": "Znamy dachy w Goręczynie i okolicach — wiemy, które pokrycia sprawdzają się najlepiej w naszym klimacie. Po myciu doradzimy, czy warto malować, impregnować, czy dach jest w stanie, który wymaga tylko czyszczenia.",
            "p3": "Dla klientów z Goręczyna i najbliższych wsi (Kamienica Szlachecka, Niestępowo) — ustalamy termin elastycznie, bo nie musimy planować długiego dojazdu."
        }
    },
    "malowanie-elewacji": {
        "kartuzy": {
            "headline": "kolor odporny na kaszubską wilgoć",
            "p1": "Malowanie elewacji w Kartuzach wymaga farb premium odpornych na wilgoć. Bliskość jezior i lasów oznacza stałą ekspozycję na podwyższoną wilgotność — tańsze farby nie wytrzymują dłużej niż 3-4 lata.",
            "p2": "Stosujemy farby silikonowe i siloksanowe, które odpychają wodę i pozwalają tynkowi oddychać. Przed malowaniem — pełne przygotowanie: mycie, odgrzybianie, gruntowanie, uzupełnienie ubytków.",
            "p3": "20 minut od bazy — szybki dojazd i niższe koszty. Malujemy z podnośnika koszowego natryskową metodą — równomiernie, bez śladów wałka."
        },
        "zukowo": {
            "headline": "nowa elewacja w 15 minut od bazy",
            "p1": "Domy w Baninie, Chwaszczynie i Leźnie po 5-10 latach od budowy często mają elewacje pokryte jedną warstwą taniej farby deweloperskiej. Czas na profesjonalne malowanie farbą premium.",
            "p2": "Na terenach dawnych lasów wilgoć jest stałym towarzyszem. Farba silikonowa tworzy barierę ochronną, która odpycha wodę i brud — elewacja dłużej zachowuje czystość i kolor.",
            "p3": "Żukowo to 15 minut od Goręczyna. Najkrótszy dojazd = najniższy koszt. Znamy deweloperskie tynki na tych osiedlach i wiemy, jak je prawidłowo przygotować pod malowanie."
        },
        "koscierzyna": {
            "headline": "elewacja godna stolicy Kaszub",
            "p1": "Kościerzyna, jako stolica Kaszub, zasługuje na zadbane elewacje. W centrum wiele budynków wymaga kompleksowej renowacji — mycie, naprawa tynku, gruntowanie i dwuwarstwowe malowanie.",
            "p2": "Na obrzeżach — nowe domy, które po kilkunastu latach potrzebują odświeżenia. Farba fasadowa klasy premium to inwestycja na 10-15 lat, nawet w wilgotnym kaszubskim klimacie.",
            "p3": "40 minut od bazy. Realizujemy zlecenia kompleksowo — od przygotowania podłoża po dwuwarstwowe malowanie z podnośnika."
        },
        "bytow": {
            "headline": "malowanie na kaszubskie mrozy",
            "p1": "Bytów z ostrzejszym klimatem wymaga farb elastycznych, odpornych na przymrozki i upały. Stosujemy farby, które pracują z tynkiem bez pękania przy dużych wahaniach temperatur.",
            "p2": "Wiele budynków w centrum Bytowa wymaga nie tylko malowania, ale naprawy tynku. Wykonujemy prace kompleksowo — klient dostaje gotową, wymalowaną elewację.",
            "p3": "75 km od bazy — planujemy wyjazdy pakietowo. Łączymy kilka zleceń w regionie bytowskim, co obniża koszty dojazdu dla każdego klienta."
        },
        "lebork": {
            "headline": "farba odporna na morski wiatr",
            "p1": "Lębork, z wpływem morskiego klimatu, wymaga farb fasadowych o podwyższonej odporności na zasolenie i wilgoć. Stosujemy farby siloksanowe, które tworzą trwałą barierę ochronną.",
            "p2": "Gotyckie budynki centrum wymagają szczególnej ostrożności — dobór koloru i techniki aplikacji musi respektować historyczny charakter zabudowy. Na obrzeżach — standardowe malowanie natryskowe z podnośnika.",
            "p3": "1h 10min od bazy. Realizujemy zlecenia w regionie lęborskim pakietowo. Pełne wyposażenie na pokładzie — generator, agregat, farby."
        },
        "goreczyno": {
            "headline": "malowanie u sąsiada — bez dojazdu",
            "p1": "Malowanie elewacji w Goręczynie i okolicach to dla nas zlecenie bez kosztów dojazdu. Całe oszczędności przekładamy na jakość — stosujemy najlepsze farby i poświęcamy więcej czasu na przygotowanie podłoża.",
            "p2": "Znamy kaszubskie warunki jak nikt — wiemy, które ściany wymagają farby o najwyższej hydrofobowości, a gdzie wystarczy standardowa fasadowa. To doświadczenie zdobyte na setkach realizacji w promieniu kilku kilometrów.",
            "p3": "Dla sąsiadów z Goręczyna — elastyczne terminy, brak kosztów dojazdu, gwarancja na wykonanie. Nasza reputacja zależy od jakości pracy tuż za progiem."
        }
    },
    "malowanie-dachu": {
        "kartuzy": {
            "headline": "dach nad kaszubskim jeziorem",
            "p1": "Dachy w Kartuzach narażone na wilgoć znad jezior i opad organiczny z lasów. Malowanie farbą antykorozyjną to najskuteczniejsza ochrona przed rdzą i degradacją pokrycia.",
            "p2": "Przed malowaniem dach myjemy, odgrzybiamy i gruntujemy. W kaszubskich warunkach pominięcie któregokolwiek kroku to gwarancja problemów w ciągu 2-3 lat.",
            "p3": "20 minut od bazy. Malujemy z podnośnika — bezpiecznie, bez chodzenia po dachu. Dwie warstwy farby z gwarancją."
        },
        "zukowo": {
            "headline": "dach nowego domu — czas na malowanie",
            "p1": "Blachodachówki na nowych osiedlach Żukowa (Banino, Chwaszczyno) mają 5-15 lat — fabryczna powłoka zaczyna tracić właściwości. Na wilgotnym terenie dawnych lasów korozja postępuje szybciej.",
            "p2": "Malowanie dachu teraz, gdy podłoże jest jeszcze w dobrym stanie, to oszczędność. Za kilka lat będzie trzeba dodatkowo usuwać rdzę i naprawiać perforacje.",
            "p3": "15 minut od bazy — najniższy koszt dojazdu. Typowy dach 150m² malujemy w 1-2 dni z podnośnika."
        },
        "koscierzyna": {
            "headline": "kaszubski dach jak nowy",
            "p1": "Dachy w Kościerzynie — zarówno dachówki ceramiczne starszych domów, jak i blachodachówki nowszych — wymagają regularnego malowania. Wilgoć z jezior i lasów przyspiesza degradację powłok.",
            "p2": "Stosujemy farby dedykowane do każdego typu pokrycia — antykorozyjne na blachę, paroprzepuszczalne na dachówkę. Każdy dach traktujemy indywidualnie.",
            "p3": "40 minut od bazy. Kompleksowa usługa: mycie + gruntowanie + 2 warstwy farby. Wszystko z podnośnika."
        },
        "bytow": {
            "headline": "antykorozja na kaszubskie zimy",
            "p1": "Dachy w Bytowie muszą wytrzymać ostre zimy — farba dachowa musi być elastyczna i odporna na cykle zamarzania i rozmarzania. Stosujemy produkty premium przeznaczone do ekstremalnych warunków.",
            "p2": "Wiele dachów w Bytowie nie było malowanych od lat. Im wcześniej malowanie, tym mniej kosztuje przygotowanie — rdza nie zdąży wnikać głęboko.",
            "p3": "75 km — realizujemy pakietowo. Malowanie dachu 150-200m² to 2-3 dni pracy z podnośnika."
        },
        "lebork": {
            "headline": "ochrona przed morską korozją",
            "p1": "Dachy w Lęborku narażone na zasolone powietrze z Bałtyku — korozja postępuje szybciej niż w głębi lądu. Malowanie farbą antykorozyjną klasy premium to konieczność, nie luksus.",
            "p2": "Obróbki blacharskie — rynny, wiatrownice, kołnierze — to najsłabsze punkty dachu w klimacie morskim. Malujemy je wraz z pokryciem, zapewniając kompletną ochronę.",
            "p3": "1h 10min dojazdu. Pakietowe zlecenia w regionie lęborskim. Pełne wyposażenie na pokładzie."
        },
        "goreczyno": {
            "headline": "malowanie dachu za rogiem",
            "p1": "Malowanie dachów w Goręczynie to nasza codzienność — znamy każdy typ pokrycia w okolicy. Zero dojazdu oznacza, że całość budżetu idzie na materiały i wykonanie, nie na transport.",
            "p2": "Kaszubski klimat jest wymagający dla dachów — wilgotne lasy, opad organiczny, przymrozki. Stosujemy farby, które sprawdziły się na setkach dachów w naszej okolicy.",
            "p3": "Dla sąsiadów — elastyczne terminy i najlepsza cena. Nasza reputacja w gminie to nasza najlepsza reklama."
        }
    },
    "impregnacja": {
        "kartuzy": {
            "headline": "tarcza na kaszubską wilgoć",
            "p1": "W Kartuzach, otoczonych jeziorami i lasami, impregnacja to absolutna konieczność po myciu. Bez niej elewacja porastanie za 2 lata. Z impregnacją — spokojnie 5-7 lat czystości.",
            "p2": "Impregnacja hydrofobowa szczególnie ważna jest przy domach nad jeziorami — stała wilgoć powoduje, że glony wracają najszybciej tam, gdzie jest najbliżej wody.",
            "p3": "20 minut od bazy. Pakiet mycie + impregnacja = 2× cena mycia, wieloletnia ochrona. Najlepsza inwestycja w kaszubskim klimacie."
        },
        "zukowo": {
            "headline": "ochrona nowego domu od samego początku",
            "p1": "Nowe domy w Baninie, Chwaszczynie i Leźnie powinny być zaimpregnowane profilaktycznie — zanim elewacja zacznie szarzeć. Deweloperzy tego nie robią, a wilgotny teren dawnych lasów przyspiesza degradację.",
            "p2": "Impregnacja w ciągu 2-3 lat od budowy to najtańsza opcja — tynk jest czysty, nie trzeba wcześniej myć. Preparat wnika głęboko i chroni na lata.",
            "p3": "15 minut dojazdu. Oferujemy pakiet nowy dom: przegląd + impregnacja profilaktyczna + zabezpieczenie cokołu. Idealne dla domów do 5 lat."
        },
        "koscierzyna": {
            "headline": "ochrona w krainie jezior",
            "p1": "Kościerzyna, otoczona jeziorami i Puszczą Kaszubską, to miejsce gdzie impregnacja daje najlepsze efekty. Różnica między elewacją zaimpregnowaną a nie — widoczna gołym okiem po 2 sezonach.",
            "p2": "Impregnujemy elewacje, dachy, cokoły i kostki brukowe. W Kościerzynie szczególnie polecamy pakiet: mycie elewacji + impregnacja + czyszczenie rynien.",
            "p3": "40 minut dojazdu. Łączymy zlecenia w regionie kościerskim. Impregnację wykonujemy bezpośrednio po myciu — jeden wyjazd, pełna ochrona."
        },
        "bytow": {
            "headline": "zabezpieczenie przed przymrozkami",
            "p1": "W Bytowie impregnacja chroni przede wszystkim przed wnikaniem wody, która zamarzając rozsadza tynk. Ostrzejszy klimat kontynentalny sprawia, że niezaimpregnowane elewacje pękają szybciej.",
            "p2": "Preparat hydrofobowy zmniejsza nasiąkliwość tynku o 95%. Woda nie wnika — nie ma czego zamrażać zimą. To bezpośrednio przekłada się na dłuższą żywotność elewacji.",
            "p3": "75 km — zlecenia pakietowe. Impregnacja po myciu w jednym podejściu. Cena = 100% ceny mycia."
        },
        "lebork": {
            "headline": "bariera przed morskim zasoleniem",
            "p1": "Lębork, z wpływem morskiego klimatu, to miejsce gdzie impregnacja chroni nie tylko przed wilgocią, ale i przed zasoleniem. Sól wnikająca w tynk powoduje wykwity i przyspiesza korozję.",
            "p2": "Impregnacja siloksanowa tworzy barierę odporną na sól morską. Elewacja zaimpregnowana w Lęborku utrzymuje czystość dłużej niż niezaimpregnowana w Kartuzach — mimo trudniejszych warunków.",
            "p3": "1h 10min dojazdu. Impregnację wykonujemy po myciu, w jednym podejściu. Pakietowe zlecenia w regionie."
        },
        "goreczyno": {
            "headline": "impregnacja u źródła — zero dojazdu",
            "p1": "Dla klientów z Goręczyna impregnacja jest szczególnie opłacalna — zero kosztów dojazdu oznacza, że cały budżet idzie na materiały i wykonanie. Stosujemy preparaty premium, bo oszczędzamy na transporcie.",
            "p2": "Znamy każdą elewację w okolicy — wiemy, które ściany wymagają impregnacji najbardziej (północne, zacienione, blisko lasu). Doradzamy gdzie warto zainwestować, a gdzie tynk radzi sobie sam.",
            "p3": "Pakiet mycie + impregnacja w Goręczynie to nasza najlepsza oferta cenowa. Sąsiedzi polecają sąsiadom — dołącz do grona zadowolonych klientów z gminy."
        }
    }
}

data['cities'].update(tier3_cities)

for service_slug, city_intros in intros.items():
    for city_slug, intro in city_intros.items():
        data['services'][service_slug]['intro_templates'][city_slug] = intro

with open('city-data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Total cities: {len(data['cities'])}")
print(f"✅ Total pages: {len(data['cities']) * len(data['services'])}")
