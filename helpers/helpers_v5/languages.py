a=["acholi",
"african-languages-nec",
"african-languages-nfd",
"afrikaans",
"akan",
"albanian",
"amharic",
"anuak",
"arabic",
"armenian",
"assyrian-neo-aramaic",
"bengali",
"bisaya",
"bosnian",
"bulgarian",
"burmese",
"burmese-and-related-languages-nec",
"burmese-and-related-languages-nfd",
"cantonese",
"catalan",
"cebuano",
"chaldean-neo-aramaic",
"chin-haka",
"chinese-nfd",
"creole-nfd",
"croatian",
"czech",
"danish",
"dari",
"dhivehi",
"dinka",
"dravidian-nec",
"dutch",
"english",
"estonian",
"fijian",
"filipino",
"finnish",
"french",
"french-creole-nfd",
"german",
"greek",
"gujarati",
"hakka",
"harari",
"hausa",
"hazaraghi",
"hebrew",
"hindi",
"hungarian",
"iban",
"igbo",
"ilonggo-hiligaynon-",
"inadequately-described",
"indonesian",
"iranic-nfd",
"italian",
"japanese",
"kannada",
"karen",
"khmer",
"kinyarwanda-rwanda-",
"kirundi-rundi-",
"konkani",
"korean",
"kurdish",
"lao",
"lithuanian",
"loma-lorma-",
"luganda",
"macedonian",
"malay",
"malayalam",
"maltese",
"mandarin",
"maori-cook-island-",
"maori-new-zealand-",
"marathi",
"mauritian-creole",
"min-nan",
"mongolian",
"nepali",
"norwegian",
"not-stated",
"nuer",
"nyanja-chichewa-",
"oriya",
"oromo",
"other-southern-asian-languages",
"pashto",
"persian-excluding-dari-",
"pidgin-nfd",
"polish",
"portuguese",
"punjabi",
"rohingya",
"romanian",
"russian",
"samoan",
"serbian",
"shilluk",
"shona",
"sindhi",
"sinhalese",
"slovak",
"slovene",
"somali",
"southern-asian-languages-nfd",
"spanish",
"swahili",
"swedish",
"tagalog",
"tamil",
"telugu",
"tetum",
"thai",
"tibetan",
"tigrinya",
"tok-pisin-neomelanesian-",
"tongan",
"tswana",
"turkish",
"tuvaluan",
"ukrainian",
"urdu",
"vietnamese",
"wu",
"yoruba",
"zomi",
]

idx=0
for i in a:
	print '"' + i +'": int(data[' + str(idx) + ']),'
	idx+=1