# ERPNext Service Management System

This project was built as part of a Service Management assignment using ERPNext and the Frappe Framework.

The goal was to create a simple system for managing service requests, technician visits, and ticket resolution.

## What I Built

### Service Ticket

Used to register customer complaints and service requests.

Fields included:

* Customer
* Contact Person
* Equipment Serial Number
* Complaint Description
* Priority
* Status
* Assigned Technician
* SLA Due Date

### Service Visit

Used to record technician visits against a service ticket.

Fields included:

* Service Ticket
* Technician
* Visit Date
* Start Time
* End Time
* Resolution Notes
* Duration

### Service Contract

Created to store service contract information for customers.

### Parts Used

Implemented as a child table to track parts used during a service visit.

## Workflow

A workflow was created for Service Tickets with the following states:

Open → Assigned → In Progress → Resolved → Closed

This helps track the progress of a service request from creation to completion.

## Automation Implemented

A custom Python hook was added on Service Visit submission.

When a Service Visit is submitted:

* Duration is calculated from Start Time and End Time.
* The linked Service Ticket status is automatically changed to Resolved.
* A comment is added to the Service Ticket timeline.

This logic is implemented in:

service_app/service_app/events/service_visit.py

## Report

A report was created to view Service Tickets along with important information such as:

* Customer
* Priority
* Status
* Assigned Technician
* SLA Due Date

## Tech Stack

* ERPNext v15
* Frappe Framework v15
* Python
* MariaDB
* Ubuntu (WSL)

## What I Learned

This was my first hands-on project with ERPNext/Frappe. Through this assignment I learned:

* Creating custom DocTypes
* Building workflows
* Working with document events
* Writing Frappe hooks
* Creating reports
* Managing ERP-style business processes

## Demo

The demo shows the following flow:

1. Create a Service Ticket
2. Assign a Technician
3. Create a Service Visit
4. Enter Start and End Time
5. Submit the Visit
6. Duration gets calculated automatically
7. Service Ticket status changes to Resolved
