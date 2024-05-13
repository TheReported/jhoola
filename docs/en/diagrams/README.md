# Application Analysis and Design

In this document we will analyze and design our application using the different diagrams and specifications we are familiar with.

## Specification of the DB E/R Diagram

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/jhoola-er.png">

## Specification of the MR diagram of the BBDD

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/jhoola-mr.png">

## UC specification

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/usecase_diagram_jhoola.png">

As you can see in the image the user will have to authenticate in order to make a reservation in which to complete it he/she will have to make a payment. By doing so, the user will be able to review the reservation, delete it or have at his disposal a PDF with the data. On the other hand, the administrator will be able to manage users, products and reservations. 

### Specification of Stakeholders

This document specifies the different stakeholders involved in the proposed solution.

#### User

| Stakeholder | User |
|---|---|
| Description  | The user can reserve hammocks at the hotel by logging in. |
| Characteristics  | Must go through authentication to perform the actions. |
| Relations | _No relations with other stakeholders_ |
| References | |   
| Notes |   |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Administrator 

| Stakeholder | Administrator |
|---|---|
| Description  | The administrator can manage products, reservations and users. |
| Characteristics  | Must go through authentication to perform the actions. |
| Relations | _No relations with other stakeholders_ |
| References | |   
| Notes |   |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Bank

| Stakeholder | Bank |
|---|---|
| Description  | The bank checks whether or not the payment can be made. |
| Characteristics  | |
| Relations | _No relations with other stakeholders_ |
| References | |   
| Notes |   |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

### Specification of Use Cases

This document specifies the use cases that are part of the proposed solution.

#### Authenticate

| Use Case CU.1 | Authenticate |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user must authenticate before performing anything. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Book

| Use Case CU.2 | Book |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user can book hammocks. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | Pay the reservation. |  
| Requirements | Be authenticated. |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Payment

| Use Case CU.3 | Payment |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user must pay at the time of booking. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | Be authenticated and have made a reservation |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Check

| Use Case CU.4 | Check |
|---|---|
| Sources | |
| Stakeholder | Bank |
| Description | The bank verifies whether payment can be made. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Accepted

| Use Case CU.5 | Accepted |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | Payment has been accepted. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a payment has been made |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Cancel Book

| Use Case CU.6 | Cancel Book |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | Cancel reservation in case of mistake. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a payment has been accepted. |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Denied

| Use Case CU.7 | Denied |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | Payment has been denied. |
| Basic flow | |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a payment has been made |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Delete

| Use Case CU.8 | Delete |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user deletes his reservation. |
| Basic flow | |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a reservation has been made. |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _07/05/2024_ |

#### Consult

| Use Case CU.9 | Consult |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user consults his reservation. |
| Basic flow | |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a reservation has been made. |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _07/05/2024_ |

#### Download PDF

| Use Case CU.10 | Download PDF |
|---|---|
| Sources | |
| Stakeholder | User |
| Description | The user downloads a PDF with the reservation data. |
| Basic flow | |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements | That a reservation has been made. |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _07/05/2024_ |

#### Authenticate

| Use Case CU.11 | Authenticate |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator must authenticate before performing anything. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### User Management

| Use Case CU.12 | User Management |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can manage application users. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Create

| Use Case CU.13 | Create |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can create users in the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Read

| Use Case CU.14 | Read |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can consult the users of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Update

| Use Case CU.15 | Update |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can modify the users of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Delete

| Use Case CU.16 | Delete |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can delete the users of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Booking Management

| Use Case CU.17 | Booking Management |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can manage application bookings. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Read

| Use Case CU.18 | Read |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can consult the bookings of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Delete

| Use Case CU.19 | Delete |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can delete the bookings of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Product Management

| Use Case CU.20 | Product Management |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can manage application products. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Create

| Use Case CU.21 | Create |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can create products in the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Read

| Use Case CU.22 | Read |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can consult the products of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Update

| Use Case CU.23 | Update |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can modify the products of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

#### Delete

| Use Case CU.24 | Delete |
|---|---|
| Sources | |
| Stakeholder | Administrator |
| Description | The administrator can delete the products of the application. |
| Basic flow |  |
| Pre-conditions |  |  
| Post-conditions | |  
| Requirements |  |
| Notes |  |
| Author | _Abián Castañeda Méndez_ |
| Date | _06/03/2024_ |

## Specification of the class diagram

<img src="https://github.com/TheReported/jhoola/blob/development/docs/en/diagrams/img/class_diagram_jhoola.png">

In this diagram a hotel has a large number of products and users and at the same time they have the possibility to make from none to many reservations. On the other hand, the administrator, who has the same tools as the user, has superior powers that allow him to manage the different areas.
