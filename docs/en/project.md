<div align="center">

# IT Department - I.E.S. PUERTO DE LA CRUZ – TELESFORO BRAVO 

***

### PROJECT MODULE (PRW)

### H.L.T.C. Web Applications Development (DAW) 

<img src="../../src/img/Jhoola-logo3.png" width="200" />

<br>
</br>




***Author(s):*** Abián Gustavo Castañeda Méndez, Diego Peraza Cabo, Samuel Eloy González Díaz

***Date:*** 10 de Mayo de 2024

***Tutor:*** Alejandro Martín Zarza



</div>
<center>

# INDEX 

</center>

1. [***INTRODUCTION.***](#id1)
2. [***ORIGIN, CONTEXTUALIZATION, AND JUSTIFICATION OF THE PROJECT.***](#id2)
3. [***GENERAL OBJECTIVE OF THE PROJECT.***](#id3)
4. [***GENERAL DESCRIPTION OF THE PROJECT (SCOPE).***](#id4)
5. [***TIMETABLE.***](#id5)
6. [***SUMMARY OF TASKS, HUMAN AND MATERIAL RESOURCES.***](#id6)
7. [***RISK CONTROL.***](#id7)
8. [***POLICY FOR MONITORING, EVALUATION, AND QUALITY CONTROL.***](#id8)
9. [***CLAUSES.***](#id9)
10. [***BIBLIOGRAPHY..***](#id10)
11. [***GLOSSARY.***](#id11)
12. [***ANNEXES.***](#id12)

### 1. INTRODUCTION. <a name="id1"></a>

The main objective of this document is to establish the bases and the path to follow for the development of a project aimed at the management of hammock 
reservations in hotels. It will detail the objectives, scope, requirements and resources needed to carry out the project successfully.

### 2. ORIGIN, CONTEXTUALIZATION, AND JUSTIFICATION OF THE PROJECT. <a name="id2"></a>

#### Origin of the idea

The idea of developing a hammock reservation management system in hotels arises as a response to a situation experienced by many individuals. On many 
occasions there has been a bad experience of having to deal with people who get up very early to take the hammocks or leave their belongings at night 
causing mismanagement and fights for which the hotels are not responsible. In addition, with digitalization on the rise in the hotel industry, 
the aim is to take advantage of technology to improve the quality of service offered.

#### Needs identified

As a result of the information mentioned in the previous point, several needs have been identified that are not being fully satisfied. Among these needs, the 
following stand out:

**Complexity in booking:** Customers often find the hammock booking process complicated and unintuitive, which can result in a frustrating experience.

**Lack of control and monitoring:** Hotel managers lack adequate tools to manage and monitor hammock reservations effectively, which can lead to uneven 
distribution of available spaces.

**Opportunities for improvement in customer experience:** There is potential to improve customer experience by offering a more streamlined and personalized 
booking process, as well as greater transparency in hammock availability.

#### Problems to solve

The main problems that this project seeks to address is the lack of a comprehensive hammock reservation management system that meets the needs of both 
customers and hotel managers. This problem can result in an unsatisfactory customer experience, inefficient space allocation and lost revenue opportunities 
for the hotel.

#### Project justification

The justification for this project lies in the importance of improving the customer experience, optimizing hotel resources and increasing their competitiveness
in the tourism market, as well as generating more jobs and favoring the economy of the territories by giving the possibility of generatingmore wealth to the 
hotels with the reservation system.

In summary, this project seeks to solve a need identified in the hotel market by implementing a technological solution that benefits both clients and hotel 
managers.

### 3. GENERAL OBJECTIVE OF THE PROJECT. <a name="id3"></a>

The overall objective of this project is to develop a web application using the Django framework, which allows the efficient management of hammock reservations 
in hotels. This application will provide customers with an intuitive platform to make hammock reservations quickly and easily using a secure payment 
system, while providing administrators with tools to monitor and manage these reservations effectively.

### 4. GENERAL DESCRIPTION OF THE PROJECT (SCOPE). <a name="id4"></a>

The project consists of developing a web application to manage lodging reservations in an efficient and accessible way. The application will be designed to 
provide a seamless experience for both users making reservations and administrators managing the system. The following is the general description of the 
project:

#### General operation of the application

Both users and administrators will be able to access the application through a web browser from any device with an internet connection. They will be able to 
search for the hotel where they are staying and then go to a window where they will have to log in with the data provided. 

In the case of customers, once they have accessed their area they will be able to make reservations by choosing the product to be booked and the features 
that come with it and manage their existing reservations.

Administrators will have access to an administration panel where they will be able to manage reservations, manage the products that can be reserved and manage 
the creation of users.

#### Divisions of the application

The application will be divided into two main parts: the frontend and the backend.

- The frontend will be that set of designs that will be made to make the administrator and customer experience excellent.
  
- The backend will be responsible for processing client requests, interacting with the database and performing the business logic. In addition, an
intermediate layer will be implemented for authentication and user session management.

#### Architecture and structure

- For the backend, the Django web framework will be used, known for its robustness, scalability and security. Django provides a structure that facilitates
the development and organization of the code.

- For the frontend, HTML, CSS and JavaScript will be used for the static part of the user interface. In addition, Bootstrap 5 will be integrated to
ensure a responsive and attractive design.

- User authentication will be performed using mechanisms provided by Django, such as the built-in authentication system or using external libraries such as
Django REST Framework for token-based authentication.

- Data validation will be performed on both the frontend and backend to ensure data integrity.

#### Technologies to be used:

- Backend: Django, Django REST Framework, Python.

- Frontend: HTML, CSS, JavaScript, Bootstrap 5.

- Database: Possibly SQLite will be used for development and testing, and will be migrated to a more robust database such as PostgreSQL for production.

- Deployment: The use of a VPS in Azure is contemplated for the deployment of the project, with the possibility of implementing Docker containers for ease
of management and scalability.

In summary, the project will be structured using modern and robust technologies to deliver an efficient and secure web application for accommodation booking 
management.

### 5. TIMETABLE. <a name="id5"></a>

Since the diagram is too large to be shown in screenshots, a link to access it will be attached.

https://github.com/users/TheReported/projects/1/views/4

### 6. SUMMARY OF TASKS, HUMAN AND MATERIAL RESOURCES. <a name="id6"></a>

In the following table we will try to make an estimate (impossible to make it exact) of the dates in which work was done in the different areas of the 
project and the time it took.
<center>

| Task | Title | Description and Methodology | Duration | Start Date | End Date | Human Resources | Material Resources | Cost | Responsible |
|-------|--------|----------------------------|----------|-----------|-----------|------------------|---------------------|-------|-------------|
| Task 1 | Landing Page Development | A landing page was developed for the application where customers can find information about our project, such as how to contact us, etc. | 4-5 hours | March | March | 1 | 0 | €0 (It will be a service) | Abián |
| Task 2 | Hotel Login Development | A hotel search with autocomplete was developed so that customers and administrators can search for their hotel before logging in. | 4-5 hours | March | April | 1 | 0 | €0 (It will be a service) | Samuel |
| Task 3 | Main Login Development | A login for the hotel was developed through which customers and administrators would verify themselves before using the application. | 4 hours | March | April | 3 | 0 | €0 (It will be a service) | Abián, Diego, and Samuel |
| Task 4 | Admin Area Development | An admin area was developed from which administrators can manage user, product, and customer reservation information. | 12-16 hours | March | May | 3 | 0 | €0 (It will be a service) | Abián, Diego, and Samuel |
| Task 4.1 | Admin Area Backend Development | The programming logic behind the admin area, allowing administrators to manage user, product, and customer reservation information, was developed. | 5-6 hours | March | May | 3 | 0 | €0 (It will be a service) | Abián, Diego, and Samuel |
| Task 4.2 | Admin Area Frontend Development | The visual representation of the admin area, allowing administrators to manage user, product, and customer reservation information, was developed. | 7 - 8 hours | March | May | 2 | 0 | €0 (It will be a service) | Abián and Samuel |
| Task 5 | Customer Area Development | A customer area was developed from which customers can make, check, and cancel reservations. | 8-11 hours | April | May | 3 | 0 | €0 (It will be a service) | Abián, Diego, and Samuel |
| Task 5.1 | Payment System and Backend Development | Stripe was used to develop a payment system for the customer area. | 4-6 hours | April | May | 1 | 0 | €0 (It will be a service) | Abián, Samuel |
| Task 5.2 | Frontend Development for Customer Area | HTML, CSS, JS, and Bootstrap were used to design the customer area. | 4 hours | April | May | 1 | 0 | €0 (It will be a service) | Samuel |
| Task 5.3 | Hammock Selector Development and Logic | JS, backend, and SVGs were used to develop the logic behind the hammock selector. | 4 hours | April | May | 1 | 0 | €0 (It will be a service) | Diego |
| Task 6 | API Development | An API was developed to efficiently and securely connect the different areas of the application. | 2 hours | March | March | 1 | 0 | €0 (It will be a service) | Diego |
| Task 7 | Application Deployment | The application was prepared for automated deployment using a script on an Azure machine. | 1 hour | May | May | 1 | 0 | €0 (It will be a service) | Diego |
| Task 8 | Database Migration to PostgreSQL | The application was migrated to PostgreSQL to improve efficiency and security. | 1 hour | May | May | 1 | 0 | €0 (It will be a service) | Diego |
| Task 9 | Application Testing Development | A series of tests were conducted to ensure the proper functioning of the application. | 2 hours | April | May | 1 | 0 | €0 (It will be a service) | Abián |
| Task 10 | Final Application Responsiveness | Responsiveness was applied to the entire application. | 10-12 hours | May | May | 1 | 0 | €0 (It will be a service) | Samuel |

</center>

### 7. RISK CONTROL. <a name="id7"></a>

#### 7.1 Risk of minor changes in client requirements

**Probability:** Low (0.10)

**Impact:** Low (0.20) → These are usually minor changes that do not significantly affect the project scope or timeline.

**Risk Type:** Low

**Action to Take:** Divide these changes calmly among the various workers involved in the project. The team can handle these changes easily without the need for additional intervention. Agile practices can be implemented to adapt to changes efficiently and ensure customer satisfaction.

#### 7.2 Risk of deployment infrastructure failures

**Probability:** Very Low (0.10)

**Impact:** Medium (0.40) → Could cause service interruptions and affect application availability.

**Risk Type:** Medium

**Action to Take:** Mitigation Plan → Conduct various exhaustive tests of the deployment infrastructure and configure systems to detect potential issues. Additionally, establish a protocol for quick response to address any failures and minimize downtime.

#### 7.3 Risk of lack of experience with selected technologies

**Probability:** High (0.60)

**Impact:** Medium (0.50) → Could result in development delays and require additional time to learn and adapt to new technologies.

**Risk Type:** High

**Action to Take:** Mitigation Plan → Change the working model applied in the project to launch it with the technologies that the team is familiar with or directly transition to an agile learning process to move the project forward.
  
### 8. POLICY FOR MONITORING, EVALUATION, AND QUALITY CONTROL. <a name="id8"></a>

To ensure that the project stays on track and meets the set objectives, various monitoring, evaluation, and quality control actions will be implemented. Here are some of the actions to be carried out:

#### 8.1 Regular Tracking Meetings

Regular meetings will be held with the project team to review progress, discuss any changes or issues, and take necessary actions if required.

#### 8.2 Milestone Tracking

Milestones will be set in the project schedule. Constant tracking will be conducted to ensure they are met within the established timelines.

#### 8.3 Code Reviews and Testing

Regular code reviews will be conducted to ensure its quality and consistency. Additionally, testing will be carried out to ensure that different system components function properly together.

#### 8.4 Customer Satisfaction Surveys and Beta Testing

Surveys will be sent to clients to assess their satisfaction with the project and gather feedback to identify areas for improvement. Additionally, they will be invited to test the application so that those less familiar with the field can help us find errors.

#### 8.5 Team Feedback

A healthy environment will be fostered within the team, where members can share their ideas, concerns, and suggestions to improve the process and the final product.

By implementing these monitoring, evaluation, and quality control actions, the team will be able to stay tuned to the project's progress, identify and address unforeseen cases in a timely manner, and ensure the delivery of a high-quality product that meets the client's requirements and expectations.

### 9.  CLAUSES. <a name="id9"></a>

#### 9.1 Delivery and Deadlines

- The delivery of the web application to the company will be made on the agreed-upon date between the parties, as specified in the initial contract.
  
- In case of any delays in delivery on our team's part, financial penalties will be applied.
  
- Deadlines for each project functionality will be detailed in the schedule and can only be modified post-contract with the mutual consent of the team and the client.

#### 9.2 Payments

- Payment will be made according to the schedule established in the contract, detailing the monthly amount and the date it is due.
  
- The client commits to making payments as agreed upon, and the team will deliver the project and support **if acquired** as stipulated.
  
- In case of non-compliance with payments by the client, the team reserves the right to suspend its activities until the situation is resolved.

#### 9.3 Intellectual Property

- All intellectual property rights of the developed software, including the source code, documentation, and any associated material, will be the exclusive property of Jhoola.

#### 9.4 Support

- Support will be provided to the client if they acquire the subscription that includes such service.

#### 9.5 Confidentiality

- Both parties agree to maintain the confidentiality of all information provided during the project, including client data, project details, and any other sensitive information.
  
- The aforementioned point shall remain in force even after the implementation of the project or the termination of the contract.

#### 9.6 Quality and Change Control

- The development team commits to meeting agreed-upon quality standards and conducting thorough testing to ensure the proper functioning of the web application.
  
- Changes or improvements to be implemented will require written approval from the client and may involve adjustments to the schedule and an increase in the application's cost.

#### 9.7 Conflict Resolution

- If a problem arises between the team and the client, both parties will attempt to resolve it amicably and through direct negotiations.

#### 9.8 Service Cancellation

- In case the client wishes to cancel their service, they only need to do so before the payment for the following month. If payment has already been made, we do not commit to refunding the money.

### 10. BIBLIOGRAPHY. <a name="id10"></a>

- [Django](https://docs.djangoproject.com/en/5.0/)
- [ChatGPT](https://chatgpt.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Docs Python](https://docs.python.org/3/)
- Django 4 By Example
- [Developer Mozilla](https://developer.mozilla.org)
- [Material Icons](https://fonts.google.com/icons)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/es)
- [Django Cors-Headers](https://pypi.org/project/django-cors-headers/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/es/)
- [Django REST framework](https://www.django-rest-framework.org/)
    
### 11. GLOSSARY. <a name="id11"></a>

**- API (Application Programming Interface):** A set of rules and definitions that allows software applications to communicate with each other.

**- Backend:** The part of a web application that handles client requests, interacts with the database, and performs business logic.

**- Frontend:** The part of a web application that interacts directly with the user, providing the graphical interface they interact with.

**- Testing:** The process of evaluating a system or application to verify that it meets specified requirements and to identify defects or errors.

**- Beta Testing:** It is a stage in the development of a product, whether software, hardware, or any other type of product, in which a preliminary version of it is made available to a limited group of external users.

**- Token:** A unique and temporary code generated and sent to the user as part of an authentication process.

**- Landing Page:** A web page designed specifically to receive and convert visitors into leads or potential customers.

### 12. ANNEXES. <a name="id12"></a>

- [Diagrams](https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/README.md)
- [Final Report](https://github.com/TheReported/jhoola/blob/development/docs/en/finalreport.md)
