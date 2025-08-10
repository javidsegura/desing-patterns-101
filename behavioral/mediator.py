"""

Intent: multidirectional communication between objects (in contrast with 1:M from Observer's)

Components:
      - Mediator => based on given event type it notfieis corresponding element
      - Colleage => has references to mediatior, makes mediatior notify, has receive point 

Usecase:
      - AdmissionsOfficerMediator mediates messages between Admission office, Student and professor
      - Interaction:
            - Admissions offices notifies students on apploication resutls
            - Student sends application and notifies professor for recommendation letter and admision offices which rejects randomly
            - Professor notifies student on recommendation

"""

from abc import abstractmethod, ABC
from typing import Any, Optional, List
import random


class Mediator(ABC):
      @abstractmethod
      def notify(self, sender: "Colleague", event: str, data: Any):
            pass

class Colleague(ABC): # Corrected from Colleage to Colleague
      def __init__(self, mediator: Mediator) -> None:
            self.mediator = mediator
      
      @abstractmethod
      def receive(self, event, data):
            pass

class AdmissionsOfficerMediator(Mediator):
      def __init__(self) -> None:
            self._admissions_office: Optional['AdmissionsOffice'] = None
            self._students: List['Student'] = []
            self._professors: List['Professor'] = []

      def set_admissions_office(self, office: 'AdmissionsOffice'):
        self._admissions_office = office

      def add_student(self, student: 'Student'):
            self._students.append(student)

      def add_professor(self, professor: 'Professor'):
            self._professors.append(professor)

      def notify(self, sender: Colleague, event: str, data: Any):
            if event == "application_submitted":
                  if self._admissions_office:
                        self._admissions_office.receive(event, data)
            elif event == "recommendation_request":
                  for professor in self._professors:
                        if professor.name == data["professor_name"]: # Use professor_name key
                              professor.receive(event ,data)
                              break
            elif event == "admission_decision":
                  for student in self._students:
                        if student.name == data["student_name"]: # Use student_name key
                              student.receive(event, data)
            elif event == "recommendation_submitted":
                  for student in self._students:
                        if student.name == data["student_name"]: # Use student_name key
                              student.receive(event, data)


class AdmissionsOffice(Colleague):
      def __init__(self, mediator: Mediator) -> None:
            super().__init__(mediator)
      
      def process_application(self, student_name: str):
            print(f"Admissions Office: Processing application for {student_name}.")
            accept_application = random.random() >= 0.5
            print(f"Admissions Office: Decision for {student_name} is {'Accepted' if accept_application else 'Rejected'}.")
            self.mediator.notify(self, "admission_decision", {"student_name": student_name, "status": accept_application})
      
      def receive(self, event: str, data: Any):
            if event == "application_submitted":
                  print(f"Admissions Office: Received application from {data['student_name']}.")
                  self.process_application(data["student_name"])
                  

class Student(Colleague):
      def __init__(self,name: str, mediator: Mediator) -> None:
            self.name = name
            super().__init__(mediator)

      def submit_application(self, professor_name: str):
            print(f"{self.name}: Submitting application and requesting recommendation from {professor_name}.")
            self.mediator.notify(self, "recommendation_request", {"student_name": self.name, "professor_name": professor_name})
            self.mediator.notify(self, "application_submitted", {"student_name": self.name})

      def receive(self, event, data):
            if event == "admission_decision":
                  status = "Accepted" if data["status"] else "Rejected"
                  print(f"{self.name}: Received admission decision: {status}.")
            elif event == "recommendation_submitted":
                  print(f"{self.name}: Received recommendation notification.")
      
class Professor(Colleague):
      def __init__(self, name: str, mediator: Mediator) -> None:
            self.name = name
            super().__init__(mediator)

      def submit_recommendation(self, student_name: str):
            print(f"{self.name}: Submitting recommendation for {student_name}.")
            self.mediator.notify(self, "recommendation_submitted", {"student_name": student_name})

      def receive(self, event, data):
            if event == "recommendation_request":
                  print(f"{self.name}: Received recommendation request for {data['student_name']}.")
                  self.submit_recommendation(data["student_name"])

if __name__ == "__main__":
      admissions_mediator = AdmissionsOfficerMediator()

      admissions_office = AdmissionsOffice(admissions_mediator)
      student_alice = Student("Alice", admissions_mediator)
      student_bob = Student("Bob", admissions_mediator)
      professor_smith = Professor("Dr. Smith", admissions_mediator)
      professor_jones = Professor("Dr. Jones", admissions_mediator)


      admissions_mediator.set_admissions_office(admissions_office)
      admissions_mediator.add_student(student_alice)
      admissions_mediator.add_student(student_bob)
      admissions_mediator.add_professor(professor_smith)
      admissions_mediator.add_professor(professor_jones)

      print("\n--- Alice's Application Process ---")
      student_alice.submit_application("Dr. Smith")

      print("\n--- Bob's Application Process ---")
      student_bob.submit_application("Dr. Jones") # Bob asks Dr. Jones for recommendation