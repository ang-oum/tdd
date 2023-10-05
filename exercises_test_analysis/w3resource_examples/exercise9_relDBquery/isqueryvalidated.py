import unittest
import sqlite3

class TestDatabaseQuery(unittest.TestCase):
    
    def setUp(self):
        # Create a database connection and insert test data
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
        self.conn.commit()

    def tearDown(self):
        # Close the database connection
        self.cursor.close()
        self.conn.close()

    def test_database_query(self):
        # Execute the query
        self.cursor.execute("SELECT name, salary FROM employees ORDER BY name")
        results = self.cursor.fetchall()

        # Define the expected results
        expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]

        # Assert that the results match the expected results
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
