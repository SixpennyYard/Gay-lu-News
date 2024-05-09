from datetime import datetime

from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from data_client_management.ClientManager import ClientManager
from data_client_management.FormDataManager import FormDataManager
from data_client_management.User import User

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.static_folder = 'static'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """
    Charge une session
    :param user_id: ID de l'utilisateur
    :return:
    """
    user = User(user_id)
    return user


@app.route('/')
def accueil():
    """
    Page d'acceuil du site web
    :return:
    """
    articles = FormDataManager.read_from_csv()
    titles = [article_data for article_data in articles]
    return render_template('index.html', user=current_user, titles=titles)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Fonction de login du site web
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('accueil'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not ClientManager.is_already_registered_username(username):
            return render_template('login.html', user=current_user,
                                   error='Votre nom d\'utilisateur est incorrecte, Voulez-vous créer un compte ?')
        user = load_user(username)
        if check_password_hash(user.get_hashed_password, password):
            login_user(user)
            return redirect(url_for('accueil'))
        else:
            return render_template('login.html', user=current_user, error='Mot de passe incorrecte !')

    return render_template('login.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    """
    Fonction pour se déconnecter de son compte
    :return:
    """
    logout_user()
    return redirect(url_for('accueil'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Fonction pour se register au site web
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('accueil'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if ClientManager.is_already_registered_email(email):
            return render_template('register.html', user=current_user,
                                   error='Un compte sous cette adresse email existe déjà')
        if ClientManager.is_already_registered_username(username):
            return render_template('register.html', user=current_user,
                                   error='Ce nom d\'utilisateur existe déjà')

        hashed_password = generate_password_hash(password)
        user = User(username, email, hashed_password)
        user.save_data(username, email, hashed_password)

        login_user(user)
        return redirect(url_for('profil'))

    return render_template('register.html', user=current_user)


@app.route('/profil')
@login_required
def profil():
    """
    Page de profil d'utilisateur
    :return:
    """
    return render_template('profil.html', user=current_user)


@app.route('/formulaire', methods=['GET', 'POST'])
@login_required
def formulaire():
    """
    Fonction de gestion du formulaire de création d'un article
    :return:
    """
    if request.method == 'POST':
        title = request.form.get('title')
        summary = request.form.get('summary')
        user_article = request.form.get('user_article')
        date = datetime.now().strftime('%d/%m/%Y à %H:%M')

        if FormDataManager.add_article(title, summary, user_article, current_user._username, date):  # ici il ne
            # faudrait pas utiliser le nom d'utilisateur sinon je devrais le mettre public
            return redirect(url_for('article', title=title, header=True))
        else:
            return render_template('formulaire.html', user=current_user,
                                   error="Le titre de l'article est déjà utilisé.")

    return render_template('formulaire.html', user=current_user)


@app.route('/articles/<string:title>')
def article(title):
    """
    Page des articles
    :param title:
    :return:
    """
    header = request.args.get('header', False) == 'True'
    data = FormDataManager.read_from_csv()
    for article_data in data:
        if article_data['title'] == title:
            return render_template('articlesTemplate.html', user=current_user, title=title,
                                   user_article=article_data['user_article'], author=article_data['author'],
                                   date=article_data['date'], header=header)
    return render_template('article_not_found.html'), 404


@app.route('/article', methods=['GET', 'POST'])
def search():
    """
    Fonction gérant la recherche d'un article
    :return:
    """
    if request.method == 'POST':
        search_query = request.form.get('search')
        articles = FormDataManager.read_from_csv()
        matched_articles = []
        for article_data in articles:
            if (search_query.lower() in article_data['title'].lower()
                    or search_query.lower() in article_data['summary'].lower()):
                matched_articles.append(article_data)
        return render_template('articles.html', user=current_user, articles=matched_articles, query=search_query)
    return redirect(url_for('accueil'))


@app.route('/delete-article/<string:title>', methods=['POST'])
@login_required
def delete_article(title):
    """
    Fonction permettant de supprimer un article
    :param title:
    :return:
    """
    if current_user._username == FormDataManager.get_article_author(title):
        FormDataManager.delete_article(title)
    return redirect(url_for('accueil'))


@app.route('/modifier-article/<string:title>', methods=['GET', 'POST'])
@login_required
def modifier_article(title):
    """
    Fonction permettant de modifier un article
    :param title:
    :return:
    """
    if current_user._username != FormDataManager.get_article_author(title):
        return "Vous n'êtes pas l'auteur de cette article", 403

    if request.method == 'POST':
        new_title = request.form.get('title')
        summary = request.form.get('summary')
        user_article = request.form.get('user_article')
        date = datetime.now().strftime('%d/%m/%Y à %H:%M')

        if title != new_title and FormDataManager.article_exists(new_title):
            return render_template('edit_article.html', user=current_user, title=title,
                                   error="Le titre de l'article est déjà utilisé.")

        FormDataManager.update_article(title, new_title, summary, user_article, date)
        return redirect(url_for('article', title=new_title, header=True))

    article_data = FormDataManager.get_article_data(title)
    return render_template('edit_article.html', user=current_user, article=article_data)


if __name__ == '__main__':
    app.run(debug=True)
