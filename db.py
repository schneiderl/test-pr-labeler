
import sqlite3 as sl

class DB():
    def __init__(self):
        self.con = sl.connect('db.db', check_same_thread=False)
        self.__create_schema()

        
    def __create_schema(self):
        print("creating schema")
        with self.con:
            self.con.execute("""
                CREATE TABLE IF NOT EXISTS PRS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    original_pr TEXT,
                    origin_label TEXT,
                    generated_pr TEXT,
                    status TEXT,
                    branch TEXT
                );
            """)
            
            
    def insert_pr(self, original_pr, origin_label, generated_pr, status, branch):
        print("inserting pr")
        with self.con:
            self.con.execute("""
                INSERT INTO PRS (original_pr, origin_label, generated_pr, status, branch) values (?, ?, ?, ?, ?)
            """, (original_pr, origin_label, generated_pr, status, branch))
            
    def get_from_original_pr(self, original_pr):
        print("getting pr")
        with self.con:
            data = self.con.execute("""
                SELECT * FROM PRS WHERE original_pr = ?
            """, (original_pr,)).fetchall()
            return data
    
    def get_from_generated_pr(self, generated_pr):
        print("getting pr from generated")
        with self.con:
            data = self.con.execute("""
                SELECT * FROM PRS WHERE generated_pr = ?
            """, (generated_pr,)).fetchall()
            return data
        
    def change_status(self, generated_pr, status):
        print("changing status")
        with self.con:
            self.con.execute("""
                UPDATE PRS SET status = ? WHERE generated_pr = ?
            """, (status, generated_pr))
        
    def get_branch_from_original_pr_and_label(self, original_pr, origin_label):
        print("getting branch")
        with self.con:
            data = self.con.execute("""
                SELECT * FROM PRS WHERE original_pr = ? AND origin_label = ?
            """, (original_pr, origin_label)).fetchall()
            return data
    
    def delete_from_originaL_pr_and_label(self, original_pr, origin_label):
        print("deleting branch")
        with self.con:
            self.con.execute("""
                DELETE FROM PRS WHERE original_pr = ? AND origin_label = ?
            """, (original_pr, origin_label))
        
        
        
    # def insert_pr(self, original_pr, generated_pr, branch):
    #     print("inserting pr")
    #     with self.con:
    #         self.con.execute("""
    #             INSERT INTO PRS (original_pr,  generated_pr, branch) values (?, ?, ?)
    #         """, (original_pr, generated_pr, branch))
    
    # def get_from_original_pr(self, original_pr):
    #     print("getting pr")
    #     with self.con:
    #         data = self.con.execute("""
    #             SELECT * FROM PRS WHERE original_pr = ?
    #         """, (original_pr,)).fetchall()
    #         return data
    
    # def get_from_generated_pr(self, generated_pr):
    #     print("getting pr from generated")
    #     with self.con:
    #         data = self.con.execute("""
    #             SELECT * FROM PRS WHERE generated_pr = ?
    #         """, (generated_pr,)).fetchall()
    #         return data
    
    # def change_status(self, generated_pr, status):
    #     print("changing status")
    #     with self.con:
    #         self.con.execute("""
    #             UPDATE PRS SET status = ? WHERE generated_pr = ?
    #         """, (status, generated_pr))
    
    
db = DB()