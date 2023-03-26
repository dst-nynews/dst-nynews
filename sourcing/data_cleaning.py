"""

Script pour clean les données : prends les .json provenant de "requete_articlesearch" en entrée et retourne des .json contenant seulement les données qui nous intéressent. 
Ces .json clean pourront ensuite être intégrés à la BDD grâce à "script_bdd.py"

"""
import json


# récupération fichiers json
def import_json(file_name):
    with open(file_name, "r") as file:
        file_json = json.load(file)
    return file_json


#traitement fichier json
def json_clean(file_json):
    json_first_step = file_json["response"]["docs"]
    if json_first_step == []:
        return print("Fichier vide")
    else :
        list_articles_cleaned = []
        json_cleaned = {}
        for i in json_first_step:
            article={}
            article["abstract"] = i.get("abstract")
            article["web_url"] = i.get("web_url")
            article["snippet"] = i.get("snippet")
            article["lead_paragraph"] = i.get("lead_paragraph")
            article["print_section"] = i.get("print_section")
            article["print_page"] = i.get("print_page")
            article["headline"] = i.get("headline")
            article["keywords"] = i.get("keywords")
            article["pub_date"] = i.get("pub_date")
            article["document_type"] = i.get("document_type")
            article["news_desk"] = i.get("news_desk")
            article["section_name"] =i.get("section_name")
            article["subsection_name"] = i.get("subsection_name")
            article["id"] = i.get("_id")
            article["word_count"] = i.get("word_count")
            article["uri"] = i.get("uri")


            

            list_articles_cleaned.append(article)
        json_cleaned["articles"] = list_articles_cleaned

        return json_cleaned
    

    
def to_clean_json(clean_json,file_name,page_number):
    with open("data/raw_data/cleaned_"+file_name+ "_Page_" + str(page_number)+".json", "w") as f:
        json.dump(clean_json,f)


file1 = "data/raw_data/Covid2019-12-31_Page_0.json"
file2 = "data/raw_data/Covid2020-01-31_Page_0.json"

"""Test 1
to_clean = import_json(file1)
cleaned = json_clean(to_clean)
to_clean_json(cleaned,"test", 1)


print(cleaned)
"""

# Test 2
to_clean = import_json(file2)
cleaned = json_clean(to_clean)
to_clean_json(cleaned,"test", 2)