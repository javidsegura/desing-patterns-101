# Easy

## Problem

Imagine you're building a software system for a **pizza restaurant chain** that takes online orders. This system needs to handle several things:

1. Customers can build a pizza with different toppings, sauces, and crust types.
2. The system needs to calculate the price of the pizza based on these choices.
3. The restaurant needs to be able to add new toppings, sauces, or crusts easily without changing the core ordering logic.
4. The system should also be able to create different types of receipts—a simple text receipt for the kitchen and a detailed, formatted receipt for the customer's email.

## Solution

- Objects
    - Object level
        - ingredient ⇒ Pydantic model with attrs
            - attrs
                - name
                - price_per_unit
                - total_units
            - methods
                - If we have certain ingrendients that are a shortcut for many other, we can  use `Composite` design pattern in order to flatten that parent-children hiearhcy
        - class pizza(ingredients: List[ingredient])
            - methods
                - accept
            - note
                - contains `Visitor` design pattern for calculating price (currently just of pizza element possibly more in the future)
                - we use a `Builder` in order to add to crust, sauce and ingredients more modular, and validating ingredeints at that moment. We would also integrate a director class in order to have predefined builds
    - Operational level
        - class order
            - methods
                - add_item(item: pizza) ⇒ adds pizza
                - get_order_price() ⇒ gets total by visiting all pizza objects
                - get_status() ⇒
    - Manager level
        - class PaymentGateway
            - methods
                - charge
                - reimburse
            - note
                - contains `Proxy` design pattern in order to verify authentication before charging
        - class EmailService
            - methods
                - send_email
        - class orderProcessing(order: Order)
            - methods
                - place_order(order: Order) ⇒ order
                    - verify_order ⇒ Use `Chain of Responsibilities` to verify Order is compromised of valid ingredients, in stock, being offered (sometimes there is stock but may not be sold due to waiting for a promotion)
                    - charging ⇒ used PaymentGateway
                    - placing chef receipted  ⇒ uses EmailService
                    - sending user receipt ⇒ uses EmailService
            - note
                - We use `Command` in place_order in order to be able to revert actions
                - We use `Strategy` for chaining receipt strategy between chef and user
                - We use `Facade` for placing order where we keep references to verify_order class (command + CoR), charging class command, creating receipe chef and user. This ensures a simpler, less cluttered interface
    - General
        - We can use `Wrapper/Decorator` for logging purposes before executing relevant methods
- Client
    - Imports all ingredients, creates order, then places order
- Discarded patterns
    - Adapter ⇒ theres no old interface
    - Iterator ⇒ theres no clear need for iterating over any the specified objects
    - Observer, Mediator ⇒ theres no communication between objects
    - Bridge ⇒ theres only order type (abstraction) and only one way to process it. No M:N relationship
    - Abstract, simple factories and factory ⇒ the client needs to have access to Pizza() and Order() classes.
    - Prototype ⇒ no need to copy object
    - Singleton ⇒ no need to keep single instance of anything by now
    - Flyweight ⇒ no attribute being always shared between some existing items
    - Memento ⇒ revert is well-defined, we use Command instead
    - State ⇒ could be integrated if functionality changes when preparing order vs when placing vs when ready. Currently we assume theres no user-interaction after placing beyond checking status (for which updating an attribute does no justify the whole implementation of this design pattern)