"""

Script pour clean les données : prends les .json provenant de "requete_articlesearch" en entrée et retourne des .json contenant seulement les données qui nous intéressent. 
Ces .json clean pourront ensuite être intégrés à la BDD grâce à "script_bdd.py"

"""
import json
import os
import glob


class ToCleanJsonArticleSearch:
    """
    """
    def __init__(self) -> None:
        pass


    def import_json(self,file_path):
        with open(file_path, "r") as file:
            file_json = json.load(file)
        return file_json



    def file_name(self,file_path):
        name = os.path.basename(file_path)
        return name

    def json_clean(self,file_json):
        json_first_step = file_json["response"]["docs"]
        if json_first_step == []:
            return print("Fichier vide")
        else :
            list_articles_cleaned = []
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
                article["_id"] = i.get("_id")
                article["word_count"] = i.get("word_count")
                article["uri"] = i.get("uri")

                list_articles_cleaned.append(article)

            return list_articles_cleaned
    

    def to_clean_json(self,clean_json,file_name):
        with open("data/cleaned_data/cleaned_"+file_name, "w") as f:
            json.dump(clean_json,f)



    def from_raw_to_clean(self,file):
        to_treat = self.import_json(file)
        name = self.file_name(file)
        to_stock = self.json_clean(to_treat)
        self.to_clean_json(to_stock, name)


tcas = ToCleanJsonArticleSearch()
liste_test = glob.glob("data/raw_data/C*")
for i in liste_test:
    tcas.from_raw_to_clean(i)