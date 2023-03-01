import csv
import json
import random
import re
import os
def row_to_obj(data):
    with open('./data/geojson/' + data[0] + "_xaaaa.geojson", 'r') as json_file:
        json_data = json.loads(json_file.read())
        return {
            "name": data[0].title(),
            "shim": re.sub('[^0-9a-zA-Z]+', '-', data[0].lower()),
            "rating_safety": float(data[9]),
            "rating_affordability": 100-float(data[17]),
            "geojson": json_data,
            "coords": {
                "lat": float(data[3]),
                "lng": float(data[2])
            },
            "stats": {
                "suburb-residents": {
                    "number":float(data[4]),
                    "year": "2016",
                },
                "total-crimes-by-year-and-area": {
                    "number":float(data[6]),
                    "year": "2016",
                },
                "offences-per-10000": {
                    "number":float(data[7]),
                    "year": "2016",
                },
                "suburb-town-name-2016-adjusted-crime-rank": {
                    "number":float(data[8]),
                    "year": "2016",
                },
                "offence-count": {
                    "number":float(data[10]),
                    "year": "2016",
                },
                "suburb-town-name-2016-real-crime-rank": {
                    "number":float(data[11]),
                    "year": "2016",
                },
                "suburb-most-common-expense-tier": {
                    "number":str(data[12]),
                    "year": "2016",
                },
                "number-of-rental-properties": {
                    "number":float(data[13]),
                    "year": "2016",
                },
                "price-range-rank": {
                    "number":100-float(data[14]),
                    "year": "2016",
                },
                "rental-price-range-lower": {
                    "number":float(data[15]),
                    "year": "2016",
                },
                "rental-price-range-upper": {
                    "number":float(data[16]),
                    "year": "2016",
                },
                "suburb-most-int-student-lang": {
                    "number":str(data[20]),
                    "year": "2016",
                },
                "total-int-students-per-suburb": {
                    "number":float(data[21]),
                    "year": "2016",
                },
                "total-int-student-per-language": {
                    "number":float(data[22]),
                    "year": "2016",
                },
                "student-population-rating": {
                    "number":float(data[23]),
                    "year": "2016",
                },
                "suburb-largest-lang-int-student-pop": {
                    "number":float(data[24]),
                    "year": "2016",
                },
                "suburb-largest-int-student-lang": {
                    "number":str(data[25]),
                    "year": "2016",
                },
                "percent-of-int-students-language-in-suburb": {
                    "number":float(data[26]),
                    "year": "2016",
                },
                "int-student-language-rank-all-langs": {
                    "number":float(data[27]),
                    "year": "2016",
                },
                "average-public-transport-users-per-suburb": {
                    "number":float(data[157]),
                    "year": "2016",
                },
                "total-public-transport-users-per-suburb": {
                    "number":float(data[158]),
                    "year": "2016",
                },
                "total-other-usage-by-suburb": {
                    "number":float(data[159]),
                    "year": "2016",
                },
                "adjusted-total-other-usage-scale-rank": {
                    "number":float(data[160]),
                    "year": "2016",
                },
                "adjusted-total-transport-use-per-suburb": {
                    "number":float(data[161]),
                    "year": "2016",
                },
                "adjusted-total-transport-use-per-suburb-rank": {
                    "number":float(data[162]),
                    "year": "2016",
                },
                "adjusted-total-transport-use-per-suburb-scale-rank": {
                    "number":float(data[163]),
                    "year": "2016",
                },
                "most-common-transport-method": {
                    "number":str(data[164]),
                    "year": "2016",
                },
                "most-common-distance-per-suburb": {
                    "number":str(data[165]),
                    "year": "2016",
                },
                "number-of-medical-workers": {
                    "number":float(data[632]),
                    "year": "2016",
                },
                "total-med-staff-per-suburb": {
                    "number":float(data[633]),
                    "year": "2016",
                },
                "suburb-med-staff-presence-by-type-rank": {
                    "number":float(data[634]),
                    "year": "2016",
                },
                "pop-per-doc": {
                    "number":float(data[635]),
                    "year": "2016",
                },
                "pop-per-doc-type": {
                    "number":float(data[636]),
                    "year": "2016",
                },
                "total-vic-med-staff": {
                    "number":float(data[637]),
                    "year": "2016",
                },
                "real-suburb-med-staff-presence-rank": {
                    "number":float(data[638]),
                    "year": "2016",
                },
                "suburb-adjusted-med-staff-presence-rank": {
                    "number":float(data[639]),
                    "year": "2016",
                },
                "suburb-adjusted-med-staff-by-type-presence-rank": {
                    "number":float(data[640]),
                    "year": "2016",
                },
                "population-adjusted-med-staff-rating": {
                    "number":float(data[641]),
                    "year": "2016",
                },
                "aged-care-residential-services": {
                    "number":float(data[662]),
                    "year": "2016",
                },
                "allied-health-services": {
                    "number":float(data[663]),
                    "year": "2016",
                },
                "ambulance-services": {
                    "number":float(data[664]),
                    "year": "2016",
                },
                "chiropractic-and-osteopathic-services": {
                    "number":float(data[665]),
                    "year": "2016",
                },
                "dental-services": {
                    "number":float(data[666]),
                    "year": "2016",
                },
                "general-practice-medical-services": {
                    "number":float(data[667]),
                    "year": "2016",
                },
                "hospitals": {
                    "number":float(data[668]),
                    "year": "2016",
                },
                "hospitals-except-psychiatric-hospitals": {
                    "number":float(data[669]),
                    "year": "2016",
                },
                "medical-and-other-health-care-services": {
                    "number":float(data[670]),
                    "year": "2016",
                },
                "medical-services": {
                    "number":float(data[671]),
                    "year": "2016",
                },
                "no-medical-facilities-in-the-area": {
                    "number":float(data[672]),
                    "year": "2016",
                },
                "optometry-and-optical-dispensing": {
                    "number":float(data[673]),
                    "year": "2016",
                },
                "other-allied-health-services": {
                    "number":float(data[674]),
                    "year": "2016",
                },
                "other-residential-care-services": {
                    "number":float(data[675]),
                    "year": "2016",
                },
                "pathology-and-diagnostic-imaging-services": {
                    "number":float(data[676]),
                    "year": "2016",
                },
                "physiotherapy-services": {
                    "number":float(data[677]),
                    "year": "2016",
                },
                "psychiatric-hospitals": {
                    "number":float(data[678]),
                    "year": "2016",
                },
                "residential-care-services": {
                    "number":float(data[679]),
                    "year": "2016",
                },
                "specialist-medical-services": {
                    "number":float(data[680]),
                    "year": "2016",
                },
                "number-of-police-place-of-work": {
                    "number":float(data[681]),
                    "year": "2016",
                },
                "pop-per-cop": {
                    "number":float(data[683]),
                    "year": "2016",
                },
                "total-vic-pol": {
                    "number":float(data[684]),
                    "year": "2016",
                },
                "suburb-police-presence-rank": {
                    "number":float(data[685]),
                    "year": "2016",
                },
                "suburb-adjusted-police-presence-rank": {
                    "number":float(data[686]),
                    "year": "2016",
                },
                "population-adjusted-police-rating": {
                    "number":float(data[687]),
                    "year": "2016",
                },


                "int-student-rental-price-bracket": {
                    "number":str(data[1056]),
                    "year": "2016",
                },
                "number-of-int-students-in-rental-bracket": {
                    "number":float(data[1057]),
                    "year": "2016",
                },
                "international-students-renting-in-suburb": {
                    "number":float(data[1058]),
                    "year": "2016",
                },
                "avg-rental-expenditure-per-int-student-per-suburb": {
                    "number":float(data[1059]),
                    "year": "2016",
                },
                "avg-rental-expenditure-for-int-students-in-victoria": {
                    "number":float(data[1060]),
                    "year": "2016",
                },
                "vic-int-student-most-common-expense-tier": {
                    "number":str(data[1061]),
                    "year": "2016",
                },
                "vic-total-crime-stats": {
                    "number":float(data[1062]),
                    "year": "2016",
                },
                "total-crime-in-suburb-stats": {
                    "number":float(data[1063]),
                    "year": "2016",
                },
                "avg-crime-per-suburb-vic-stats": {
                    "number":float(data[1064]),
                    "year": "2016",
                },
                "bus-line-flag": {
                    "number":True if data[167]=="Y" else False,
                    "year": "2016",
                },
                "ferry-flag": {
                    "number": True if data[168]=="Y" else False,
                    "year": "2016",
                },
                "suburb-aged-care-residential-services-fac-flag": {
                    "number":True if data[646]=="Y" else False,
                    "year": "2016",
                },
                "suburb-allied-health-services-fac-flag": {
                    "number":True if data[656]=="Y" else False,
                    "year": "2016",
                },
                "suburb-ambulance-services-fac-flag": {
                    "number":True if data[654]=="Y" else False,
                    "year": "2016",
                },
                "suburb-chiropractic-and-osteopathic-services-fac-flag": {
                    "number":True if data[644]=="Y" else False,
                    "year": "2016",
                },
                "suburb-dental-services-fac-flag": {
                    "number":True if data[651]=="Y" else False,
                    "year": "2016",
                },
                "suburb-general-practice-medical-services-fac-flag": {
                    "number":True if data[648]=="Y" else False,
                    "year": "2016",
                },
                "suburb-hospital-fac-flag": {
                    "number":True if data[658]=="Y" else False,
                    "year": "2016",
                },
                "suburb-hospitals-except-psychiatric-hospitals-fac-flag": {
                    "number":True if data[645]=="Y" else False,
                    "year": "2016",
                },
                "suburb-med-fac-flag": {
                    "number":True if data[642]=="Y" else False,
                    "year": "2016",
                },
                "suburb-medical-and-other-health-care-services-fac-flag": {
                    "number":True if data[661]=="Y" else False,
                    "year": "2016",
                },
                "suburb-medical-services-fac-flag": {
                    "number":True if data[659]=="Y" else False,
                    "year": "2016",
                },
                "suburb-optometry-optical-dispensing-services-fac-flag": {
                    "number":True if data[652]=="Y" else False,
                    "year": "2016",
                },
                "suburb-other-allied-health-services-fac-flag": {
                    "number":True if data[647]=="Y" else False,
                    "year": "2016",
                },
                "suburb-other-health-care-services-fac-flag": {
                    "number":True if data[653]=="Y" else False,
                    "year": "2016",
                },
                "suburb-other-residential-care-services-fac-flag": {
                    "number":True if data[660]=="Y" else False,
                    "year": "2016",
                },
                "suburb-pathology-and-diagnostic-imaging-services-fac-flag": {
                    "number":True if data[643]=="Y" else False,
                    "year": "2016",
                },
                "suburb-physiotherapy-services-fac-flag": {
                    "number":True if data[649]=="Y" else False,
                    "year": "2016",
                },
                "suburb-police-station-flag": {
                    "number":True if data[682]=="Y" else False,
                    "year": "2016",
                },
                "suburb-psychiatric-hospitals-fac-flag": {
                    "number":True if data[657]=="Y" else False,
                    "year": "2016",
                },
                "suburb-residential-care-services-fac-flag": {
                    "number":True if data[655]=="Y" else False,
                    "year": "2016",
                },
                "suburb-specialist-medical-services-fac-flag": {
                    "number":True if data[650]=="Y" else False,
                    "year": "2016",
                },
                "train-station-flag": {
                    "number":True if data[166]=="Y" else False,
                    "year": "2016",
                },
                "tram-line-flag": {
                    "number":True if data[169]=="Y" else False,
                    "year": "2016",
                },
            },
            "ethnic_population" : {
                "acholi": {
                    "number": float(data[688]) if data[688] != "NA" else 0,
                    "year": "2016",
                },
                "african-languages--nec": {
                    "number":float(data[689]) if data[689] != "NA" else 0,
                    "year": "2016",
                },
                "african-languages--nfd": {
                    "number":float(data[690]) if data[690] != "NA" else 0,
                    "year": "2016",
                },
                "afrikaans": {
                    "number":float(data[691]) if data[691] != "NA" else 0,
                    "year": "2016",
                },
                "akan": {
                    "number":float(data[692]) if data[692] != "NA" else 0,
                    "year": "2016",
                },
                "albanian": {
                    "number":float(data[693]) if data[693] != "NA" else 0,
                    "year": "2016",
                },
                "amharic": {
                    "number":float(data[694]) if data[694] != "NA" else 0,
                    "year": "2016",
                },
                "anuak": {
                    "number":float(data[695]) if data[695] != "NA" else 0,
                    "year": "2016",
                },
                "arabic": {
                    "number":float(data[696]) if data[696] != "NA" else 0,
                    "year": "2016",
                },
                "armenian": {
                    "number":float(data[697]) if data[697] != "NA" else 0,
                    "year": "2016",
                },
                "assyrian-neo-aramaic": {
                    "number":float(data[698]) if data[698] != "NA" else 0,
                    "year": "2016",
                },
                "bengali": {
                    "number":float(data[699]) if data[699] != "NA" else 0,
                    "year": "2016",
                },
                "bisaya": {
                    "number":float(data[700]) if data[700] != "NA" else 0,
                    "year": "2016",
                },
                "bosnian": {
                    "number":float(data[701]) if data[701] != "NA" else 0,
                    "year": "2016",
                },
                "bulgarian": {
                    "number":float(data[702]) if data[702] != "NA" else 0,
                    "year": "2016",
                },
                "burmese-and-related-languages--nec": {
                    "number":float(data[703]) if data[703] != "NA" else 0,
                    "year": "2016",
                },
                "burmese-and-related-languages--nfd": {
                    "number":float(data[704]) if data[704] != "NA" else 0,
                    "year": "2016",
                },
                "burmese": {
                    "number":float(data[705]) if data[705] != "NA" else 0,
                    "year": "2016",
                },
                "cantonese": {
                    "number":float(data[706]) if data[706] != "NA" else 0,
                    "year": "2016",
                },
                "catalan": {
                    "number":float(data[707]) if data[707] != "NA" else 0,
                    "year": "2016",
                },
                "cebuano": {
                    "number":float(data[708]) if data[708] != "NA" else 0,
                    "year": "2016",
                },
                "chaldean-neo-aramaic": {
                    "number":float(data[709]) if data[709] != "NA" else 0,
                    "year": "2016",
                },
                "chin-haka": {
                    "number":float(data[710]) if data[710] != "NA" else 0,
                    "year": "2016",
                },
                "chinese--nfd": {
                    "number":float(data[711]) if data[711] != "NA" else 0,
                    "year": "2016",
                },
                "creole--nfd": {
                    "number":float(data[712]) if data[712] != "NA" else 0,
                    "year": "2016",
                },
                "croatian": {
                    "number":float(data[713]) if data[713] != "NA" else 0,
                    "year": "2016",
                },
                "czech": {
                    "number":float(data[714]) if data[714] != "NA" else 0,
                    "year": "2016",
                },
                "danish": {
                    "number":float(data[715]) if data[715] != "NA" else 0,
                    "year": "2016",
                },
                "dari": {
                    "number":float(data[716]) if data[716] != "NA" else 0,
                    "year": "2016",
                },
                "dhivehi": {
                    "number":float(data[717]) if data[717] != "NA" else 0,
                    "year": "2016",
                },
                "dinka": {
                    "number":float(data[718]) if data[718] != "NA" else 0,
                    "year": "2016",
                },
                "dravidian--nec": {
                    "number":float(data[719]) if data[719] != "NA" else 0,
                    "year": "2016",
                },
                "dutch": {
                    "number":float(data[720]) if data[720] != "NA" else 0,
                    "year": "2016",
                },
                "english": {
                    "number":float(data[721]) if data[721] != "NA" else 0,
                    "year": "2016",
                },
                "estonian": {
                    "number":float(data[722]) if data[722] != "NA" else 0,
                    "year": "2016",
                },
                "fijian": {
                    "number":float(data[723]) if data[723] != "NA" else 0,
                    "year": "2016",
                },
                "filipino": {
                    "number":float(data[724]) if data[724] != "NA" else 0,
                    "year": "2016",
                },
                "finnish": {
                    "number":float(data[725]) if data[725] != "NA" else 0,
                    "year": "2016",
                },
                "french-creole--nfd": {
                    "number":float(data[726]) if data[726] != "NA" else 0,
                    "year": "2016",
                },
                "french": {
                    "number":float(data[727]) if data[727] != "NA" else 0,
                    "year": "2016",
                },
                "german": {
                    "number":float(data[728]) if data[728] != "NA" else 0,
                    "year": "2016",
                },
                "greek": {
                    "number":float(data[729]) if data[729] != "NA" else 0,
                    "year": "2016",
                },
                "gujarati": {
                    "number":float(data[730]) if data[730] != "NA" else 0,
                    "year": "2016",
                },
                "hakka": {
                    "number":float(data[731]) if data[731] != "NA" else 0,
                    "year": "2016",
                },
                "harari": {
                    "number":float(data[732]) if data[732] != "NA" else 0,
                    "year": "2016",
                },
                "hausa": {
                    "number":float(data[733]) if data[733] != "NA" else 0,
                    "year": "2016",
                },
                "hazaraghi": {
                    "number":float(data[734]) if data[734] != "NA" else 0,
                    "year": "2016",
                },
                "hebrew": {
                    "number":float(data[735]) if data[735] != "NA" else 0,
                    "year": "2016",
                },
                "hindi": {
                    "number":float(data[736]) if data[736] != "NA" else 0,
                    "year": "2016",
                },
                "hungarian": {
                    "number":float(data[737]) if data[737] != "NA" else 0,
                    "year": "2016",
                },
                "iban": {
                    "number":float(data[738]) if data[738] != "NA" else 0,
                    "year": "2016",
                },
                "igbo": {
                    "number":float(data[739]) if data[739] != "NA" else 0,
                    "year": "2016",
                },
                "ilonggo--hiligaynon-": {
                    "number":float(data[740]) if data[740] != "NA" else 0,
                    "year": "2016",
                },
                "inadequately-described": {
                    "number":float(data[741]) if data[741] != "NA" else 0,
                    "year": "2016",
                },
                "indonesian": {
                    "number":float(data[742]) if data[742] != "NA" else 0,
                    "year": "2016",
                },
                "iranic--nfd": {
                    "number":float(data[743]) if data[743] != "NA" else 0,
                    "year": "2016",
                },
                "italian": {
                    "number":float(data[744]) if data[744] != "NA" else 0,
                    "year": "2016",
                },
                "japanese": {
                    "number":float(data[745]) if data[745] != "NA" else 0,
                    "year": "2016",
                },
                "kannada": {
                    "number":float(data[746]) if data[746] != "NA" else 0,
                    "year": "2016",
                },
                "karen": {
                    "number":float(data[747]) if data[747] != "NA" else 0,
                    "year": "2016",
                },
                "khmer": {
                    "number":float(data[748]) if data[748] != "NA" else 0,
                    "year": "2016",
                },
                "kinyarwanda--rwanda-": {
                    "number":float(data[749]) if data[749] != "NA" else 0,
                    "year": "2016",
                },
                "kirundi--rundi-": {
                    "number":float(data[750]) if data[750] != "NA" else 0,
                    "year": "2016",
                },
                "konkani": {
                    "number":float(data[751]) if data[751] != "NA" else 0,
                    "year": "2016",
                },
                "korean": {
                    "number":float(data[752]) if data[752] != "NA" else 0,
                    "year": "2016",
                },
                "kurdish": {
                    "number":float(data[753]) if data[753] != "NA" else 0,
                    "year": "2016",
                },
                "lao": {
                    "number":float(data[754]) if data[754] != "NA" else 0,
                    "year": "2016",
                },
                "lithuanian": {
                    "number":float(data[755]) if data[755] != "NA" else 0,
                    "year": "2016",
                },
                "loma--lorma-": {
                    "number":float(data[756]) if data[756] != "NA" else 0,
                    "year": "2016",
                },
                "luganda": {
                    "number":float(data[757]) if data[757] != "NA" else 0,
                    "year": "2016",
                },
                "macedonian": {
                    "number":float(data[758]) if data[758] != "NA" else 0,
                    "year": "2016",
                },
                "malay": {
                    "number":float(data[759]) if data[759] != "NA" else 0,
                    "year": "2016",
                },
                "malayalam": {
                    "number":float(data[760]) if data[760] != "NA" else 0,
                    "year": "2016",
                },
                "maltese": {
                    "number":float(data[761]) if data[761] != "NA" else 0,
                    "year": "2016",
                },
                "mandarin": {
                    "number":float(data[762]) if data[762] != "NA" else 0,
                    "year": "2016",
                },
                "maori--cook-island-": {
                    "number":float(data[763]) if data[763] != "NA" else 0,
                    "year": "2016",
                },
                "maori--new-zealand-": {
                    "number":float(data[764]) if data[764] != "NA" else 0,
                    "year": "2016",
                },
                "marathi": {
                    "number":float(data[765]) if data[765] != "NA" else 0,
                    "year": "2016",
                },
                "mauritian-creole": {
                    "number":float(data[766]) if data[766] != "NA" else 0,
                    "year": "2016",
                },
                "min-nan": {
                    "number":float(data[767]) if data[767] != "NA" else 0,
                    "year": "2016",
                },
                "mongolian": {
                    "number":float(data[768]) if data[768] != "NA" else 0,
                    "year": "2016",
                },
                "nepali": {
                    "number":float(data[769]) if data[769] != "NA" else 0,
                    "year": "2016",
                },
                "norwegian": {
                    "number":float(data[770]) if data[770] != "NA" else 0,
                    "year": "2016",
                },
                "not-stated": {
                    "number":float(data[771]) if data[771] != "NA" else 0,
                    "year": "2016",
                },
                "nuer": {
                    "number":float(data[772]) if data[772] != "NA" else 0,
                    "year": "2016",
                },
                "nyanja--chichewa-": {
                    "number":float(data[773]) if data[773] != "NA" else 0,
                    "year": "2016",
                },
                "oriya": {
                    "number":float(data[774]) if data[774] != "NA" else 0,
                    "year": "2016",
                },
                "oromo": {
                    "number":float(data[775]) if data[775] != "NA" else 0,
                    "year": "2016",
                },
                "other-southern-asian-languages": {
                    "number":float(data[776]) if data[776] != "NA" else 0,
                    "year": "2016",
                },
                "pashto": {
                    "number":float(data[777]) if data[777] != "NA" else 0,
                    "year": "2016",
                },
                "persian--excluding-dari-": {
                    "number":float(data[778]) if data[778] != "NA" else 0,
                    "year": "2016",
                },
                "pidgin--nfd": {
                    "number":float(data[779]) if data[779] != "NA" else 0,
                    "year": "2016",
                },
                "polish": {
                    "number":float(data[780]) if data[780] != "NA" else 0,
                    "year": "2016",
                },
                "portuguese": {
                    "number":float(data[781]) if data[781] != "NA" else 0,
                    "year": "2016",
                },
                "punjabi": {
                    "number":float(data[782]) if data[782] != "NA" else 0,
                    "year": "2016",
                },
                "rohingya": {
                    "number":float(data[783]) if data[783] != "NA" else 0,
                    "year": "2016",
                },
                "romanian": {
                    "number":float(data[784]) if data[784] != "NA" else 0,
                    "year": "2016",
                },
                "russian": {
                    "number":float(data[785]) if data[785] != "NA" else 0,
                    "year": "2016",
                },
                "samoan": {
                    "number":float(data[786]) if data[786] != "NA" else 0,
                    "year": "2016",
                },
                "serbian": {
                    "number":float(data[787]) if data[787] != "NA" else 0,
                    "year": "2016",
                },
                "shilluk": {
                    "number":float(data[788]) if data[788] != "NA" else 0,
                    "year": "2016",
                },
                "shona": {
                    "number":float(data[789]) if data[789] != "NA" else 0,
                    "year": "2016",
                },
                "sindhi": {
                    "number":float(data[790]) if data[790] != "NA" else 0,
                    "year": "2016",
                },
                "sinhalese": {
                    "number":float(data[791]) if data[791] != "NA" else 0,
                    "year": "2016",
                },
                "slovak": {
                    "number":float(data[792]) if data[792] != "NA" else 0,
                    "year": "2016",
                },
                "slovene": {
                    "number":float(data[793]) if data[793] != "NA" else 0,
                    "year": "2016",
                },
                "somali": {
                    "number":float(data[794]) if data[794] != "NA" else 0,
                    "year": "2016",
                },
                "southern-asian-languages--nfd": {
                    "number":float(data[795]) if data[795] != "NA" else 0,
                    "year": "2016",
                },
                "spanish": {
                    "number":float(data[796]) if data[796] != "NA" else 0,
                    "year": "2016",
                },
                "swahili": {
                    "number":float(data[797]) if data[797] != "NA" else 0,
                    "year": "2016",
                },
                "swedish": {
                    "number":float(data[798]) if data[798] != "NA" else 0,
                    "year": "2016",
                },
                "tagalog": {
                    "number":float(data[799]) if data[799] != "NA" else 0,
                    "year": "2016",
                },
                "tamil": {
                    "number":float(data[800]) if data[800] != "NA" else 0,
                    "year": "2016",
                },
                "telugu": {
                    "number":float(data[801]) if data[801] != "NA" else 0,
                    "year": "2016",
                },
                "tetum": {
                    "number":float(data[802]) if data[802] != "NA" else 0,
                    "year": "2016",
                },
                "thai": {
                    "number":float(data[803]) if data[803] != "NA" else 0,
                    "year": "2016",
                },
                "tibetan": {
                    "number":float(data[804]) if data[804] != "NA" else 0,
                    "year": "2016",
                },
                "tigrinya": {
                    "number":float(data[805]) if data[805] != "NA" else 0,
                    "year": "2016",
                },
                "tok-pisin--neomelanesian-": {
                    "number":float(data[806]) if data[806] != "NA" else 0,
                    "year": "2016",
                },
                "tongan": {
                    "number":float(data[807]) if data[807] != "NA" else 0,
                    "year": "2016",
                },
                "tswana": {
                    "number":float(data[808]) if data[808] != "NA" else 0,
                    "year": "2016",
                },
                "turkish": {
                    "number":float(data[809]) if data[809] != "NA" else 0,
                    "year": "2016",
                },
                "tuvaluan": {
                    "number":float(data[810]) if data[810] != "NA" else 0,
                    "year": "2016",
                },
                "ukrainian": {
                    "number":float(data[811]) if data[811] != "NA" else 0,
                    "year": "2016",
                },
                "urdu": {
                    "number":float(data[812]) if data[812] != "NA" else 0,
                    "year": "2016",
                },
                "vietnamese": {
                    "number":float(data[813]) if data[813] != "NA" else 0,
                    "year": "2016",
                },
                "wu": {
                    "number":float(data[814]) if data[814] != "NA" else 0,
                    "year": "2016",
                },
                "yoruba": {
                    "number":float(data[815]) if data[815] != "NA" else 0,
                    "year": "2016",
                },
                "zomi": {
                    "number":float(data[816]) if data[816] != "NA" else 0,
                    "year": "2016",
                }
            },
            "suburb_speaks": {
                "aboriginal-english": {
                    "number":float(data[817]) if data[817] != "NA" else 0,
                    "year": "2016",
                },
                "acholi": {
                    "number":float(data[818]) if data[818] != "NA" else 0,
                    "year": "2016",
                },
                "african-languages": {
                    "number":float(data[819]) if data[819] != "NA" else 0,
                    "year": "2016",
                },
                "afrikaans": {
                    "number":float(data[820]) if data[820] != "NA" else 0,
                    "year": "2016",
                },
                "akan": {
                    "number":float(data[821]) if data[821] != "NA" else 0,
                    "year": "2016",
                },
                "albanian": {
                    "number":float(data[822]) if data[822] != "NA" else 0,
                    "year": "2016",
                },
                "american-languages": {
                    "number":float(data[823]) if data[823] != "NA" else 0,
                    "year": "2016",
                },
                "amharic": {
                    "number":float(data[824]) if data[824] != "NA" else 0,
                    "year": "2016",
                },
                "anuak": {
                    "number":float(data[825]) if data[825] != "NA" else 0,
                    "year": "2016",
                },
                "arabic": {
                    "number":float(data[826]) if data[826] != "NA" else 0,
                    "year": "2016",
                },
                "armenian": {
                    "number":float(data[827]) if data[827] != "NA" else 0,
                    "year": "2016",
                },
                "aromunian-(macedo-romanian)": {
                    "number":float(data[828]) if data[828] != "NA" else 0,
                    "year": "2016",
                },
                "assamese": {
                    "number":float(data[829]) if data[829] != "NA" else 0,
                    "year": "2016",
                },
                "assyrian-neo-aramaic": {
                    "number":float(data[830]) if data[830] != "NA" else 0,
                    "year": "2016",
                },
                "auslan": {
                    "number":float(data[831]) if data[831] != "NA" else 0,
                    "year": "2016",
                },
                "australian-indigenous-languages": {
                    "number":float(data[832]) if data[832] != "NA" else 0,
                    "year": "2016",
                },
                "azeri": {
                    "number":float(data[833]) if data[833] != "NA" else 0,
                    "year": "2016",
                },
                "balinese": {
                    "number":float(data[834]) if data[834] != "NA" else 0,
                    "year": "2016",
                },
                "balochi": {
                    "number":float(data[835]) if data[835] != "NA" else 0,
                    "year": "2016",
                },
                "bari": {
                    "number":float(data[836]) if data[836] != "NA" else 0,
                    "year": "2016",
                },
                "basque": {
                    "number":float(data[837]) if data[837] != "NA" else 0,
                    "year": "2016",
                },
                "bassa": {
                    "number":float(data[838]) if data[838] != "NA" else 0,
                    "year": "2016",
                },
                "belorussian": {
                    "number":float(data[839]) if data[839] != "NA" else 0,
                    "year": "2016",
                },
                "bemba": {
                    "number":float(data[840]) if data[840] != "NA" else 0,
                    "year": "2016",
                },
                "bengali": {
                    "number":float(data[841]) if data[841] != "NA" else 0,
                    "year": "2016",
                },
                "bidjara": {
                    "number":float(data[842]) if data[842] != "NA" else 0,
                    "year": "2016",
                },
                "bikol": {
                    "number":float(data[843]) if data[843] != "NA" else 0,
                    "year": "2016",
                },
                "bisaya": {
                    "number":float(data[844]) if data[844] != "NA" else 0,
                    "year": "2016",
                },
                "bislama": {
                    "number":float(data[845]) if data[845] != "NA" else 0,
                    "year": "2016",
                },
                "bosnian": {
                    "number":float(data[846]) if data[846] != "NA" else 0,
                    "year": "2016",
                },
                "bulgarian": {
                    "number":float(data[847]) if data[847] != "NA" else 0,
                    "year": "2016",
                },
                "burmese": {
                    "number":float(data[848]) if data[848] != "NA" else 0,
                    "year": "2016",
                },
                "burmese-and-related-languages": {
                    "number":float(data[849]) if data[849] != "NA" else 0,
                    "year": "2016",
                },
                "cantonese": {
                    "number":float(data[850]) if data[850] != "NA" else 0,
                    "year": "2016",
                },
                "catalan": {
                    "number":float(data[851]) if data[851] != "NA" else 0,
                    "year": "2016",
                },
                "cebuano": {
                    "number":float(data[852]) if data[852] != "NA" else 0,
                    "year": "2016",
                },
                "celtic": {
                    "number":float(data[853]) if data[853] != "NA" else 0,
                    "year": "2016",
                },
                "chaldean-neo-aramaic": {
                    "number":float(data[854]) if data[854] != "NA" else 0,
                    "year": "2016",
                },
                "chin-haka": {
                    "number":float(data[855]) if data[855] != "NA" else 0,
                    "year": "2016",
                },
                "chinese": {
                    "number":float(data[856]) if data[856] != "NA" else 0,
                    "year": "2016",
                },
                "creole": {
                    "number":float(data[857]) if data[857] != "NA" else 0,
                    "year": "2016",
                },
                "croatian": {
                    "number":float(data[858]) if data[858] != "NA" else 0,
                    "year": "2016",
                },
                "cypriot": {
                    "number":float(data[859]) if data[859] != "NA" else 0,
                    "year": "2016",
                },
                "czech": {
                    "number":float(data[860]) if data[860] != "NA" else 0,
                    "year": "2016",
                },
                "czechoslovakian": {
                    "number":float(data[861]) if data[861] != "NA" else 0,
                    "year": "2016",
                },
                "dan-(gio-dan)": {
                    "number":float(data[862]) if data[862] != "NA" else 0,
                    "year": "2016",
                },
                "danish": {
                    "number":float(data[863]) if data[863] != "NA" else 0,
                    "year": "2016",
                },
                "dari": {
                    "number":float(data[864]) if data[864] != "NA" else 0,
                    "year": "2016",
                },
                "dhivehi": {
                    "number":float(data[865]) if data[865] != "NA" else 0,
                    "year": "2016",
                },
                "dinka": {
                    "number":float(data[866]) if data[866] != "NA" else 0,
                    "year": "2016",
                },
                "djambarrpuyngu": {
                    "number":float(data[867]) if data[867] != "NA" else 0,
                    "year": "2016",
                },
                "dravidian": {
                    "number":float(data[868]) if data[868] != "NA" else 0,
                    "year": "2016",
                },
                "dutch": {
                    "number":float(data[869]) if data[869] != "NA" else 0,
                    "year": "2016",
                },
                "eastern-european-languages": {
                    "number":float(data[870]) if data[870] != "NA" else 0,
                    "year": "2016",
                },
                "english": {
                    "number":float(data[871]) if data[871] != "NA" else 0,
                    "year": "2016",
                },
                "estonian": {
                    "number":float(data[872]) if data[872] != "NA" else 0,
                    "year": "2016",
                },
                "ewe": {
                    "number":float(data[873]) if data[873] != "NA" else 0,
                    "year": "2016",
                },
                "fijian": {
                    "number":float(data[874]) if data[874] != "NA" else 0,
                    "year": "2016",
                },
                "fijian-hindustani": {
                    "number":float(data[875]) if data[875] != "NA" else 0,
                    "year": "2016",
                },
                "filipino": {
                    "number":float(data[876]) if data[876] != "NA" else 0,
                    "year": "2016",
                },
                "finnish": {
                    "number":float(data[877]) if data[877] != "NA" else 0,
                    "year": "2016",
                },
                "french": {
                    "number":float(data[878]) if data[878] != "NA" else 0,
                    "year": "2016",
                },
                "french-creole": {
                    "number":float(data[879]) if data[879] != "NA" else 0,
                    "year": "2016",
                },
                "frisian": {
                    "number":float(data[880]) if data[880] != "NA" else 0,
                    "year": "2016",
                },
                "fulfulde": {
                    "number":float(data[881]) if data[881] != "NA" else 0,
                    "year": "2016",
                },
                "ga": {
                    "number":float(data[882]) if data[882] != "NA" else 0,
                    "year": "2016",
                },
                "gaelic-(scotland)": {
                    "number":float(data[883]) if data[883] != "NA" else 0,
                    "year": "2016",
                },
                "georgian": {
                    "number":float(data[884]) if data[884] != "NA" else 0,
                    "year": "2016",
                },
                "german": {
                    "number":float(data[885]) if data[885] != "NA" else 0,
                    "year": "2016",
                },
                "gilbertese": {
                    "number":float(data[886]) if data[886] != "NA" else 0,
                    "year": "2016",
                },
                "greek": {
                    "number":float(data[887]) if data[887] != "NA" else 0,
                    "year": "2016",
                },
                "gujarati": {
                    "number":float(data[888]) if data[888] != "NA" else 0,
                    "year": "2016",
                },
                "guugu-yimidhirr": {
                    "number":float(data[889]) if data[889] != "NA" else 0,
                    "year": "2016",
                },
                "hakka": {
                    "number":float(data[890]) if data[890] != "NA" else 0,
                    "year": "2016",
                },
                "harari": {
                    "number":float(data[891]) if data[891] != "NA" else 0,
                    "year": "2016",
                },
                "hausa": {
                    "number":float(data[892]) if data[892] != "NA" else 0,
                    "year": "2016",
                },
                "hazaraghi": {
                    "number":float(data[893]) if data[893] != "NA" else 0,
                    "year": "2016",
                },
                "hebrew": {
                    "number":float(data[894]) if data[894] != "NA" else 0,
                    "year": "2016",
                },
                "hindi": {
                    "number":float(data[895]) if data[895] != "NA" else 0,
                    "year": "2016",
                },
                "hmong": {
                    "number":float(data[896]) if data[896] != "NA" else 0,
                    "year": "2016",
                },
                "hungarian": {
                    "number":float(data[897]) if data[897] != "NA" else 0,
                    "year": "2016",
                },
                "iban": {
                    "number":float(data[898]) if data[898] != "NA" else 0,
                    "year": "2016",
                },
                "iberian-romance": {
                    "number":float(data[899]) if data[899] != "NA" else 0,
                    "year": "2016",
                },
                "icelandic": {
                    "number":float(data[900]) if data[900] != "NA" else 0,
                    "year": "2016",
                },
                "igbo": {
                    "number":float(data[901]) if data[901] != "NA" else 0,
                    "year": "2016",
                },
                "iiokano": {
                    "number":float(data[902]) if data[902] != "NA" else 0,
                    "year": "2016",
                },
                "ilonggo-(hiligaynon)": {
                    "number":float(data[903]) if data[903] != "NA" else 0,
                    "year": "2016",
                },
                "inadequately-described": {
                    "number":float(data[904]) if data[904] != "NA" else 0,
                    "year": "2016",
                },
                "indo-aryan": {
                    "number":float(data[905]) if data[905] != "NA" else 0,
                    "year": "2016",
                },
                "indonesian": {
                    "number":float(data[906]) if data[906] != "NA" else 0,
                    "year": "2016",
                },
                "invented-languages": {
                    "number":float(data[907]) if data[907] != "NA" else 0,
                    "year": "2016",
                },
                "iranic": {
                    "number":float(data[908]) if data[908] != "NA" else 0,
                    "year": "2016",
                },
                "irish": {
                    "number":float(data[909]) if data[909] != "NA" else 0,
                    "year": "2016",
                },
                "italian": {
                    "number":float(data[910]) if data[910] != "NA" else 0,
                    "year": "2016",
                },
                "japanese": {
                    "number":float(data[911]) if data[911] != "NA" else 0,
                    "year": "2016",
                },
                "javanese": {
                    "number":float(data[912]) if data[912] != "NA" else 0,
                    "year": "2016",
                },
                "kanai": {
                    "number":float(data[913]) if data[913] != "NA" else 0,
                    "year": "2016",
                },
                "kannada": {
                    "number":float(data[914]) if data[914] != "NA" else 0,
                    "year": "2016",
                },
                "karen": {
                    "number":float(data[915]) if data[915] != "NA" else 0,
                    "year": "2016",
                },
                "kashmiri": {
                    "number":float(data[916]) if data[916] != "NA" else 0,
                    "year": "2016",
                },
                "key-word-sign-australia": {
                    "number":float(data[917]) if data[917] != "NA" else 0,
                    "year": "2016",
                },
                "khmer": {
                    "number":float(data[918]) if data[918] != "NA" else 0,
                    "year": "2016",
                },
                "kikuyu": {
                    "number":float(data[919]) if data[919] != "NA" else 0,
                    "year": "2016",
                },
                "kinyarwanda-(rwanda)": {
                    "number":float(data[920]) if data[920] != "NA" else 0,
                    "year": "2016",
                },
                "kirundi-(rundi)": {
                    "number":float(data[921]) if data[921] != "NA" else 0,
                    "year": "2016",
                },
                "konkani": {
                    "number":float(data[922]) if data[922] != "NA" else 0,
                    "year": "2016",
                },
                "korean": {
                    "number":float(data[923]) if data[923] != "NA" else 0,
                    "year": "2016",
                },
                "krahn": {
                    "number":float(data[924]) if data[924] != "NA" else 0,
                    "year": "2016",
                },
                "krio": {
                    "number":float(data[925]) if data[925] != "NA" else 0,
                    "year": "2016",
                },
                "kriol": {
                    "number":float(data[926]) if data[926] != "NA" else 0,
                    "year": "2016",
                },
                "kune": {
                    "number":float(data[927]) if data[927] != "NA" else 0,
                    "year": "2016",
                },
                "kurdish": {
                    "number":float(data[928]) if data[928] != "NA" else 0,
                    "year": "2016",
                },
                "lao": {
                    "number":float(data[929]) if data[929] != "NA" else 0,
                    "year": "2016",
                },
                "latin": {
                    "number":float(data[930]) if data[930] != "NA" else 0,
                    "year": "2016",
                },
                "latvian": {
                    "number":float(data[931]) if data[931] != "NA" else 0,
                    "year": "2016",
                },
                "letzeburgish": {
                    "number":float(data[932]) if data[932] != "NA" else 0,
                    "year": "2016",
                },
                "liberian-(liberian-english)": {
                    "number":float(data[933]) if data[933] != "NA" else 0,
                    "year": "2016",
                },
                "lingala": {
                    "number":float(data[934]) if data[934] != "NA" else 0,
                    "year": "2016",
                },
                "lithuanian": {
                    "number":float(data[935]) if data[935] != "NA" else 0,
                    "year": "2016",
                },
                "loma-(lorma)": {
                    "number":float(data[936]) if data[936] != "NA" else 0,
                    "year": "2016",
                },
                "luganda": {
                    "number":float(data[937]) if data[937] != "NA" else 0,
                    "year": "2016",
                },
                "luo": {
                    "number":float(data[938]) if data[938] != "NA" else 0,
                    "year": "2016",
                },
                "macedonian": {
                    "number":float(data[939]) if data[939] != "NA" else 0,
                    "year": "2016",
                },
                "madi": {
                    "number":float(data[940]) if data[940] != "NA" else 0,
                    "year": "2016",
                },
                "malay": {
                    "number":float(data[941]) if data[941] != "NA" else 0,
                    "year": "2016",
                },
                "malayalam": {
                    "number":float(data[942]) if data[942] != "NA" else 0,
                    "year": "2016",
                },
                "maltese": {
                    "number":float(data[943]) if data[943] != "NA" else 0,
                    "year": "2016",
                },
                "mandaean-(mandaic)": {
                    "number":float(data[944]) if data[944] != "NA" else 0,
                    "year": "2016",
                },
                "mandarin": {
                    "number":float(data[945]) if data[945] != "NA" else 0,
                    "year": "2016",
                },
                "mandinka": {
                    "number":float(data[946]) if data[946] != "NA" else 0,
                    "year": "2016",
                },
                "mann": {
                    "number":float(data[947]) if data[947] != "NA" else 0,
                    "year": "2016",
                },
                "manyjilyjarra": {
                    "number":float(data[948]) if data[948] != "NA" else 0,
                    "year": "2016",
                },
                "maori-(cook-island)": {
                    "number":float(data[949]) if data[949] != "NA" else 0,
                    "year": "2016",
                },
                "maori-(new-zealand)": {
                    "number":float(data[950]) if data[950] != "NA" else 0,
                    "year": "2016",
                },
                "marathi": {
                    "number":float(data[951]) if data[951] != "NA" else 0,
                    "year": "2016",
                },
                "mauritian-creole": {
                    "number":float(data[952]) if data[952] != "NA" else 0,
                    "year": "2016",
                },
                "middle-eastern-semitic-languages": {
                    "number":float(data[953]) if data[953] != "NA" else 0,
                    "year": "2016",
                },
                "min-nan": {
                    "number":float(data[954]) if data[954] != "NA" else 0,
                    "year": "2016",
                },
                "mon": {
                    "number":float(data[955]) if data[955] != "NA" else 0,
                    "year": "2016",
                },
                "mon-khmer": {
                    "number":float(data[956]) if data[956] != "NA" else 0,
                    "year": "2016",
                },
                "mongolian": {
                    "number":float(data[957]) if data[957] != "NA" else 0,
                    "year": "2016",
                },
                "moro-(nuba-moro)": {
                    "number":float(data[958]) if data[958] != "NA" else 0,
                    "year": "2016",
                },
                "motu-(hirimotu)": {
                    "number":float(data[959]) if data[959] != "NA" else 0,
                    "year": "2016",
                },
                "murrinh-patha": {
                    "number":float(data[960]) if data[960] != "NA" else 0,
                    "year": "2016",
                },
                "nauruan": {
                    "number":float(data[961]) if data[961] != "NA" else 0,
                    "year": "2016",
                },
                "ndebele": {
                    "number":float(data[962]) if data[962] != "NA" else 0,
                    "year": "2016",
                },
                "nepali": {
                    "number":float(data[963]) if data[963] != "NA" else 0,
                    "year": "2016",
                },
                "ngarrindjeri": {
                    "number":float(data[964]) if data[964] != "NA" else 0,
                    "year": "2016",
                },
                "niue": {
                    "number":float(data[965]) if data[965] != "NA" else 0,
                    "year": "2016",
                },
                "norf'k-pitcairn": {
                    "number":float(data[966]) if data[966] != "NA" else 0,
                    "year": "2016",
                },
                "norwegian": {
                    "number":float(data[967]) if data[967] != "NA" else 0,
                    "year": "2016",
                },
                "nuer": {
                    "number":float(data[968]) if data[968] != "NA" else 0,
                    "year": "2016",
                },
                "nyanja-(chichewa)": {
                    "number":float(data[969]) if data[969] != "NA" else 0,
                    "year": "2016",
                },
                "nyungar": {
                    "number":float(data[970]) if data[970] != "NA" else 0,
                    "year": "2016",
                },
                "oceanian-pidgins-and-creoles": {
                    "number":float(data[971]) if data[971] != "NA" else 0,
                    "year": "2016",
                },
                "oriya": {
                    "number":float(data[972]) if data[972] != "NA" else 0,
                    "year": "2016",
                },
                "oromo": {
                    "number":float(data[973]) if data[973] != "NA" else 0,
                    "year": "2016",
                },
                "other-eastern-asian-languages": {
                    "number":float(data[974]) if data[974] != "NA" else 0,
                    "year": "2016",
                },
                "other-southeast-asian-languages": {
                    "number":float(data[975]) if data[975] != "NA" else 0,
                    "year": "2016",
                },
                "other-southern-asian-languages": {
                    "number":float(data[976]) if data[976] != "NA" else 0,
                    "year": "2016",
                },
                "other-southern-european-languages": {
                    "number":float(data[977]) if data[977] != "NA" else 0,
                    "year": "2016",
                },
                "paakantyi": {
                    "number":float(data[978]) if data[978] != "NA" else 0,
                    "year": "2016",
                },
                "pacific-austronesian-languages": {
                    "number":float(data[979]) if data[979] != "NA" else 0,
                    "year": "2016",
                },
                "pampangan": {
                    "number":float(data[980]) if data[980] != "NA" else 0,
                    "year": "2016",
                },
                "papua-new-guinea-languages": {
                    "number":float(data[981]) if data[981] != "NA" else 0,
                    "year": "2016",
                },
                "pashto": {
                    "number":float(data[982]) if data[982] != "NA" else 0,
                    "year": "2016",
                },
                "persian-(excluding-dari)": {
                    "number":float(data[983]) if data[983] != "NA" else 0,
                    "year": "2016",
                },
                "pidgin": {
                    "number":float(data[984]) if data[984] != "NA" else 0,
                    "year": "2016",
                },
                "pitjantjatjara": {
                    "number":float(data[985]) if data[985] != "NA" else 0,
                    "year": "2016",
                },
                "polish": {
                    "number":float(data[986]) if data[986] != "NA" else 0,
                    "year": "2016",
                },
                "portuguese": {
                    "number":float(data[987]) if data[987] != "NA" else 0,
                    "year": "2016",
                },
                "portuguese-creole": {
                    "number":float(data[988]) if data[988] != "NA" else 0,
                    "year": "2016",
                },
                "punjabi": {
                    "number":float(data[989]) if data[989] != "NA" else 0,
                    "year": "2016",
                },
                "rohingya": {
                    "number":float(data[990]) if data[990] != "NA" else 0,
                    "year": "2016",
                },
                "romanian": {
                    "number":float(data[991]) if data[991] != "NA" else 0,
                    "year": "2016",
                },
                "romany": {
                    "number":float(data[992]) if data[992] != "NA" else 0,
                    "year": "2016",
                },
                "rotuman": {
                    "number":float(data[993]) if data[993] != "NA" else 0,
                    "year": "2016",
                },
                "russian": {
                    "number":float(data[994]) if data[994] != "NA" else 0,
                    "year": "2016",
                },
                "samoan": {
                    "number":float(data[995]) if data[995] != "NA" else 0,
                    "year": "2016",
                },
                "scandinavian": {
                    "number":float(data[996]) if data[996] != "NA" else 0,
                    "year": "2016",
                },
                "serbian": {
                    "number":float(data[997]) if data[997] != "NA" else 0,
                    "year": "2016",
                },
                "serbo-croatian/yugoslavian": {
                    "number":float(data[998]) if data[998] != "NA" else 0,
                    "year": "2016",
                },
                "seychelles-creole": {
                    "number":float(data[999]) if data[999] != "NA" else 0,
                    "year": "2016",
                },
                "shilluk": {
                    "number":float(data[1000]) if data[1000] != "NA" else 0,
                    "year": "2016",
                },
                "shona": {
                    "number":float(data[1001]) if data[1001] != "NA" else 0,
                    "year": "2016",
                },
                "sign-languages": {
                    "number":float(data[1002]) if data[1002] != "NA" else 0,
                    "year": "2016",
                },
                "sindhi": {
                    "number":float(data[1003]) if data[1003] != "NA" else 0,
                    "year": "2016",
                },
                "sinhalese": {
                    "number":float(data[1004]) if data[1004] != "NA" else 0,
                    "year": "2016",
                },
                "slovak": {
                    "number":float(data[1005]) if data[1005] != "NA" else 0,
                    "year": "2016",
                },
                "slovene": {
                    "number":float(data[1006]) if data[1006] != "NA" else 0,
                    "year": "2016",
                },
                "somali": {
                    "number":float(data[1007]) if data[1007] != "NA" else 0,
                    "year": "2016",
                },
                "southeast-asian-austronesian-languages": {
                    "number":float(data[1008]) if data[1008] != "NA" else 0,
                    "year": "2016",
                },
                "southern-asian-languages": {
                    "number":float(data[1009]) if data[1009] != "NA" else 0,
                    "year": "2016",
                },
                "spanish": {
                    "number":float(data[1010]) if data[1010] != "NA" else 0,
                    "year": "2016",
                },
                "spanish-creole": {
                    "number":float(data[1011]) if data[1011] != "NA" else 0,
                    "year": "2016",
                },
                "swahili": {
                    "number":float(data[1012]) if data[1012] != "NA" else 0,
                    "year": "2016",
                },
                "swedish": {
                    "number":float(data[1013]) if data[1013] != "NA" else 0,
                    "year": "2016",
                },
                "swiss": {
                    "number":float(data[1014]) if data[1014] != "NA" else 0,
                    "year": "2016",
                },
                "tagalog": {
                    "number":float(data[1015]) if data[1015] != "NA" else 0,
                    "year": "2016",
                },
                "tai": {
                    "number":float(data[1016]) if data[1016] != "NA" else 0,
                    "year": "2016",
                },
                "tamil": {
                    "number":float(data[1017]) if data[1017] != "NA" else 0,
                    "year": "2016",
                },
                "tatar": {
                    "number":float(data[1018]) if data[1018] != "NA" else 0,
                    "year": "2016",
                },
                "telugu": {
                    "number":float(data[1019]) if data[1019] != "NA" else 0,
                    "year": "2016",
                },
                "tetum": {
                    "number":float(data[1020]) if data[1020] != "NA" else 0,
                    "year": "2016",
                },
                "thai": {
                    "number":float(data[1021]) if data[1021] != "NA" else 0,
                    "year": "2016",
                },
                "tibetan": {
                    "number":float(data[1022]) if data[1022] != "NA" else 0,
                    "year": "2016",
                },
                "tigre": {
                    "number":float(data[1023]) if data[1023] != "NA" else 0,
                    "year": "2016",
                },
                "tigrinya": {
                    "number":float(data[1024]) if data[1024] != "NA" else 0,
                    "year": "2016",
                },
                "timorese": {
                    "number":float(data[1025]) if data[1025] != "NA" else 0,
                    "year": "2016",
                },
                "tok-pisin-(neomelanesian)": {
                    "number":float(data[1026]) if data[1026] != "NA" else 0,
                    "year": "2016",
                },
                "tokelauan": {
                    "number":float(data[1027]) if data[1027] != "NA" else 0,
                    "year": "2016",
                },
                "tongan": {
                    "number":float(data[1028]) if data[1028] != "NA" else 0,
                    "year": "2016",
                },
                "tswana": {
                    "number":float(data[1029]) if data[1029] != "NA" else 0,
                    "year": "2016",
                },
                "tulu": {
                    "number":float(data[1030]) if data[1030] != "NA" else 0,
                    "year": "2016",
                },
                "turkic": {
                    "number":float(data[1031]) if data[1031] != "NA" else 0,
                    "year": "2016",
                },
                "turkish": {
                    "number":float(data[1032]) if data[1032] != "NA" else 0,
                    "year": "2016",
                },
                "turkmen": {
                    "number":float(data[1033]) if data[1033] != "NA" else 0,
                    "year": "2016",
                },
                "tuvaluan": {
                    "number":float(data[1034]) if data[1034] != "NA" else 0,
                    "year": "2016",
                },
                "ukrainian": {
                    "number":float(data[1035]) if data[1035] != "NA" else 0,
                    "year": "2016",
                },
                "urdu": {
                    "number":float(data[1036]) if data[1036] != "NA" else 0,
                    "year": "2016",
                },
                "uygur": {
                    "number":float(data[1037]) if data[1037] != "NA" else 0,
                    "year": "2016",
                },
                "uzbek": {
                    "number":float(data[1038]) if data[1038] != "NA" else 0,
                    "year": "2016",
                },
                "vietnamese": {
                    "number":float(data[1039]) if data[1039] != "NA" else 0,
                    "year": "2016",
                },
                "wajarri": {
                    "number":float(data[1040]) if data[1040] != "NA" else 0,
                    "year": "2016",
                },
                "warlpiri": {
                    "number":float(data[1041]) if data[1041] != "NA" else 0,
                    "year": "2016",
                },
                "welsh": {
                    "number":float(data[1042]) if data[1042] != "NA" else 0,
                    "year": "2016",
                },
                "wergaia": {
                    "number":float(data[1043]) if data[1043] != "NA" else 0,
                    "year": "2016",
                },
                "wiradjuri": {
                    "number":float(data[1044]) if data[1044] != "NA" else 0,
                    "year": "2016",
                },
                "wu": {
                    "number":float(data[1045]) if data[1045] != "NA" else 0,
                    "year": "2016",
                },
                "xhosa": {
                    "number":float(data[1046]) if data[1046] != "NA" else 0,
                    "year": "2016",
                },
                "yankunytjatjara": {
                    "number":float(data[1047]) if data[1047] != "NA" else 0,
                    "year": "2016",
                },
                "yiddish": {
                    "number":float(data[1048]) if data[1048] != "NA" else 0,
                    "year": "2016",
                },
                "yidiny": {
                    "number":float(data[1049]) if data[1049] != "NA" else 0,
                    "year": "2016",
                },
                "yolngu-matha": {
                    "number":float(data[1050]) if data[1050] != "NA" else 0,
                    "year": "2016",
                },
                "yorta-yorta": {
                    "number":float(data[1051]) if data[1051] != "NA" else 0,
                    "year": "2016",
                },
                "yoruba": {
                    "number":float(data[1052]) if data[1052] != "NA" else 0,
                    "year": "2016",
                },
                "yumplatok-(torres-strait-creole)": {
                    "number":float(data[1053]) if data[1053] != "NA" else 0,
                    "year": "2016",
                },
                "zomi": {
                    "number":float(data[1054]) if data[1054] != "NA" else 0,
                    "year": "2016",
                },
                "zulu": {
                    "number":float(data[1055]) if data[1055] != "NA" else 0,
                    "year": "2016",
                }

            },
            "university_distances": {
                "aapoly-melbourne-campus": {"number": float(data[171]), "year": "2016"},
                "academia-international-melbourne-campus": {"number": float(data[172]), "year": "2016"},
                "acumen-institute-of-further-education-cbd-campus": {"number": float(data[173]), "year": "2016"},
                "acumen-institute-of-further-education-richmond-campus": {"number": float(data[174]), "year": "2016"},
                "agb-training-geelong-campus": {"number": float(data[175]), "year": "2016"},
                "alacc-health-college-australia": {"number": float(data[176]), "year": "2016"},
                "alfred-deakin-college-mibt-waurn-ponds-campus": {"number": float(data[177]), "year": "2016"},
                "altec-college-melbourne-campus": {"number": float(data[178]), "year": "2016"},
                "angad-australian-institute-of-technology-la-trobe-st-campus": {"number": float(data[179]), "year": "2016"},
                "aoi-institute": {"number": float(data[180]), "year": "2016"},
                "ashton-college-footscray-campus": {"number": float(data[181]), "year": "2016"},
                "ashton-college-hallam-campus": {"number": float(data[182]), "year": "2016"},
                "ashton-college-hospitality-campus": {"number": float(data[183]), "year": "2016"},
                "ashton-college-northcote-campus": {"number": float(data[184]), "year": "2016"},
                "australian-academy-of-fashion-design": {"number": float(data[185]), "year": "2016"},
                "australian-careers-education-donald-street-campus-aurora-building": {"number": float(data[186]), "year": "2016"},
                "australian-careers-education-victoria-street-campus": {"number": float(data[187]), "year": "2016"},
                "australian-catholic-univeristy-melbourne-campus": {"number": float(data[188]), "year": "2016"},
                "australian-catholic-university-ballarat-campus": {"number": float(data[189]), "year": "2016"},
                "australian-centre-of-further-education": {"number": float(data[190]), "year": "2016"},
                "australian-college-of-applied-psychology-acap-melbourne-campus": {"number": float(data[191]), "year": "2016"},
                "australian-college-of-sport-basketball-melbourne-campus": {"number": float(data[192]), "year": "2016"},
                "australian-college-of-theology": {"number": float(data[193]), "year": "2016"},
                "australian-college-of-trade-thornbury-campus": {"number": float(data[194]), "year": "2016"},
                "australian-education-academy-10-blissington-street-springvale": {"number": float(data[195]), "year": "2016"},
                "australian-institute-of-technical-training-aitt-melbourne-campus": {"number": float(data[196]), "year": "2016"},
                "australian-institute-of-trades-institute-of-hotel-management-australia": {"number": float(data[197]), "year": "2016"},
                "australian-institute-of-translation-interpretation-aiti-melbourne-campus": {"number": float(data[198]), "year": "2016"},
                "australian-it-hospitality-institute-footscray-campus": {"number": float(data[199]), "year": "2016"},
                "australian-national-airline-college": {"number": float(data[200]), "year": "2016"},
                "australian-national-college-franklin-street-campus": {"number": float(data[201]), "year": "2016"},
                "australian-national-institute-of-business-technology-anibt-melbourne-campus": {"number": float(data[202]), "year": "2016"},
                "australian-pacific-college-melbourne-campus": {"number": float(data[203]), "year": "2016"},
                "australian-study-link-institute": {"number": float(data[204]), "year": "2016"},
                "aveta-australian-vocational-education-training-academy": {"number": float(data[205]), "year": "2016"},
                "barkly-international-college-city-campus": {"number": float(data[206]), "year": "2016"},
                "barkly-international-college-north-melbourne-campus-automotive-workshop": {"number": float(data[207]), "year": "2016"},
                "baxter-institute-automotive-bakery-campus": {"number": float(data[208]), "year": "2016"},
                "baxter-institute-fabrication-campus": {"number": float(data[209]), "year": "2016"},
                "baxter-institute-hairdressing-and-beauty-campus-flinders-street": {"number": float(data[210]), "year": "2016"},
                "beaconhills-college": {"number": float(data[211]), "year": "2016"},
                "bendigo-tafe-bendigo": {"number": float(data[212]), "year": "2016"},
                "bendigo-tafe-and-kangan-institute-broadmeadows-campus": {"number": float(data[213]), "year": "2016"},
                "biba-academy-swantson-street-campus": {"number": float(data[214]), "year": "2016"},
                "box-hill-institute-city-campus": {"number": float(data[215]), "year": "2016"},
                "box-hill-institute": {"number": float(data[216]), "year": "2016"},
                "brighton-institute-of-technology": {"number": float(data[217]), "year": "2016"},
                "catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": {"number": float(data[218]), "year": "2016"},
                "central-australian-college-cac-melbourne-campus": {"number": float(data[219]), "year": "2016"},
                "central-melbourne-institute-cmi-city-campus": {"number": float(data[220]), "year": "2016"},
                "central-melbourne-institute": {"number": float(data[221]), "year": "2016"},
                "central-queensland-university-city-campus": {"number": float(data[222]), "year": "2016"},
                "charles-sturt-university-study-centres-melbourne": {"number": float(data[223]), "year": "2016"},
                "chisholm-institue-chisholm-at-331": {"number": float(data[224]), "year": "2016"},
                "chisholm-institute-bass-coast": {"number": float(data[225]), "year": "2016"},
                "chisholm-institute-cranbourne-campus": {"number": float(data[226]), "year": "2016"},
                "chisholm-institute-dandenong-campus": {"number": float(data[227]), "year": "2016"},
                "chisholm-institute-flinders-lane-campus": {"number": float(data[228]), "year": "2016"},
                "chisholm-institute-melbourne-city-campus": {"number": float(data[229]), "year": "2016"},
                "collarts-australian-college-of-the-arts": {"number": float(data[230]), "year": "2016"},
                "dalton-college": {"number": float(data[231]), "year": "2016"},
                "dance-factory": {"number": float(data[232]), "year": "2016"},
                "deakin-college-mibt-burwood-campus": {"number": float(data[233]), "year": "2016"},
                "deakin-university-geelong-waterfront-campus": {"number": float(data[234]), "year": "2016"},
                "deakin-university-warrnambool-campus": {"number": float(data[235]), "year": "2016"},
                "deakin-university-waurn-ponds-campus": {"number": float(data[236]), "year": "2016"},
                "della-international-college-city-campus": {"number": float(data[237]), "year": "2016"},
                "della-international-college-sunshine-campus": {"number": float(data[238]), "year": "2016"},
                "department-of-education-and-training-victoria": {"number": float(data[239]), "year": "2016"},
                "east-west-college-of-natural-therapies": {"number": float(data[240]), "year": "2016"},
                "education-access-australia": {"number": float(data[241]), "year": "2016"},
                "education-training-employment-australia-etea": {"number": float(data[242]), "year": "2016"},
                "elite-training-institute": {"number": float(data[243]), "year": "2016"},
                "elly-lukas-beauty-therapy-college": {"number": float(data[244]), "year": "2016"},
                "elsis-melbourne-campus": {"number": float(data[245]), "year": "2016"},
                "endeavour-college-of-natural-health-melbourne-campus": {"number": float(data[246]), "year": "2016"},
                "everest-institute-of-education": {"number": float(data[247]), "year": "2016"},
                "explore-english": {"number": float(data[248]), "year": "2016"},
                "federation-university-ballarat-campus": {"number": float(data[249]), "year": "2016"},
                "federation-university-gippsland-campus": {"number": float(data[250]), "year": "2016"},
                "federation-university-wimmera-campus": {"number": float(data[251]), "year": "2016"},
                "flinders-international-college": {"number": float(data[252]), "year": "2016"},
                "fusion-enlgish-melbourne-campus": {"number": float(data[253]), "year": "2016"},
                "global-business-college-of-australia": {"number": float(data[254]), "year": "2016"},
                "gordon-institute-of-tafe-east-geelong-campus": {"number": float(data[255]), "year": "2016"},
                "gordon-institute-of-tafe-east-geelong-elicos-campus": {"number": float(data[256]), "year": "2016"},
                "greenwich-english-college-melbourne": {"number": float(data[257]), "year": "2016"},
                "harvest-bible-college": {"number": float(data[258]), "year": "2016"},
                "hays-international-college": {"number": float(data[259]), "year": "2016"},
                "heading-out-academy": {"number": float(data[260]), "year": "2016"},
                "headmasters-advanced-academy-of-training": {"number": float(data[261]), "year": "2016"},
                "holmesglen-holmesglen-institute-chadstone-campus": {"number": float(data[262]), "year": "2016"},
                "holmesglen-holmesglen-institute-city-campus": {"number": float(data[263]), "year": "2016"},
                "holmesglen-holmesglen-institute-waverley-campus": {"number": float(data[264]), "year": "2016"},
                "holmesglen-institute-holmesglen-moorabbin-campus": {"number": float(data[265]), "year": "2016"},
                "hospitality-management-institute-of-australia": {"number": float(data[266]), "year": "2016"},
                "impact-english-college-melbourne-campus": {"number": float(data[267]), "year": "2016"},
                "imperial-college-of-technology-and-management": {"number": float(data[268]), "year": "2016"},
                "institute-of-health-and-nursing-australia": {"number": float(data[269]), "year": "2016"},
                "institute-of-tertiary-and-higher-education-australia-ithea": {"number": float(data[270]), "year": "2016"},
                "inus-australia-education-and-training": {"number": float(data[271]), "year": "2016"},
                "jmc-academy": {"number": float(data[272]), "year": "2016"},
                "job-training-institute-dandenong-campus": {"number": float(data[273]), "year": "2016"},
                "kangan-batman-institute-of-tafe-docklands": {"number": float(data[274]), "year": "2016"},
                "kangan-batman-institute-of-tafe-richmond": {"number": float(data[275]), "year": "2016"},
                "kangan-institute-moonee-ponds-campus": {"number": float(data[276]), "year": "2016"},
                "kaplan-business-school": {"number": float(data[277]), "year": "2016"},
                "la-trobe-bundoora-campus": {"number": float(data[278]), "year": "2016"},
                "la-trobe-university-albury-wodonga-campus": {"number": float(data[279]), "year": "2016"},
                "la-trobe-university-bendigo-campus": {"number": float(data[280]), "year": "2016"},
                "la-trobe-university-city-campus-collins-street-city-campus-collins-street": {"number": float(data[281]), "year": "2016"},
                "la-trobe-university-mildura-campus": {"number": float(data[282]), "year": "2016"},
                "la-trobe-university-shepparton-campus": {"number": float(data[283]), "year": "2016"},
                "latrobe-college-of-art-and-design": {"number": float(data[284]), "year": "2016"},
                "lawson-college-australia": {"number": float(data[285]), "year": "2016"},
                "lonsdale-institute-eurocentres-melbourne": {"number": float(data[286]), "year": "2016"},
                "marcus-oldham-college": {"number": float(data[287]), "year": "2016"},
                "megt-institute-melbourne-campus": {"number": float(data[288]), "year": "2016"},
                "melbourne-college-of-hair-and-beauty": {"number": float(data[289]), "year": "2016"},
                "melbourne-flight-training": {"number": float(data[290]), "year": "2016"},
                "melbourne-institute-of-technology-federation-university-melbourne-campus": {"number": float(data[291]), "year": "2016"},
                "melbourne-polytechnic-brunswick-campus": {"number": float(data[292]), "year": "2016"},
                "melbourne-polytechnic-epping-campus": {"number": float(data[293]), "year": "2016"},
                "melbourne-polytechnic-fairfield-campus": {"number": float(data[294]), "year": "2016"},
                "melbourne-polytechnic-heidelberg-campus": {"number": float(data[295]), "year": "2016"},
                "melbourne-polytechnic-preston-campus": {"number": float(data[296]), "year": "2016"},
                "melbourne-polytechnic-preston-tafe-campus": {"number": float(data[297]), "year": "2016"},
                "melbourne-rudolf-steiner-seminar": {"number": float(data[298]), "year": "2016"},
                "melbourne-school-of-theology": {"number": float(data[299]), "year": "2016"},
                "melbourne-university-hawthorn-english-language-centre": {"number": float(data[300]), "year": "2016"},
                "melbourne-university-trinity-college": {"number": float(data[301]), "year": "2016"},
                "menzies-institute-of-technology-adderley-campus": {"number": float(data[302]), "year": "2016"},
                "menzies-institute-of-technology-batman-campus": {"number": float(data[303]), "year": "2016"},
                "menzies-institute-of-technology-spencer-campus": {"number": float(data[304]), "year": "2016"},
                "monash-college-monash-university-english-language-centre": {"number": float(data[305]), "year": "2016"},
                "federation-university-berwick-campus": {"number": float(data[306]), "year": "2016"},
                "monash-international-peninsula-campus": {"number": float(data[307]), "year": "2016"},
                "monash-university-caulfield-campus": {"number": float(data[308]), "year": "2016"},
                "monash-university-city-campus": {"number": float(data[309]), "year": "2016"},
                "monash-university-clayton-campus": {"number": float(data[310]), "year": "2016"},
                "monash-university-parkville-campus-manning-building": {"number": float(data[311]), "year": "2016"},
                "monash-university-english-language-centre-monash-college-city-campus": {"number": float(data[312]), "year": "2016"},
                "moorabbin-flying-services": {"number": float(data[313]), "year": "2016"},
                "national-theatre-drama-ballet-school": {"number": float(data[314]), "year": "2016"},
                "navitas-college-of-public-safety-ncps": {"number": float(data[315]), "year": "2016"},
                "north-melbourne-college": {"number": float(data[316]), "year": "2016"},
                "nova-institute-of-technology": {"number": float(data[317]), "year": "2016"},
                "oceania-polytechnic-institute-of-education-opie": {"number": float(data[318]), "year": "2016"},
                "orange-international-college": {"number": float(data[319]), "year": "2016"},
                "ozford-college-of-busines": {"number": float(data[320]), "year": "2016"},
                "ozford-college-of-business": {"number": float(data[321]), "year": "2016"},
                "ozford-college": {"number": float(data[322]), "year": "2016"},
                "pax-institute-of-education": {"number": float(data[323]), "year": "2016"},
                "pearson-aviation-essendon-airport": {"number": float(data[324]), "year": "2016"},
                "photography-studies-college-psc-melbourne-campus": {"number": float(data[325]), "year": "2016"},
                "pilgrim-theological-college": {"number": float(data[326]), "year": "2016"},
                "planetshakers-college": {"number": float(data[327]), "year": "2016"},
                "presbyterian-theological-college-box-hill-campus": {"number": float(data[328]), "year": "2016"},
                "rabbinical-college-of-australia-and-n-z": {"number": float(data[329]), "year": "2016"},
                "rc-rhodes-college": {"number": float(data[330]), "year": "2016"},
                "reformed-theological-college-geelong-campus": {"number": float(data[331]), "year": "2016"},
                "ridley-college-parkville-campus": {"number": float(data[332]), "year": "2016"},
                "rmit-english-worldwide": {"number": float(data[333]), "year": "2016"},
                "rmit-univeristy-brunswick-campus": {"number": float(data[334]), "year": "2016"},
                "rmit-university-rmit-city-campus": {"number": float(data[335]), "year": "2016"},
                "rmit-university-bundoora-campus": {"number": float(data[336]), "year": "2016"},
                "rmit-university-point-cook-campus": {"number": float(data[337]), "year": "2016"},
                "royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": {"number": float(data[338]), "year": "2016"},
                "royal-gurkhas-institute-of-technology-australia-rgit": {"number": float(data[339]), "year": "2016"},
                "royal-victorian-aero-club": {"number": float(data[340]), "year": "2016"},
                "sae-institute-qantm-college-melbourne-campus": {"number": float(data[341]), "year": "2016"},
                "school-for-f-m-alexander-studies": {"number": float(data[342]), "year": "2016"},
                "south-australian-college-of-english-sace-melbourne-college-of-english": {"number": float(data[343]), "year": "2016"},
                "south-pacific-institute-spi-melbourne-campus": {"number": float(data[344]), "year": "2016"},
                "southern-cross-education-institute-scei-second-campus": {"number": float(data[345]), "year": "2016"},
                "southern-cross-education-institute-scei-third-campus": {"number": float(data[346]), "year": "2016"},
                "southern-school-of-natural-therapies": {"number": float(data[347]), "year": "2016"},
                "st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": {"number": float(data[348]), "year": "2016"},
                "st-peter-institute-bourke-street-campus": {"number": float(data[349]), "year": "2016"},
                "st-peter-institute-little-collins-campus": {"number": float(data[350]), "year": "2016"},
                "stott-s-colleges-front-cooking-school-carlton-campus-vet": {"number": float(data[351]), "year": "2016"},
                "stott-s-colleges-box-hill-campus": {"number": float(data[352]), "year": "2016"},
                "stott-s-colleges-melbourne-campus": {"number": float(data[353]), "year": "2016"},
                "strathfield-college-melbourne-campus": {"number": float(data[354]), "year": "2016"},
                "sunraysia-institute-of-tafe-mildura-campus": {"number": float(data[355]), "year": "2016"},
                "sunshine-college-of-management": {"number": float(data[356]), "year": "2016"},
                "swinburne-university-of-technology-croydon-campus": {"number": float(data[357]), "year": "2016"},
                "swinburne-university-of-technology-wantirna-campus": {"number": float(data[358]), "year": "2016"},
                "swinburne-university-of-technology-hawthorn-campus": {"number": float(data[359]), "year": "2016"},
                "technical-education-development-institute": {"number": float(data[360]), "year": "2016"},
                "technical-institute-of-victoria": {"number": float(data[361]), "year": "2016"},
                "the-university-of-melbourne-southbank-campus": {"number": float(data[362]), "year": "2016"},
                "the-academy-of-interactive-entertainment-melbourne-campus": {"number": float(data[363]), "year": "2016"},
                "the-australian-ballet-school": {"number": float(data[364]), "year": "2016"},
                "the-australian-conservatoire-of-ballet-melbourne-campus": {"number": float(data[365]), "year": "2016"},
                "the-university-of-melbourne-burnley-campus": {"number": float(data[366]), "year": "2016"},
                "the-university-of-melbourne": {"number": float(data[367]), "year": "2016"},
                "the-university-of-melbourne-werribee-campus": {"number": float(data[368]), "year": "2016"},
                "tmg-college": {"number": float(data[369]), "year": "2016"},
                "torrens-university-fitzroy-campus": {"number": float(data[370]), "year": "2016"},
                "torrens-university-flinders-st-campus": {"number": float(data[371]), "year": "2016"},
                "trinity-college-theological-school": {"number": float(data[372]), "year": "2016"},
                "turner-english-box-hill-campus": {"number": float(data[373]), "year": "2016"},
                "turner-english-camberwell-campus": {"number": float(data[374]), "year": "2016"},
                "turner-english-dandenong-campus": {"number": float(data[375]), "year": "2016"},
                "turner-english-melbourne-cbd-campus": {"number": float(data[376]), "year": "2016"},
                "univeristy-of-divinity-whitley-college": {"number": float(data[377]), "year": "2016"},
                "universal-institute-of-technology": {"number": float(data[378]), "year": "2016"},
                "university-of-canberra-uc-melbourne-chadstone-campus": {"number": float(data[379]), "year": "2016"},
                "university-of-divinity-stirling-college": {"number": float(data[380]), "year": "2016"},
                "university-of-divinity-yarra-theological-union": {"number": float(data[381]), "year": "2016"},
                "victoria-university-city-flinders-lane": {"number": float(data[382]), "year": "2016"},
                "victoria-university-city-flinders": {"number": float(data[383]), "year": "2016"},
                "victoria-university-city-queen": {"number": float(data[384]), "year": "2016"},
                "victoria-university-footscray-nicholson": {"number": float(data[385]), "year": "2016"},
                "victoria-university-footscray-park": {"number": float(data[386]), "year": "2016"},
                "victoria-university-st-albans": {"number": float(data[387]), "year": "2016"},
                "victoria-university-sunshine": {"number": float(data[388]), "year": "2016"},
                "victoria-university-werribee": {"number": float(data[389]), "year": "2016"},
                "victoria-university-city-king": {"number": float(data[390]), "year": "2016"},
                "victorian-academy-of-commerce-and-technology-startups-vacts": {"number": float(data[391]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-main-campus-spotswood": {"number": float(data[392]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": {"number": float(data[393]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": {"number": float(data[394]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": {"number": float(data[395]), "year": "2016"},
                "vit-victorian-institute-of-technology-abbotsford-campus": {"number": float(data[396]), "year": "2016"},
                "vit-victorian-institute-of-technology-melbourne-cbd-campus": {"number": float(data[397]), "year": "2016"},
                "whitehouse-institute-of-design-australia": {"number": float(data[398]), "year": "2016"},
                "william-angliss-institute": {"number": float(data[399]), "year": "2016"},
                "yorke-institute": {"number": float(data[400]), "year": "2016"}
            },
            "language": {
                "acholi": float(data[28]),
                "african-languages-nec": float(data[29]),
                "african-languages-nfd": float(data[30]),
                "afrikaans": float(data[31]),
                "akan": float(data[32]),
                "albanian": float(data[33]),
                "amharic": float(data[34]),
                "anuak": float(data[35]),
                "arabic": float(data[36]),
                "armenian": float(data[37]),
                "assyrian-neo-aramaic": float(data[38]),
                "bengali": float(data[39]),
                "bisaya": float(data[40]),
                "bosnian": float(data[41]),
                "bulgarian": float(data[42]),
                "burmese": float(data[43]),
                "burmese-and-related-languages-nec": float(data[44]),
                "burmese-and-related-languages-nfd": float(data[45]),
                "cantonese": float(data[46]),
                "catalan": float(data[47]),
                "cebuano": float(data[48]),
                "chaldean-neo-aramaic": float(data[49]),
                "chin-haka": float(data[50]),
                "chinese-nfd": float(data[51]),
                "creole-nfd": float(data[52]),
                "croatian": float(data[53]),
                "czech": float(data[54]),
                "danish": float(data[55]),
                "dari": float(data[56]),
                "dhivehi": float(data[57]),
                "dinka": float(data[58]),
                "dravidian-nec": float(data[59]),
                "dutch": float(data[60]),
                "english": float(data[61]),
                "estonian": float(data[62]),
                "fijian": float(data[63]),
                "filipino": float(data[64]),
                "finnish": float(data[65]),
                "french": float(data[66]),
                "french-creole-nfd": float(data[67]),
                "german": float(data[68]),
                "greek": float(data[69]),
                "gujarati": float(data[70]),
                "hakka": float(data[71]),
                "harari": float(data[72]),
                "hausa": float(data[73]),
                "hazaraghi": float(data[74]),
                "hebrew": float(data[75]),
                "hindi": float(data[76]),
                "hungarian": float(data[77]),
                "iban": float(data[78]),
                "igbo": float(data[79]),
                "ilonggo-hiligaynon-": float(data[80]),
                "inadequately-described": float(data[81]),
                "indonesian": float(data[82]),
                "iranic-nfd": float(data[83]),
                "italian": float(data[84]),
                "japanese": float(data[85]),
                "kannada": float(data[86]),
                "karen": float(data[87]),
                "khmer": float(data[88]),
                "kinyarwanda-rwanda-": float(data[89]),
                "kirundi-rundi-": float(data[90]),
                "konkani": float(data[91]),
                "korean": float(data[92]),
                "kurdish": float(data[93]),
                "lao": float(data[94]),
                "lithuanian": float(data[95]),
                "loma-lorma-": float(data[96]),
                "luganda": float(data[97]),
                "macedonian": float(data[98]),
                "malay": float(data[99]),
                "malayalam": float(data[100]),
                "maltese": float(data[101]),
                "mandarin": float(data[102]),
                "maori-cook-island-": float(data[103]),
                "maori-new-zealand-": float(data[104]),
                "marathi": float(data[105]),
                "mauritian-creole": float(data[106]),
                "min-nan": float(data[107]),
                "mongolian": float(data[108]),
                "nepali": float(data[109]),
                "norwegian": float(data[110]),
                "not-stated": float(data[111]),
                "nuer": float(data[112]),
                "nyanja-chichewa-": float(data[113]),
                "oriya": float(data[114]),
                "oromo": float(data[115]),
                "other-southern-asian-languages": float(data[116]),
                "pashto": float(data[117]),
                "persian-excluding-dari-": float(data[118]),
                "pidgin-nfd": float(data[119]),
                "polish": float(data[120]),
                "portuguese": float(data[121]),
                "punjabi": float(data[122]),
                "rohingya": float(data[123]),
                "romanian": float(data[124]),
                "russian": float(data[125]),
                "samoan": float(data[126]),
                "serbian": float(data[127]),
                "shilluk": float(data[128]),
                "shona": float(data[129]),
                "sindhi": float(data[130]),
                "sinhalese": float(data[131]),
                "slovak": float(data[132]),
                "slovene": float(data[133]),
                "somali": float(data[134]),
                "southern-asian-languages-nfd": float(data[135]),
                "spanish": float(data[136]),
                "swahili": float(data[137]),
                "swedish": float(data[138]),
                "tagalog": float(data[139]),
                "tamil": float(data[140]),
                "telugu": float(data[141]),
                "tetum": float(data[142]),
                "thai": float(data[143]),
                "tibetan": float(data[144]),
                "tigrinya": float(data[145]),
                "tok-pisin-neomelanesian-": float(data[146]),
                "tongan": float(data[147]),
                "tswana": float(data[148]),
                "turkish": float(data[149]),
                "tuvaluan": float(data[150]),
                "ukrainian": float(data[151]),
                "urdu": float(data[152]),
                "vietnamese": float(data[153]),
                "wu": float(data[154]),
                "yoruba": float(data[155]),
                "zomi": float(data[156]),
            },
            "universities": {
                "aapoly-melbourne-campus": {"number": float(data[402]), "year": "2016"},
                "academia-international-melbourne-campus": {"number": float(data[403]), "year": "2016"},
                "acumen-institute-of-further-education-cbd-campus": {"number": float(data[404]), "year": "2016"},
                "acumen-institute-of-further-education-richmond-campus": {"number": float(data[405]), "year": "2016"},
                "agb-training-geelong-campus": {"number": float(data[406]), "year": "2016"},
                "alacc-health-college-australia": {"number": float(data[407]), "year": "2016"},
                "alfred-deakin-college-mibt-waurn-ponds-campus": {"number": float(data[408]), "year": "2016"},
                "altec-college-melbourne-campus": {"number": float(data[409]), "year": "2016"},
                "angad-australian-institute-of-technology-la-trobe-st-campus": {"number": float(data[410]), "year": "2016"},
                "aoi-institute": {"number": float(data[411]), "year": "2016"},
                "ashton-college-footscray-campus": {"number": float(data[412]), "year": "2016"},
                "ashton-college-hallam-campus": {"number": float(data[413]), "year": "2016"},
                "ashton-college-hospitality-campus": {"number": float(data[414]), "year": "2016"},
                "ashton-college-northcote-campus": {"number": float(data[415]), "year": "2016"},
                "australian-academy-of-fashion-design": {"number": float(data[416]), "year": "2016"},
                "australian-careers-education-donald-street-campus-aurora-building": {"number": float(data[417]), "year": "2016"},
                "australian-careers-education-victoria-street-campus": {"number": float(data[418]), "year": "2016"},
                "australian-catholic-univeristy-melbourne-campus": {"number": float(data[419]), "year": "2016"},
                "australian-catholic-university-ballarat-campus": {"number": float(data[420]), "year": "2016"},
                "australian-centre-of-further-education": {"number": float(data[421]), "year": "2016"},
                "australian-college-of-applied-psychology-acap-melbourne-campus": {"number": float(data[422]), "year": "2016"},
                "australian-college-of-sport-basketball-melbourne-campus": {"number": float(data[423]), "year": "2016"},
                "australian-college-of-theology": {"number": float(data[424]), "year": "2016"},
                "australian-college-of-trade-thornbury-campus": {"number": float(data[425]), "year": "2016"},
                "australian-education-academy-10-blissington-street-springvale": {"number": float(data[426]), "year": "2016"},
                "australian-institute-of-technical-training-aitt-melbourne-campus": {"number": float(data[427]), "year": "2016"},
                "australian-institute-of-trades-institute-of-hotel-management-australia": {"number": float(data[428]), "year": "2016"},
                "australian-institute-of-translation-interpretation-aiti-melbourne-campus": {"number": float(data[429]), "year": "2016"},
                "australian-it-hospitality-institute-footscray-campus": {"number": float(data[430]), "year": "2016"},
                "australian-national-airline-college": {"number": float(data[431]), "year": "2016"},
                "australian-national-college-franklin-street-campus": {"number": float(data[432]), "year": "2016"},
                "australian-national-institute-of-business-technology-anibt-melbourne-campus": {"number": float(data[433]), "year": "2016"},
                "australian-pacific-college-melbourne-campus": {"number": float(data[434]), "year": "2016"},
                "australian-study-link-institute": {"number": float(data[435]), "year": "2016"},
                "aveta-australian-vocational-education-training-academy": {"number": float(data[436]), "year": "2016"},
                "barkly-international-college-city-campus": {"number": float(data[437]), "year": "2016"},
                "barkly-international-college-north-melbourne-campus-automotive-workshop": {"number": float(data[438]), "year": "2016"},
                "baxter-institute-automotive-bakery-campus": {"number": float(data[439]), "year": "2016"},
                "baxter-institute-fabrication-campus": {"number": float(data[440]), "year": "2016"},
                "baxter-institute-hairdressing-and-beauty-campus-flinders-street": {"number": float(data[441]), "year": "2016"},
                "beaconhills-college": {"number": float(data[442]), "year": "2016"},
                "bendigo-tafe-bendigo": {"number": float(data[443]), "year": "2016"},
                "bendigo-tafe-and-kangan-institute-broadmeadows-campus": {"number": float(data[444]), "year": "2016"},
                "biba-academy-swantson-street-campus": {"number": float(data[445]), "year": "2016"},
                "box-hill-institute-city-campus": {"number": float(data[446]), "year": "2016"},
                "box-hill-institute": {"number": float(data[447]), "year": "2016"},
                "brighton-institute-of-technology": {"number": float(data[448]), "year": "2016"},
                "catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": {"number": float(data[449]), "year": "2016"},
                "central-australian-college-cac-melbourne-campus": {"number": float(data[450]), "year": "2016"},
                "central-melbourne-institute-cmi-city-campus": {"number": float(data[451]), "year": "2016"},
                "central-melbourne-institute": {"number": float(data[452]), "year": "2016"},
                "central-queensland-university-city-campus": {"number": float(data[453]), "year": "2016"},
                "charles-sturt-university-study-centres-melbourne": {"number": float(data[454]), "year": "2016"},
                "chisholm-institue-chisholm-at-331": {"number": float(data[455]), "year": "2016"},
                "chisholm-institute-bass-coast": {"number": float(data[456]), "year": "2016"},
                "chisholm-institute-cranbourne-campus": {"number": float(data[457]), "year": "2016"},
                "chisholm-institute-dandenong-campus": {"number": float(data[458]), "year": "2016"},
                "chisholm-institute-flinders-lane-campus": {"number": float(data[459]), "year": "2016"},
                "chisholm-institute-melbourne-city-campus": {"number": float(data[460]), "year": "2016"},
                "collarts-australian-college-of-the-arts": {"number": float(data[461]), "year": "2016"},
                "dalton-college": {"number": float(data[462]), "year": "2016"},
                "dance-factory": {"number": float(data[463]), "year": "2016"},
                "deakin-college-mibt-burwood-campus": {"number": float(data[464]), "year": "2016"},
                "deakin-university-geelong-waterfront-campus": {"number": float(data[465]), "year": "2016"},
                "deakin-university-warrnambool-campus": {"number": float(data[466]), "year": "2016"},
                "deakin-university-waurn-ponds-campus": {"number": float(data[467]), "year": "2016"},
                "della-international-college-city-campus": {"number": float(data[468]), "year": "2016"},
                "della-international-college-sunshine-campus": {"number": float(data[469]), "year": "2016"},
                "department-of-education-and-training-victoria": {"number": float(data[470]), "year": "2016"},
                "east-west-college-of-natural-therapies": {"number": float(data[471]), "year": "2016"},
                "education-access-australia": {"number": float(data[472]), "year": "2016"},
                "education-training-employment-australia-etea": {"number": float(data[473]), "year": "2016"},
                "elite-training-institute": {"number": float(data[474]), "year": "2016"},
                "elly-lukas-beauty-therapy-college": {"number": float(data[475]), "year": "2016"},
                "elsis-melbourne-campus": {"number": float(data[476]), "year": "2016"},
                "endeavour-college-of-natural-health-melbourne-campus": {"number": float(data[477]), "year": "2016"},
                "everest-institute-of-education": {"number": float(data[478]), "year": "2016"},
                "explore-english": {"number": float(data[479]), "year": "2016"},
                "federation-university-ballarat-campus": {"number": float(data[480]), "year": "2016"},
                "federation-university-gippsland-campus": {"number": float(data[481]), "year": "2016"},
                "federation-university-wimmera-campus": {"number": float(data[482]), "year": "2016"},
                "flinders-international-college": {"number": float(data[483]), "year": "2016"},
                "fusion-enlgish-melbourne-campus": {"number": float(data[484]), "year": "2016"},
                "global-business-college-of-australia": {"number": float(data[485]), "year": "2016"},
                "gordon-institute-of-tafe-east-geelong-campus": {"number": float(data[486]), "year": "2016"},
                "gordon-institute-of-tafe-east-geelong-elicos-campus": {"number": float(data[487]), "year": "2016"},
                "greenwich-english-college-melbourne": {"number": float(data[488]), "year": "2016"},
                "harvest-bible-college": {"number": float(data[489]), "year": "2016"},
                "hays-international-college": {"number": float(data[490]), "year": "2016"},
                "heading-out-academy": {"number": float(data[491]), "year": "2016"},
                "headmasters-advanced-academy-of-training": {"number": float(data[492]), "year": "2016"},
                "holmesglen-holmesglen-institute-chadstone-campus": {"number": float(data[493]), "year": "2016"},
                "holmesglen-holmesglen-institute-city-campus": {"number": float(data[494]), "year": "2016"},
                "holmesglen-holmesglen-institute-waverley-campus": {"number": float(data[495]), "year": "2016"},
                "holmesglen-institute-holmesglen-moorabbin-campus": {"number": float(data[496]), "year": "2016"},
                "hospitality-management-institute-of-australia": {"number": float(data[497]), "year": "2016"},
                "impact-english-college-melbourne-campus": {"number": float(data[498]), "year": "2016"},
                "imperial-college-of-technology-and-management": {"number": float(data[499]), "year": "2016"},
                "institute-of-health-and-nursing-australia": {"number": float(data[500]), "year": "2016"},
                "institute-of-tertiary-and-higher-education-australia-ithea": {"number": float(data[501]), "year": "2016"},
                "inus-australia-education-and-training": {"number": float(data[502]), "year": "2016"},
                "jmc-academy": {"number": float(data[503]), "year": "2016"},
                "job-training-institute-dandenong-campus": {"number": float(data[504]), "year": "2016"},
                "kangan-batman-institute-of-tafe-docklands": {"number": float(data[505]), "year": "2016"},
                "kangan-batman-institute-of-tafe-richmond": {"number": float(data[506]), "year": "2016"},
                "kangan-institute-moonee-ponds-campus": {"number": float(data[507]), "year": "2016"},
                "kaplan-business-school": {"number": float(data[508]), "year": "2016"},
                "la-trobe-bundoora-campus": {"number": float(data[509]), "year": "2016"},
                "la-trobe-university-albury-wodonga-campus": {"number": float(data[510]), "year": "2016"},
                "la-trobe-university-bendigo-campus": {"number": float(data[511]), "year": "2016"},
                "la-trobe-university-city-campus-collins-street-city-campus-collins-street": {"number": float(data[512]), "year": "2016"},
                "la-trobe-university-mildura-campus": {"number": float(data[513]), "year": "2016"},
                "la-trobe-university-shepparton-campus": {"number": float(data[514]), "year": "2016"},
                "latrobe-college-of-art-and-design": {"number": float(data[515]), "year": "2016"},
                "lawson-college-australia": {"number": float(data[516]), "year": "2016"},
                "lonsdale-institute-eurocentres-melbourne": {"number": float(data[517]), "year": "2016"},
                "marcus-oldham-college": {"number": float(data[518]), "year": "2016"},
                "megt-institute-melbourne-campus": {"number": float(data[519]), "year": "2016"},
                "melbourne-college-of-hair-and-beauty": {"number": float(data[520]), "year": "2016"},
                "melbourne-flight-training": {"number": float(data[521]), "year": "2016"},
                "melbourne-institute-of-technology-federation-university-melbourne-campus": {"number": float(data[522]), "year": "2016"},
                "melbourne-polytechnic-brunswick-campus": {"number": float(data[523]), "year": "2016"},
                "melbourne-polytechnic-epping-campus": {"number": float(data[524]), "year": "2016"},
                "melbourne-polytechnic-fairfield-campus": {"number": float(data[525]), "year": "2016"},
                "melbourne-polytechnic-heidelberg-campus": {"number": float(data[526]), "year": "2016"},
                "melbourne-polytechnic-preston-campus": {"number": float(data[527]), "year": "2016"},
                "melbourne-polytechnic-preston-tafe-campus": {"number": float(data[528]), "year": "2016"},
                "melbourne-rudolf-steiner-seminar": {"number": float(data[529]), "year": "2016"},
                "melbourne-school-of-theology": {"number": float(data[530]), "year": "2016"},
                "melbourne-university-hawthorn-english-language-centre": {"number": float(data[531]), "year": "2016"},
                "melbourne-university-trinity-college": {"number": float(data[532]), "year": "2016"},
                "menzies-institute-of-technology-adderley-campus": {"number": float(data[533]), "year": "2016"},
                "menzies-institute-of-technology-batman-campus": {"number": float(data[534]), "year": "2016"},
                "menzies-institute-of-technology-spencer-campus": {"number": float(data[535]), "year": "2016"},
                "monash-college-monash-university-english-language-centre": {"number": float(data[536]), "year": "2016"},
                "federation-university-berwick-campus": {"number": float(data[537]), "year": "2016"},
                "monash-international-peninsula-campus": {"number": float(data[538]), "year": "2016"},
                "monash-university-caulfield-campus": {"number": float(data[539]), "year": "2016"},
                "monash-university-city-campus": {"number": float(data[540]), "year": "2016"},
                "monash-university-clayton-campus": {"number": float(data[541]), "year": "2016"},
                "monash-university-parkville-campus-manning-building": {"number": float(data[542]), "year": "2016"},
                "monash-university-english-language-centre-monash-college-city-campus": {"number": float(data[543]), "year": "2016"},
                "moorabbin-flying-services": {"number": float(data[544]), "year": "2016"},
                "national-theatre-drama-ballet-school": {"number": float(data[545]), "year": "2016"},
                "navitas-college-of-public-safety-ncps": {"number": float(data[546]), "year": "2016"},
                "north-melbourne-college": {"number": float(data[547]), "year": "2016"},
                "nova-institute-of-technology": {"number": float(data[548]), "year": "2016"},
                "oceania-polytechnic-institute-of-education-opie": {"number": float(data[549]), "year": "2016"},
                "orange-international-college": {"number": float(data[550]), "year": "2016"},
                "ozford-college-of-busines": {"number": float(data[551]), "year": "2016"},
                "ozford-college-of-business": {"number": float(data[552]), "year": "2016"},
                "ozford-college": {"number": float(data[553]), "year": "2016"},
                "pax-institute-of-education": {"number": float(data[554]), "year": "2016"},
                "pearson-aviation-essendon-airport": {"number": float(data[555]), "year": "2016"},
                "photography-studies-college-psc-melbourne-campus": {"number": float(data[556]), "year": "2016"},
                "pilgrim-theological-college": {"number": float(data[557]), "year": "2016"},
                "planetshakers-college": {"number": float(data[558]), "year": "2016"},
                "presbyterian-theological-college-box-hill-campus": {"number": float(data[559]), "year": "2016"},
                "rabbinical-college-of-australia-and-n-z": {"number": float(data[560]), "year": "2016"},
                "rc-rhodes-college": {"number": float(data[561]), "year": "2016"},
                "reformed-theological-college-geelong-campus": {"number": float(data[562]), "year": "2016"},
                "ridley-college-parkville-campus": {"number": float(data[563]), "year": "2016"},
                "rmit-english-worldwide": {"number": float(data[564]), "year": "2016"},
                "rmit-univeristy-brunswick-campus": {"number": float(data[565]), "year": "2016"},
                "rmit-university-rmit-city-campus": {"number": float(data[566]), "year": "2016"},
                "rmit-university-bundoora-campus": {"number": float(data[567]), "year": "2016"},
                "rmit-university-point-cook-campus": {"number": float(data[568]), "year": "2016"},
                "royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": {"number": float(data[569]), "year": "2016"},
                "royal-gurkhas-institute-of-technology-australia-rgit": {"number": float(data[570]), "year": "2016"},
                "royal-victorian-aero-club": {"number": float(data[571]), "year": "2016"},
                "sae-institute-qantm-college-melbourne-campus": {"number": float(data[572]), "year": "2016"},
                "school-for-f-m-alexander-studies": {"number": float(data[573]), "year": "2016"},
                "south-australian-college-of-english-sace-melbourne-college-of-english": {"number": float(data[574]), "year": "2016"},
                "south-pacific-institute-spi-melbourne-campus": {"number": float(data[575]), "year": "2016"},
                "southern-cross-education-institute-scei-second-campus": {"number": float(data[576]), "year": "2016"},
                "southern-cross-education-institute-scei-third-campus": {"number": float(data[577]), "year": "2016"},
                "southern-school-of-natural-therapies": {"number": float(data[578]), "year": "2016"},
                "st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": {"number": float(data[579]), "year": "2016"},
                "st-peter-institute-bourke-street-campus": {"number": float(data[580]), "year": "2016"},
                "st-peter-institute-little-collins-campus": {"number": float(data[581]), "year": "2016"},
                "stott-s-colleges-front-cooking-school-carlton-campus-vet": {"number": float(data[582]), "year": "2016"},
                "stott-s-colleges-box-hill-campus": {"number": float(data[583]), "year": "2016"},
                "stott-s-colleges-melbourne-campus": {"number": float(data[584]), "year": "2016"},
                "strathfield-college-melbourne-campus": {"number": float(data[585]), "year": "2016"},
                "sunraysia-institute-of-tafe-mildura-campus": {"number": float(data[586]), "year": "2016"},
                "sunshine-college-of-management": {"number": float(data[587]), "year": "2016"},
                "swinburne-university-of-technology-croydon-campus": {"number": float(data[588]), "year": "2016"},
                "swinburne-university-of-technology-wantirna-campus": {"number": float(data[589]), "year": "2016"},
                "swinburne-university-of-technology-hawthorn-campus": {"number": float(data[590]), "year": "2016"},
                "technical-education-development-institute": {"number": float(data[591]), "year": "2016"},
                "technical-institute-of-victoria": {"number": float(data[592]), "year": "2016"},
                "the-university-of-melbourne-southbank-campus": {"number": float(data[593]), "year": "2016"},
                "the-academy-of-interactive-entertainment-melbourne-campus": {"number": float(data[594]), "year": "2016"},
                "the-australian-ballet-school": {"number": float(data[595]), "year": "2016"},
                "the-australian-conservatoire-of-ballet-melbourne-campus": {"number": float(data[596]), "year": "2016"},
                "the-university-of-melbourne-burnley-campus": {"number": float(data[597]), "year": "2016"},
                "the-university-of-melbourne": {"number": float(data[598]), "year": "2016"},
                "the-university-of-melbourne-werribee-campus": {"number": float(data[599]), "year": "2016"},
                "tmg-college": {"number": float(data[600]), "year": "2016"},
                "torrens-university-fitzroy-campus": {"number": float(data[601]), "year": "2016"},
                "torrens-university-flinders-st-campus": {"number": float(data[602]), "year": "2016"},
                "trinity-college-theological-school": {"number": float(data[603]), "year": "2016"},
                "turner-english-box-hill-campus": {"number": float(data[604]), "year": "2016"},
                "turner-english-camberwell-campus": {"number": float(data[605]), "year": "2016"},
                "turner-english-dandenong-campus": {"number": float(data[606]), "year": "2016"},
                "turner-english-melbourne-cbd-campus": {"number": float(data[607]), "year": "2016"},
                "univeristy-of-divinity-whitley-college": {"number": float(data[608]), "year": "2016"},
                "universal-institute-of-technology": {"number": float(data[609]), "year": "2016"},
                "university-of-canberra-uc-melbourne-chadstone-campus": {"number": float(data[610]), "year": "2016"},
                "university-of-divinity-stirling-college": {"number": float(data[611]), "year": "2016"},
                "university-of-divinity-yarra-theological-union": {"number": float(data[612]), "year": "2016"},
                "victoria-university-city-flinders-lane": {"number": float(data[613]), "year": "2016"},
                "victoria-university-city-flinders": {"number": float(data[614]), "year": "2016"},
                "victoria-university-city-queen": {"number": float(data[615]), "year": "2016"},
                "victoria-university-footscray-nicholson": {"number": float(data[616]), "year": "2016"},
                "victoria-university-footscray-park": {"number": float(data[617]), "year": "2016"},
                "victoria-university-st-albans": {"number": float(data[618]), "year": "2016"},
                "victoria-university-sunshine": {"number": float(data[619]), "year": "2016"},
                "victoria-university-werribee": {"number": float(data[620]), "year": "2016"},
                "victoria-university-city-king": {"number": float(data[621]), "year": "2016"},
                "victorian-academy-of-commerce-and-technology-startups-vacts": {"number": float(data[622]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-main-campus-spotswood": {"number": float(data[623]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": {"number": float(data[624]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": {"number": float(data[625]), "year": "2016"},
                "victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": {"number": float(data[626]), "year": "2016"},
                "vit-victorian-institute-of-technology-abbotsford-campus": {"number": float(data[627]), "year": "2016"},
                "vit-victorian-institute-of-technology-melbourne-cbd-campus": {"number": float(data[628]), "year": "2016"},
                "whitehouse-institute-of-design-australia": {"number": float(data[629]), "year": "2016"},
                "william-angliss-institute": {"number": float(data[630]), "year": "2016"},
                "yorke-institute": {"number": float(data[631]), "year": "2016"},
            }
}

with open('17_05_ITERATION_2_FINAL.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    # readr.next()
    readr.next()
    for line in readr:
        obj = row_to_obj(line)
        if obj['name']!="Ballarat":
            print(json.dumps(obj))
        #if(line[0]=="BROWN HILL"):
            #print line
#print line[620]