from app import db
from sqlalchemy import create_engine, text

class Articles(db.Model):
    article_id = db.Column(db.Integer, primary_key = True)
    article_name = db.Column(db.String(), nullable = False, unique = True)
    article_description = db.Column(db.String())
    article_image_path = db.Column(db.String(), nullable = False)
    link_to_article = db.Column(db.String())
    article_category = db.Column(db.String())

    def __repr__(self):
        return f"article: '{self.article_name}', '{self.article_description}'"

class Recommendations(db.Model):
    main_article_id = db.Column(db.Integer, primary_key = True)
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
    # select('articles', ('article_id, article_name'), 'article_id < 10')
    def select(table_name: str, columns_select: tuple, filter: str = None) -> list:
        """ Method for select data from mysql table

        Args:
            table_name (str) : Name of table from where we want to select data
            columns_select (tuple): the columns we want to select
            filter (str): the condition by which we want to filter our selection
        """
        engine = create_engine('sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        query = ""
        exec_res = []
        if columns_select[0] == '*':
            query = f"SELECT * FROM {table_name}"
        else:
            query = f"SELECT {columns_select} FROM {table_name}"
        if filter is not None:
            query += f" WHERE {filter}"
        try:
            exec_res = conn.execute(text(query))
        except Exception as e:
            print(e)
        res = [row for row in exec_res]
        return res

    def insert(table_name: str, data: dict) -> None:
        """ Method for inserting data into mysql table

        Args:
            table_name (str) : Name of table where we want to insert data
            data (dict) : Dictionary of data we need to insert
        """
        
        engine = create_engine('sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        try:
            conn.execute(text(f"INSERT INTO {table_name} {tuple(data.keys())} VALUES {tuple(data.values())}"))
        except Exception as e:
            print(e)

    def delete(table_name: str, condition: str) -> None:
        """ Method for delete row from mysql table

        Args:
            table_name (str) : Name of table where we want to delete row
            condition (str) : condition for delete
        """
        engine = create_engine('sqlite:///C:\\Users\\admin\\Desktop\\Rango\\Projects\\Recommendation_System_With_Web\\app\\news.db')
        conn = engine.connect()
        try:
            conn.execute(text(f"DELETE FROM {table_name} WHERE {condition}"))
        except Exception as e:
            print(e)
    
    def fill_recommendations():
        pass