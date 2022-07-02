# XSS-InjectionAndTestTools

Group Members:
Tuğcan Barbin 25168
Emre Ekmekçioğlu 25223
Doğan Can Hasanoğlu 26809

Video Link:
https://drive.google.com/drive/folders/10-WCqJdRvCtnt4ttr0DMrJkON1jzeni0?usp=sharing

Responsibility : 8 / Injection XSS

Description: We created a vulnerable Django web application to demonstrate XSS vulnerability.
First we created a Django project from scratch then added some features to create XSS
vulnerability. VS Code was used for editing issues and SQLite for databases. Our web
application was named LearnVul. Application consists of three main parts: Home, Search,
Contact. On the home page, you can comment on topics and see previously made comments.
Search tab is for searching as the name suggests. Contact is for suggesting new topics. For
front-end purposes we used HTML and CSS.

XSS vulnerability arises when the application takes input from the user and uses it without
sanitizing it. If this is the case an attacker can inject malicious payload to run javascript in the
browser. From the attackers point of view, first the determination of the vulnerable input points
should be performed to do this. The attacker will inject various payloads according to the context
that user input is used in. The application has 3 examples of the XSS, one of them stored XSS in
HTML context, the others are reflected XSS examples in different contexts (JavaScript context
and tag attribute context.) After determining the exploitation should be done to steal users’
cookies, to do that an attacker can open a server and inject a payload for stored XSS and prepare
links for reflected ones. The difference between those types of XSS, at stored one attacker does
not need to perform social engineering action so we can say it is a powerful vulnerability since it
will affect multiple users at the same time. For the reflected XSS attacker should force the victim
to click the link with social engineering skills. All the actions are performed during the
demonstration of this assignment
