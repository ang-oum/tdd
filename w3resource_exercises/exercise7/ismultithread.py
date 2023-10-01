import unittest
import threading

def perform_task():
    # Simulate some task
    result = 0
    for i in range(1, 100000):
        result += i
    return result

class Test_Multi_Threading(unittest.TestCase):
    def test_multi_threading(self):
        num_threads = 10
        threads = []

        # Create and start multiple threads
        for _ in range(num_threads):
            t = threading.Thread(target=perform_task)
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Assert that all threads completed successfully
        for t in threads:
            self.assertFalse(t.is_alive())

if __name__ == '__main__':
    unittest.main()