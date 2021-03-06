import pandas as pd

from app import db
from sqlalchemy import create_engine, text
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class Articles(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(), nullable=False, unique=True)
    article_description = db.Column(db.String())
    article_image_path = db.Column(db.String(), nullable=False)
    link_to_article = db.Column(db.String())
    article_category = db.Column(db.String())
    article_author = db.Column(db.String())
    article_publish_date = db.Column(db.String())

    def __repr__(self):
        return f"article: '{self.article_name}', '{self.article_description}'"


class Recommendations(db.Model):
    main_article_id = db.Column(db.Integer, primary_key=True)
    recommendation_1_id = db.Column(db.Integer)
    recommendation_2_id = db.Column(db.Integer)
    recommendation_3_id = db.Column(db.Integer)
    recommendation_4_id = db.Column(db.Integer)
    recommendation_5_id = db.Column(db.Integer)

    def __repr__(self):
        return f"article: '{self.main_article_id}', recommendations: '{self.recommendation_1_id}', \
              '{self.recommendation_2_id}', '{self.recommendation_3_id}', '{self.recommendation_4_id}', \
              '{self.recommendation_5_id}'"


class Helpers():
    """
    In this class we have methods related to sql database
    """

    def select(table_name: str, columns_select: str, filter: str = None, order_columns: str = None,
               order_asc: bool = None) -> list:
        """ Method for select data from mysql table

        Args:
            table_name (str) : Name of table from where we want to select data
            columns_select (tuple): the columns we want to select
            filter (str): the condition by which we want to filter our selection
        """

        engine = create_engine(
            'sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        query = ""
        exec_res = []
        res = []
        if columns_select[0] == '*':
            query = f"SELECT * FROM {table_name}"
        else:
            query = f"SELECT {columns_select} FROM {table_name}"

        if filter is not None:
            query += f" WHERE {filter}"

        if order_columns is not None:
            query += f" ORDER BY {order_columns} "
            if order_asc == True:
                query += "asc"
            else:
                query += "desc"

        try:
            exec_res = conn.execute(text(query))
            res = [row for row in exec_res]
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return res

    def insert(table_name: str, data: dict) -> None:
        """ Method for inserting data into mysql table

        Args:
            table_name (str) : Name of table where we want to insert data
            data (dict) : Dictionary of data we need to insert
        """

        engine = create_engine(
            'sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        try:
            conn.execute(text(f"INSERT INTO {table_name} {tuple(data.keys())} VALUES {tuple(data.values())}"))
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def delete(table_name: str, condition: str) -> None:
        """ Method for delete row from mysql table

        Args:
            table_name (str) : Name of table where we want to delete row
            condition (str) : condition for delete
        """

        engine = create_engine(
            'sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        try:
            conn.execute(text(f"DELETE FROM {table_name} WHERE {condition}"))
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def update(table_name: str, update_column: str, update_id: str, update_string: str) -> None:
        """ Method for update row in mysql table

        Args:
            table_name (str) : Name of table where we want to update row
            update_id (str) : id(primary key) of the row we want to update
            data (dict) : data for update
            condition (str) : condition for update
        """

        engine = create_engine(
            'sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        try:
            conn.execute(text(f"UPDATE {table_name} SET {update_string} WHERE {update_column} = {update_id}"))
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def if_exists_update_else_insert(table_name: str, main_article_id: str, data: dict, update_column: str,
                                     update_string: str) -> None:
        """ Method for insert row into mysql table but if such id exists in table, then update it

        Args:
            main_article_id (str) : Id of article we want to insert/update
            data (str) : data to insert/update 
        """

        select_row = Helpers.select(table_name, 'main_article_id', f"main_article_id = '{main_article_id}'")

        if len(select_row) > 0:
            print(select_row)
            Helpers.update(table_name, update_column, main_article_id, update_string)
        else:
            Helpers.insert(table_name, data)

    def fill_recommendations(articles_to_fill, category: str = None) -> None:
        """ Method for fill recommendations table. 

        Args:
            filter (str) : we filter data with this parameter and filtered data will be filled
        """

        all_articles = Helpers.select('articles', 'article_id, article_name, article_description')

        if (len(all_articles) % 100 == 0):
            articles_to_fill = all_articles
        else:
            articles_to_fill = Helpers.select('articles', 'article_id, article_name', None, "article_id", False)[0:11]

        tfidf = TfidfVectorizer(stop_words='english')
        articles_df = pd.DataFrame(all_articles, columns=['article_id', 'article_name', 'article_description'])
        tfidf_matrix = tfidf.fit_transform(articles_df['article_description'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix, True)
        for elem in articles_to_fill[::-1]:
            article_id = elem[0]
            article_name = elem[1]
            recommendations = Helpers.get_recommendations(article_name, article_id, cosine_sim, articles_df)
            recommendations = list(set(list(recommendations)))[::-1]

            unique_recommendation = []
            for rec in recommendations:
                # check if exists in unique_list or not
                if rec not in unique_recommendation and rec != article_id:
                    unique_recommendation.append(rec)
            recommendations = unique_recommendation
            print(recommendations)

            data = {
                "recommendation_1_id": recommendations[0],
                "recommendation_2_id": recommendations[1],
                "recommendation_3_id": recommendations[2],
                "recommendation_4_id": recommendations[3],
                "recommendation_5_id": recommendations[4]
            }

            update_string = f"recommendation_1_id = {recommendations[0]}, recommendation_2_id = {recommendations[1]}, \
                            recommendation_3_id = {recommendations[2]}, recommendation_4_id = {recommendations[3]}, \
                            recommendation_5_id = {recommendations[4]}"

            Helpers.if_exists_update_else_insert('recommendations', article_id, data, 'main_article_id', update_string)

    def get_recommendations(title: str, idx: int, cosine_sim, data) -> list:
        """ Method that takes in article title as input and outputs most similar articles

        Args:
            title (str) : title of article for which we are searching similarities
            idx (str) : index of article for which we are searching similarities
            cosine_sim (numpy.ndarray) : array of similarities
            data (pandas dataframe) : dataframe with columns ['article_id', 'article_name', 'article_description']

        Return:
            res (list) : list of recommended article ids
        """

        sim_scores = list(enumerate(cosine_sim[idx - 1]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[0:11]
        article_indices = [i[0] for i in sim_scores]
        res = [(i + 1) for i in article_indices]

        return res
