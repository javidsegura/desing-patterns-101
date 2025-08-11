# Difficult

### Problem Statement: Dynamic Workflow and Approval System ⚙️

You're tasked with building a software system for a large enterprise to manage and automate business processes. The core of the system is a **workflow engine** that handles multi-step approvals for various types of requests (e.g., travel expenses, new hire onboarding, procurement requests).

Here are the key requirements for the system:

- **Diverse Workflow Types:** There are several distinct workflow types, each with its own set of sequential steps and business logic. For example:
    - **Travel Expense:** Submit → Manager Approval → Finance Approval → Payment.
    - **New Hire:** HR Approval → IT Provisioning → Welcome Kit Shipment.
    - **Procurement:** Request → Department Head Approval → Budget Review → Vendor Selection.
- **Dynamic Step Behavior:** The behavior of each step can change based on the current state of the workflow. For instance, a "Manager Approval" step might have different logic if the expense amount is over a certain threshold. It could automatically be forwarded to a "Director Approval" step instead.
- **State Management:** The workflow object itself must track its current state (e.g., "Pending Manager Approval," "Approved," "Rejected"). The system must ensure that only valid state transitions are possible. For example, a workflow cannot transition from "Payment" back to "Submitted."
- **User Actions:** Users can perform a limited set of actions on a workflow, such as `approve`, `reject`, or `forward`. The available actions for a user depend on the workflow's current state and the user's role. A user cannot reject an already-rejected workflow.
- **Audit Trail:** Every action taken on a workflow (submission, approval, rejection, state change) must be recorded in an immutable audit trail. This is a critical requirement for compliance. The logging of these actions should be a cross-cutting concern.
- **Extensibility:** The system needs to be easily extensible. Adding a new workflow type (e.g., "Marketing Campaign Approval") or a new step to an existing workflow should not require modifying the core workflow engine. New business logic for steps or transitions should be easy to add

## SOLUTION

- Objects
    - Object level
        - class Node()
            - methods
                - add_procedure(func: callable, *args, **kwargs)
                - set_state() ⇒ sets current state of “pending”, “approved” or “rejected”
                - add_metadata()
    - Operational level
        - class Workflow
            - methods
                - add_node(node : Node) → List[Node]
                    - We can use a `Chain of responbility` design pattern when trying to add a node to the workflow. We could verify for it to have a callable, to have some metadata, and other possible checks.
                - pretty_print() ⇒ we could have an `Iterator` design patterns that iterates down the graph (in this case linear DAG, later possibly different) that retrieves the metadata of each node and stores some diagram
            - note
                - We are using a `Builder` design pattern where we enable the possibility to add at each step new nodes of computation . This is for add_node(). There is a director with pre-defined steps for existing workflows such as Travel Expense, New Hire and Procurement. If u want to add a new process you just have to defined your own steps through the builder
                    - Dynamic step behavior is added by passing as params the values of a given step (for one of the predefined execution flows in the director) and conditionally using `Strategy` to resolve the given node. For instance if for a the Manger approval node a expense amount paramter is passed, a factory is used in order to select the proper processing logic, tho all with the same value
                - We use `State` design pattern in order to link all nodes state to each other. This allows travelling through time and reattempt logic
        
    - Manager level
        - class WorkflowEngine
            - methods
                - execute_workflow(workflow: Workflow, request_human_action: bool)
                    - Human action may be required before executing the workflow in order to approve, reject or forward
- General
    - We can use `Wrapper/Decorator` for logging purposes before executing relevant methods
- Discarded patterns
    - Adapter ⇒ theres no old interface
    - Observer, Mediator ⇒ theres no communication between objects
    - Bridge ⇒ theres only node type (abstraction) and only one way to process it. No M:N relationship
    - Abstract, simple factories and factory ⇒ the client needs to have access to Pizza() and Order() classes.
    - Prototype ⇒ no need to copy object
    - Singleton ⇒ no need to keep single instance of anything by now
    - Flyweight ⇒ no attribute being always shared between some existing items
    - Memento, Command ⇒ we use State instead
    - Visitor ⇒ no external responsibilioties defined yet.
    - Facade ⇒ no major class with lots of subgrouping logic
    - Proxy ⇒ no need to control the workflow engine accessing the nodes