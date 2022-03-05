import psycopg2
import logging
import os

logging.basicConfig(
    format='%(asctime)s | %(levelname)s: %(message)s', level=logging.DEBUG)

log = logging.getLogger()


def create_tables(conn, cursor):
    cursor.execute(open("setup.sql", 'r').read())

    conn.commit()

    logging.info("Tables have been added")


def ingest_csv(conn, cursor, csv_file):
    table = csv_file.split('/')[-1][:-4]

    with open(csv_file, 'r') as file_object:
        next(file_object)

        for count, _ in enumerate(file_object):
            pass

        cursor.copy_from(file_object, table, sep=',')
        file_object.close()

    conn.commit()

    logging.info(f'{csv_file} added, {count+1} lines ingested')


def main():
    csv_files = [
        f'./data/{csv}' for csv in os.listdir('./data') if csv.endswith('csv')]

    try:
        host = 'postgres'
        database = 'postgres'
        user = 'postgres'
        pas = 'postgres'
        conn = psycopg2.connect(host=host, database=database,
                                user=user, password=pas)

        cursor = conn.cursor()

        create_tables(conn, cursor)

        for csv_file in csv_files:
            ingest_csv(conn, cursor, csv_file)

    except (Exception, psycopg2.Error) as error:
        logging.warn("Error while working with PostgreSQL", error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            logging.info("PostgreSQL connection is closed")


if __name__ == '__main__':
    main()
