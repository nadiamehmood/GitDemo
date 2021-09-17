# download jenkin from this url:- (https://www.jenkins.io/download/)
# select (generic java package .war) from this url
# open cmd prompt and navigate to the path where your jenkins located (C:\Program Files)
# jenkin is not a tool its starts in your own local server
# to start jenkin we run the following command:
# java -jar jenkins.war -httpPort=9090   # we are asking the java to open the jar, we can use 9090 OR 8080
#


##########################################
# download 'jdk 8' -> windows x64
# set the "JAVA_HOME" and "JRE_HOME" path from environment variables setting
# set "PATH" as bin like this "C:\Program Files\Java\jdk1.8.0_301\bin;C:\Program Files\Java\jre1.8.0_301\bin"
# download jenkins by clicking the "windows" option
# double click on jenkins exe file
# click next and complete the download process
# open windows tab and open "localhost:8080"
# to find the administrator password, go to 'C:' driver open jenkins folder from program files folder. open jenkins.err file and copy the password
# now, you have logged in to the jenkins account.
# for creating new job:- click on 'new item' and add name and click on 'freestype project' and press 'ok'
# now, click on 'Advanced' button and click on checkbox 'use custom workspace'
# copy the path of your project and paste it in use custom workspace text field
# now, click on 'add Build setup' button on "Build" section
# type command:-
# cd tests # it moved to the tests folder
# now move to the "reports" folder to create a report of your test case
# py.test --browser_name chrome --html=$WORKSPACE/reports/reports.html     # WORKSPACE is the env variable offered by jenkins
# click on 'save' button
# now the job has been created successfully
# ------------------------
# now from dashboard click on your project
# click on 'build now' button
# cd tests
# python -m pytest --browser_name chrome --html=$WORKSPACE/reports/reports.html
# python location:- C:\Users\Southville\AppData\Local\Programs\Python\Python38-32\Scripts