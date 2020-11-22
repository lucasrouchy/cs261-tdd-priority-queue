# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# YOUR NAME

class Job:
    def __init__(self, priority = None, message = None):
        self.priority = priority
        self.message = message
    def __eq__(self,p):
        return self.priority == p.priority
    def __lt__(self,p):
        return self.priority < p.priority
    def __gt__(self,p):
        return self.priority > p.priority
    
