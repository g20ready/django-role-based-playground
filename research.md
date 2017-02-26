# Django Role Permissions

    ## Pros
    
    1. Easy to use
    2. Covers most cases
    3. Has build-in filters, decorators
    4. Mixin for both Views and Objects
    5. Does not create (additional) or alter (existing) database tables
    
    ## Cons
    
    1. Does not support multiple roles assigned to a user 
       (There is a request for this feature issue#37)
    2. You have to migrate (add your custom roles) to existing users, 
       otherwise no role is assigned
    