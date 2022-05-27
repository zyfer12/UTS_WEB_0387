from app.db import get_db


def get_news():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT title, content, news_id, datetime, flag FROM tbl_news_0387 WHERE flag = 1"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result


def get_news_by_id(news_id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT title, content, news_id, datetime, flag FROM tbl_news_0387 WHERE news_id = ? AND flag = 1"
    cursor.execute(query, [news_id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result


def insert_news(title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_news_0387(title, content, datetime, flag) VALUES (?,?,?,?)"
    cursor.execute(query, [title, content, datetime, flag])
    db.commit()
    return True
    


def update_news(news_id, title, content, datetime, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0387 SET title = ?, content = ?, datetime = ?, flag = ? WHERE news_id = ?"
    cursor.execute(query, [title, content, datetime, flag, news_id])
    db.commit()
    return True

def flag_news(news_id, flag):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0387 SET flag = ? WHERE news_id = ?"
    cursor.execute(query, [flag, news_id])
    db.commit()
    return True

def delete_news(news_id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_news_0387 WHERE news_id = ?"
    cursor.execute(query, [news_id])
    db.commit()
    return True
