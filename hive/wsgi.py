from hive.application import Application

app = Application()


def main():
    app.init()
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
