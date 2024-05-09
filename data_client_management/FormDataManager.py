import csv


class FormDataManager:
    """
    Class qui gére les données des articles
    """
    @staticmethod
    def save_to_csv(data):
        """
        Sauvegarde les données dans le fichier CSV
        :param data:
        :return:
        """
        with open('data/form_data.csv', 'a', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

    @staticmethod
    def read_from_csv():
        """
        Cette fonction viens extraire les données du CSV
        :return:
        """
        form_data = []
        with open('data/form_data.csv', 'r', newline='', encoding="UTF-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                form_data.append({
                    'title': row[0],
                    'summary': row[1],
                    'user_article': row[2],
                    'author': row[3],
                    'date': row[4]
                })
        return form_data

    @staticmethod
    def article_exists(title):
        """
        Verifie si un article avec ce même titre existe déjà dans la base de donnée
        :param title:
        :return:
        """
        data = FormDataManager.read_from_csv()
        for article in data:
            if article['title'] == title:
                return True
        return False

    @staticmethod
    def add_article(title, summary, user_article, author, date):
        """S'il est possible d'ajouter l'article dans la base de donnée, cette fonction l'ajoute"""
        if FormDataManager.article_exists(title):
            return False
        else:
            FormDataManager.save_to_csv([title, summary, user_article, author, date])
            return True

    @staticmethod
    def get_article_author(title):
        """
        Donne le nom de l'auteur qui a écrit l'article nommé 'title'
        :param title:
        :return:
        """
        data = FormDataManager.read_from_csv()
        for article in data:
            if article['title'] == title:
                return article['author']
        return None

    @staticmethod
    def delete_article(title):
        """
        Supprime l'article grace à son titre
        :param title:
        :return:
        """
        data = FormDataManager.read_from_csv()
        updated_data = [article for article in data if article['title'] != title]
        with open('data/form_data.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            for article in updated_data:
                writer.writerow(
                    [article['title'], article['summary'], article['user_article'], article['author'], article['date']])

    @staticmethod
    def update_article(old_title, new_title, summary, user_article, date):
        """
        Met à jour les informations d'un article
        :param old_title:
        :param new_title:
        :param summary:
        :param user_article:
        :param date:
        :return:
        """
        data = FormDataManager.read_from_csv()
        updated_data = []
        for article in data:
            if article['title'] == old_title:
                article['title'] = new_title
                article['summary'] = summary
                article['user_article'] = user_article
                article['date'] = date
            updated_data.append(article)
        with open('data/form_data.csv', 'w', newline='', encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            for article in updated_data:
                writer.writerow([
                    article['title'],
                    article['summary'],
                    article['user_article'],
                    article['author'],
                    article['date']
                ])

    @staticmethod
    def get_article_data(title):
        """
        Récupére les données d'un article grace à son 'title'
        :param title:
        :return:
        """
        data = FormDataManager.read_from_csv()
        for article in data:
            if article['title'] == title:
                return article
        return None

