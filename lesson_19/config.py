class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///movie.db"
    
class DevelopmentConfig(Config):
    DEBUG=True

    
class ProductionConfig(Config):
    ...