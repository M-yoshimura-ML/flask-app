from flask import Blueprint, render_template, request, flash
from blueprints.searchImage.google_search import GoogleSearch

search_image_bp = Blueprint('SearchImage', __name__, template_folder="templates")


@search_image_bp.route("/search-image", methods=['GET'])
def index():
    return render_template('searchImage/search_screen.html')


@search_image_bp.route('/search')
def search():
    query = request.args.get('query')
    language = request.args.get('language')

    # Google Images検索を実行して画像URLのリストを取得
    google_search = GoogleSearch(query, language);
    search_results = google_search.search_images(query, language)

    return render_template('searchImage/search_screen.html', query=query, language=language, search_results=search_results)



