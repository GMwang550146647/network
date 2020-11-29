

from utils.DataBase import DataBase


if __name__ == '__main__':
    with DataBase() as db:
        db.main()