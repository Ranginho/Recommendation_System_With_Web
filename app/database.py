from app import db

class Articles(db.Model):
    article_id = db.Column(db.Integer, primary_key = True)
    article_name = db.Column(db.String(), nullable = False)
    article_description = db.Column(db.String())
    article_image_path = db.Column(db.String(), nullable = False)
    link_to_article = db.Column(db.String())

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
