<center>

# Final Report
***

</center>

<right>

***Author(s):*** Abián Gustavo Castañeda Méndez, Diego Peraza Cabo, Samuel Eloy González Díaz
<br>
***Date:*** May 10, 2024
<br>
***Tutor:*** Alejandro Martín Zarza

</right>

<center>

# INDEX

</center>

1. [***INTRODUCTION.***](#id1)
2. [***TECHNOLOGIES USED.***](#id2)
3. [***WEB STYLE GUIDE.***](#id3)
4. [***RESEARCH.***](#id4)
5. [***COPYRIGHT.***](#id5)
6. [***RISKS AND MEASURES.***](#id6)
7. [***COMPLIANCE LEVEL IN SCOPE.***](#id7)
8. [***COMPLIANCE LEVEL IN TIME.***](#id8)
9. [***COMPLIANCE LEVEL IN COST.***](#id9)
10. [***FINAL PRODUCT.***](#id10)
11. [***LESSONS LEARNED TO CONSIDER IN FUTURE PROJECTS.***](#id11)
12. [***CONCLUSIONS, COMMENTS, AND FINAL ASSESSMENT.***](#id12)


### 1. INTRODUCTION. <a name="id1"></a>

This document is the final report of the project to develop a hammock reservation application for clients and a management system for the administrator. The
main purpose of this report is to comprehensively document the process of planning, design, implementation and evaluation of the system, as well as to 
highlight the achievements and lessons learned throughout the project.

### 2. TECHNOLOGIES USED. <a name="id2"></a>

The technologies used in the project are as follows:

**Django==4.2:** Django is a high-level web framework written in Python that allows for the rapid development of secure and maintainable web applications. 
It provides a set of components and design patterns that facilitate the creation of complex web applications.

**prettyconf==2.2.1:** PrettyConf is a Python library that facilitates managing application configuration using simple and readable configuration files. It 
allows for defining environment variables and default values clearly and orderly.

**djangorestframework==3.15.1:** Django REST Framework is a Django library that makes it easy to create web APIs using the REST architecture style. It provides 
tools for data serialization, user authentication, permission management, and creating class-based views.

**pillow==10.3.0:** Pillow is a Python image processing library commonly used to manipulate images in web applications. It provides tools for opening, 
manipulating, and saving images in a variety of formats.

**WeasyPrint==61.2:** WeasyPrint is a Python library that allows for generating PDF documents from HTML and CSS content. It is useful for generating reports 
or invoices in web applications.

**django-cors-headers==4.3.1:** Django CORS Headers is a Django library that simplifies configuring CORS (Cross-Origin Resource Sharing) headers in a web 
application. It allows the server to indicate to web browsers whether a web page is allowed to access resources from another origin.

**stripe==9.1.0:** Stripe is an online payment platform that facilitates accepting payments in web and mobile applications. The Stripe library provides tools 
for integrating Stripe's payment functionality into a Django application.

**django-debug-toolbar==4.3.0:** Django Debug Toolbar is a debugging tool for Django applications that displays useful information for developers while 
debugging an application. It provides interactive panels showing information about database queries, HTTP requests, and performance.

**gunicorn==22.0.0:** Gunicorn is a Python HTTP server commonly used to deploy Django web applications in production. It provides an efficient and scalable 
runtime environment for Python web applications.

**psycopg2-binary==2.9.9:** Psycopg2 is a PostgreSQL database adapter for Python that allows Python applications to interact with PostgreSQL databases.

**celery==5.4.0:** Celery is a Python library for executing tasks in the background or in parallel, asynchronously. It is commonly used for tasks that are 
CPU-intensive or that may take a long time to complete, such as sending emails or generating reports.

**redis==5.0.4:** Redis is an open-source, in-memory database commonly used as a caching data store or message queue in web applications. The Redis library 
provides tools for interacting with a Redis server from a Python application.

**qrcode==7.4.2:** It is a Python library that allows for generating QR codes programmatically. QR codes are two-dimensional barcodes that can contain a 
variety of data, such as URL links, plain text, contact information, etc.

### 3. WEB STYLE GUIDE. <a name="id3"></a>

The achievement we have set for ourselves is to establish visual and design guidelines for an application that allows users to reserve hammocks and manage 
them, both for users and administrators. The application should be intuitive, easy to use, and provide a pleasant experience in terms of functionality and 
aesthetics:

#### 3.1 Responsiveness

Ensure that the application is accessible and functional on all possible devices, from computers to mobile phones, adapting the design and layout according to 
the screen size.

#### 3.2 Colors

Select colors that convey a sense of relaxation and freshness, in line with the created logo, achieving a feeling of calmness and tranquility.

#### 3.3 Interface

Design a user interface that is intuitive and easy to navigate for both users looking to reserve a hammock and administrators needing to manage them. This 
includes proper layout, buttons, and interactive elements.

#### 3.4 Visual Feedback

Provide clear visual feedback regarding user actions, such as successful reservation confirmations or error messages. This helps keep the user informed about 
the status of the application and their actions.

#### 3.5 Testing and Continuous Improvement

Conduct comprehensive usability testing and gather user feedback to identify areas for improvement in the interface and user experience. The web style guide 
should be subject to periodic reviews and updates to ensure that the application remains effective and appealing to its target audience.

### 4. RESEARCH. <a name="id4"></a>

Before diving into the project, we had to search for some possible examples on the internet because we were quite lost on how an appropriate and attractive 
design could look. We didn't find much since the idea was quite unique, so we decided to unleash our imagination.

When we started, we had great ideas that we could apply, but time caught up with us, and therefore, we had to discard the very good idea of ​​using Angular in 
our project. This influenced our pace and motivation, but we managed to push forward and finish the project more or less on the same path.

### 5. COPYRIGHT. <a name="id5"></a>

Throughout the project, we have consistently utilized public content and referenced it to avoid any issues with copyright infringement. Just as we value respect
for our own work, we also appreciate the efforts of other individuals who earn their livelihood through their creations.

### 6. RISKS AND MEASURES. <a name="id6"></a>

During the project development, time became a constraint, and we had to take a step back, deciding not to use a frontend framework as it would require learning 
it from scratch within the approximately month and a half timeframe we had for the project. As a measure, we gathered and made the decision to move forward and 
do our best using the tools provided by Django, HTML, CSS, Bootstrap, and JS.

### 7. COMPLIANCE LEVEL IN SCOPE. <a name="id7"></a>

Everything agreed upon between the team and the supposed client has been implemented, except for the frontend where the agreed-upon technology was not used 
due to lack of time. However, this has not prevented the final product from appearing appropriately.

Among the agreed-upon functionalities that have been implemented are:

Home Page
Login
Client Area for Reservations
Payment System
PDF for verifying payments linked to QR codes
Admin Area for Management
API

### 8. COMPLIANCE LEVEL IN TIME. <a name="id8"></a>

At all times, the assigned time periods have been met, and as a result, a benefit has emerged: the fact that thanks to this organization, we have advanced 
several parts of the project ahead of schedule, which helped us improve the final product.  
### 9. COMPLIANCE LEVEL IN COST. <a name="id9"></a>

To ensure that the project stays economically sound and meets the established objectives, various actions and tests will be implemented:

#### 9.1 Budget Tracking

A budget tracking and control system will be established to continuously monitor the project costs.

#### 9.2 Detailed Planning

A detailed project planning will be conducted, including cost estimates for each task and activity. This helps identify potential areas of deviation and take 
preventive measures before they occur.

#### 9.3 Periodic Reviews

Periodic reviews of the project status will be conducted to assess progress in relation to the budget and established objectives. These reviews will be 
conducted weekly.

#### 9.4 Risk Assessment

Potential risks that could affect project costs will be evaluated, and strategies will be developed to mitigate these risks.

#### 9.5 Costing Tests

Costing tests will be proposed to ensure that the monthly product cost is realistic and accurate.

#### 9.6 Communication

Transparent communication will be maintained with all project stakeholders regarding anything related to its cost. This allows for greater collaboration and 
support in decision-making to keep the project on track.

#### 9.7 Continuous Learning

Results and lessons learned will be analyzed to continuously improve cost management processes and avoid similar errors in the future.

### 10.  FINAL PRODUCT. <a name="id10"></a>

#### 10.1 Landing Page

In this section, a website will be available to anyone where they can find information about us, the product that has been created, contact details, and most 
importantly, a section where they can choose the hotel where they are staying or, in the case of the administrator, where they are working.

#### 10.2 Login

In this area, both users and administrators will have to enter their credentials to access their respective areas. If you are an administrator, proceed 
directly to step **10.4**.

#### 10.3 Client Area

In this area, the client will have the possibility to make a reservation. They will find a series of sections where they can select the date and then the part 
of the pool where they want to stay. Then, they will proceed to payment where they will enter their details to complete the reservation. Finally, they will 
have the option to view their reservation by downloading a PDF and scanning the QR code or cancel it if they have made a mistake or want to go back.

#### 10.4 Administrator Area

In this area, the administrator will arrive at a menu where they can decide which area to go to (products, reservations, or users) and in each of them, make 
modifications, deletions, queries, or additions (except for reservations where only queries and deletions can be made to offer the consumer better efficiency 
and usability).
    
### 11.  LESSONS LEARNED TO CONSIDER IN FUTURE PROJECTS. <a name="id11"></a>

As a result of this project, we gained a great deal of knowledge and a first contact with what a real work environment could be like, beyond the internship. We have realized that good organization and teamwork are fundamental aspects for the good development of any project, and that we must improve for the future. In addition, having good communication at all times is crucial, to be able to carry out in an optimal way the decisions that we had to make, as in our case, for example, with the elimination of the frontend technology due to the lack of knowledge and problems that it was giving us.

### 12.  CONCLUSIONS, COMMENTS, AND FINAL ASSESSMENT. <a name="id12"></a>

We believe that the project together with the internship has given us a great experience and knowledge. We were left with a bad taste for not knowing how to get the most out of the application, not using a front-end framework. As we mentioned before, there was a moment when we were a bit in trouble and we decided to make the whole application in Django with Javascript, Html and Css. In this sense, we believe that perhaps, we could prioritize the teaching of a front-end framework in the second year to reinforce this point.
