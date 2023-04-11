from blog.app import app, db

if __name__ == "__main__":
    app.run(
        debug=True,
        )


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")
