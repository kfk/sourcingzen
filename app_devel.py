from sourcingzen import app

app.config.update(
	DEBUG=True,
	SQLALCHEMY_DATABASE_URI = 'sqlite:////home/alessio/projects/sourcingzen/test.db',
	SECRET_KEY = 'Very secret key'
	)
if __name__ == "__main__":
    app.run()

