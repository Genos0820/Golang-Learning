from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add a title
pdf.set_font("Arial", style="B", size=14)
pdf.cell(0, 10, "Project Questions and Answers", ln=True, align="C")
pdf.ln(10)  # Add a line break

# Questions and Answers
content = """
1. SAML-based SSO:
Q: Can you explain how SAML-based Single Sign-On (SSO) works and how you implemented it in your Django application?
A: SAML-based SSO allows users to authenticate once and access multiple applications without logging in again. I implemented it by integrating a SAML Identity Provider (IdP) with Django using libraries like `python3-saml`. The IdP handles authentication, and the Django app validates the SAML response to grant access.

Q: What challenges did you face while integrating SAML-based SSO, and how did you overcome them?
A: One challenge was configuring the SAML metadata and certificates correctly. I resolved this by carefully matching the IdP metadata with the Service Provider (SP) settings in Django. Debugging tools like SAML Tracer were also helpful.

Q: How does implementing SAML-based SSO enhance the security of a web application?
A: SAML-based SSO reduces the risk of unauthorized access by centralizing authentication and eliminating the need for multiple passwords. It also supports features like multi-factor authentication (MFA) for added security.

2. Real-time Features with WebSocket:
Q: What specific real-time features did you implement using WebSocket technology in your application?
A: I implemented features like live expense updates and notifications using WebSocket. For example, when a user adds or edits an expense, other users in the group see the changes in real-time.

Q: How did you use Django Channels to enable WebSocket communication in your project?
A: Django Channels was used to handle WebSocket connections. I created consumers to manage WebSocket events and integrated them with Django views for seamless communication.

Q: Can you describe how you handled authentication and authorization for WebSocket connections?
A: I used Django's session authentication to validate WebSocket connections. Middleware was added to ensure only authenticated users could establish WebSocket connections.

3. Scalability and Maintainability:
Q: What best practices did you follow to ensure the scalability of your Django application?
A: I used database indexing for frequently queried fields and optimized queries with Django's ORM. Additionally, I deployed the application using a load balancer to handle high traffic.

Q: How did you structure your codebase to make it maintainable for future development?
A: The project followed Django's recommended structure with modular apps. I also used reusable components and adhered to the DRY (Don't Repeat Yourself) principle.

Q: Can you discuss any specific design patterns or architectural decisions you used in this project?
A: I used the MVC (Model-View-Controller) pattern inherent in Django and implemented reusable templates and class-based views for better maintainability.

4. General Django Development:
Q: How did you manage database migrations and schema changes in your project?
A: I used Django's built-in migration framework to manage schema changes. Each migration was tested in a staging environment before applying it to production.

Q: What tools or libraries did you use to test your Django application?
A: I used `pytest` and Django's `TestCase` for unit and integration testing. Tools like `coverage.py` helped ensure sufficient test coverage.

Q: How did you handle error logging and monitoring in your application?
A: I integrated tools like Sentry for real-time error tracking and logging. This helped identify and resolve issues quickly.

5. Security Enhancements:
Q: Besides SAML-based SSO, what other security measures did you implement in your application?
A: I implemented CSRF protection, secure cookies, and HTTPS for all communications. Sensitive data like passwords were hashed using Django's `make_password` function.

Q: How did you ensure the protection of sensitive user data in your project?
A: I used environment variables to store sensitive information like API keys and database credentials. Additionally, I encrypted sensitive fields in the database.

6. Performance Optimization:
Q: Did you encounter any performance bottlenecks while implementing real-time features? If so, how did you address them?
A: While implementing real-time features, I encountered latency issues with WebSocket connections. I optimized this by using Redis as a message broker for Django Channels.

Q: How did you optimize the performance of your Django application for handling high traffic?
A: I used caching mechanisms like Django's `cache` framework and a CDN for static files to reduce server load and improve response times.
"""

# Add content to the PDF using multi_cell for proper wrapping
for line in content.split("\n"):
    pdf.multi_cell(0, 10, txt=line.strip())

# Save the PDF
pdf.output("Project_QnA.pdf")
print("PDF created successfully as 'Project_QnA.pdf'")