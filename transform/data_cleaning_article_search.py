"""

Script pour clean les données : prends les .json provenant de "requete_articlesearch" en entrée et retourne des .json contenant seulement les données qui nous intéressent. 


"""
import json
import os
import glob


class ToCleanJsonArticleSearch:
    """
    Classe permettant d'instancier un objet permettant de clean un fichier .json provenant du script "request_article_search.py".
        Méthodes :
        init

        import_json : Importe le fichier .json raw à traiter dans une variable
            Arg : le chemin du fichier 

        file_name : Extrait le nom du fichier
            Arg: le chemin du fichier

        json_clean : Clean le fichier raw
            Arg : la variable contenant le json provenant de import_json

        to_clean_json : Ecrit le json clean dans un fichier .json
            Args : le json clean provenant de json_clean, le nom du fichier provenant de file_name

        from_raw_to_clean : Automatise les méthodes précedentes 
            Arg: le chemin du fichier
    """

    def __init__(self) -> None:
        pass


    def import_json(self,file_path):
        """
         Importe le fichier .json raw à traiter dans une variable
            Arg : le chemin du fichier 
        """
        with open(file_path, "r") as file:
            file_json = json.load(file)
        return file_json



    def file_name(self,file_path):
        """
          file_name : Extrait le nom du fichier
            Arg: le chemin du fichier
        """
        name = os.path.basename(file_path)
        return name

    def json_clean(self,file_json):
        """
        json_clean : Clean le fichier raw
            Arg : la variable contenant le json provenant de import_json
        """
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
        """
        to_clean_json : Ecrit le json clean dans un fichier .json
            Args : le json clean provenant de json_clean, le nom du fichier provenant de file_name
        """
        with open("data/cleaned_data/cleaned_"+file_name, "w") as f:
            json.dump(clean_json,f)



    def from_raw_to_clean(self,file):
        """
        from_raw_to_clean : Automatise les méthodes précedentes 
            Arg: le chemin du fichier
        """
        to_treat = self.import_json(file)
        name = self.file_name(file)
        to_stock = self.json_clean(to_treat)
        self.to_clean_json(to_stock, name)

# TEst
tcas = ToCleanJsonArticleSearch()
liste_test = glob.glob("data/raw_data/C*")
for i in liste_test:
    tcas.from_raw_to_clean(i)