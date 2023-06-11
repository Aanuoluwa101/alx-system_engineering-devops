**INCIDENT REPORT PRESENTED 12TH JUNE, 2O23**
This is a postmortem for an outage of our authentication services that happened on the 11th of June, 2023.
**I THINK WE JAMMED THE DOOR WHILE TRYING SO HARD TO MAKE IT EASIER TO OPEN...AND MAYBE JAMMED EVERYONE'S FINGERS TOO IN THE PROCESS.**
We truly apologize to everyone affected by this.

**Issue Summary**  
From 2:30PM to 3:15PM WAT, our authentication servers could not access the database.
The issue affected 100% of traffic and this meant that all users could not access their accounts and remained locked out from the sites functionalities. The root cause of this outage was due to 
a software bug in our Database Management System (DBMS), introduced by a software update, causing it to crash. 

**Timeline (all West African Time)**
- 2:00 PM: Software update push
- 2:15 PM: Unusual spike in traffic
- 2:30 PM: spike triggers bug and outage begins
- 2:31 PM: Pager alerts team of an unresponsive database
- 2:34 PM: On-call engineer checked database servers for hardware issues and other things
- 2:50 PM: On-call engineer escalates the issue to senior engineer
- 2:55 PM: Senior engineer discovers bugs and recommends a rollback of software update
- 3:04 PM: Successful update rollback and server restart begins
- 3:15 PM: Authentication service fully functional

**Root cause and resolution**  
AT 2:30 PM WAT, a software update was pushed after multiple testing. The update
included a bug related to query execution and memory management into our DBMS. This bug
went unnoticed during testing but was triggered the bug and caused the DBMS to run into 
an error that made it unresponsive. This led to our authentication servers recieving a 
500 error when trying to request users' credentials from the databases. This is when the outage began.

At 2:31 PM, our monitoring systems and on-call management system
alerted the engineer on-call. At 2:34 PM, in response, The engineer checked the database server for hardware bottlenecks
and even attempted a restart of the server.This failed and the problem was escalated to a senior engineer who discovers
the bug in the most recent update push. AT 3:04 PM, we successfully rolled back the update and restarted the server.

AT 3:15 PM, the authentication server's requests were appropriately responded to and users were able to login. 

**Corrective and preventative measures**  
There should be an improvement in the testing process.
- Testing new updates under extreme conditions like unusual traffic spikes
- Establish a quicker issue escalation workflow

Our company is committed to providing the best experience to our users and we
apologize to everyone whom has been impacted by this outage. We enjoin everyone to 
join us in the journey as we strive even harder to provide better services.

Sincerely,  

Tech Lead MercyMercy on behalf of the Development Team.


