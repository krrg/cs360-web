from flask import render_template

from config import app
from schedule import *

@app.route('/fall-2013/schedule')
def fall2013schedule():
    static = '/static/fall-2013/'
    term = '/fall-2013/'
    s = Schedule()

    s.week()

    d = s.day("September 4")
    d.lecture('Introduction','The Internet and its Architecture')
    d.reading('The Internet and its Architecture',static + 'lectures/the-internet-and-its-architecture.pdf')
    d.reading('Neal Stephenson on laying undersea fiber-optic cables','http://www.wired.com/wired/archive/4.12/ffglass.html')

    d = s.day("September 6")
    d.lecture('Introduction','The Internet and its Architecture, Lab Discussion')

    s.week()

    d = s.day("September 9")
    d.lecture('Systems','Socket Programming')
    d.reading('Socket Programming',static + 'lectures/socket-programming.pdf')

    d = s.day("September 11")
    d.lecture('Systems','Sockets and the OS')
    d.reading('Sockets and the OS',static + 'lectures/sockets-and-the-os.pdf')

    d = s.day("September 13")
    d.lecture('Concurrent Programming','Threads and the OS')
    d.reading('Threads and the OS',static+'lectures/threads-and-the-os.pdf')
    d.reading('Pthreads Tutorial','http://www.llnl.gov/computing/tutorials/pthreads/')

    s.week()

    d = s.day("September 16")
    d.lecture('Systems','Thread Pool Architecture, Lab Discussion')
    d.reading('Thread Pool Architecture',static+'lectures/thread-pool-architecture.pdf')

    d = s.day("September 17")
    d.assignment('Lab: Messaging Service',term + 'labs/messaging-service')

    d = s.day('September 18')
    d.lecture('Concurrent Programming','Thread Synchronization')
    d.reading('Thread Synchronization',static+'lectures/thread-synchronization.pdf')

    d = s.day('September 20')
    d.lecture('Concurrent Programming','Semaphores')
    d.reading('Semaphores',static+'lectures/semaphores.pdf')

    s.week()

    d = s.day('September 23')
    d.lecture('Concurrent Programming','Mutexes and Monitors')
    d.reading('Mutexes and Monitors',static+'lectures/mutexes-and-monitors.pdf')

    d = s.day('September 25')
    d.lecture('Concurrent Programming and Systems','Deadlock and UNIX Domain Sockets')
    d.reading('Deadlock',static+'lectures/deadlock.pdf')
    d.reading('UNIX Domain Sockets',static+'lectures/unix-domain-sockets.pdf')

    d = s.day('September 27')
    d.lecture('Concurrent Programming','Help With Lab 2')

    d = s.day('September 28')
    d.assignment('Lab: Threaded Messaging Service',term + 'labs/threaded-messaging-service')

    s.week()

    d = s.day('September 30')
    d.lecture('Systems','Introduction to Python Programming')
    d.reading('Introduction to Python',static+'lectures/introduction-to-python.pdf')
    d.reading('Python Documentation','http://www.python.org/')
    d.reading('Dive Into Python','http://www.diveinto.org/python3/')

    d = s.day('October 2')
    d.assignment('Exam | Weeks 1 - 4','')

    d = s.day('October 4')
    d.lecture('Systems','Python Networking and Threading, Lab Discussion')
    d.reading('Python Networking and Threading',static+'lectures/python-networking-and-threading.pdf')
    s.week()

    d = s.day('October 7')
    d.lecture('Systems','HTTP')
    d.reading('HTTP',static+'lectures/http.pdf')
  
    d = s.day('October 9')
    d.lecture('Systems','DNS')
    d.reading('DNS',static+'lectures/dns.pdf')

    d = s.day('October 11')
    d.lecture('No Class','')

    s.week()

    d = s.day('October 14')
    d.lecture('No Class','')

    d = s.day('October 15')
    d.assignment('Lab: Download Accelerator',term + 'labs/download-accelerator')

    d = s.day('October 16')
    d.lecture('Concurrent Programming','Python Socket Programming, Lab Discussion')
    d.reading('Python Socket Programming',static+'lectures/python-socket-programming.pdf')

    d = s.day('October 18')
    d.lecture('Systems','Event Driven Architecture, Lab Discussion')
    d.reading('Event-Driven Architecture',static+'lectures/event-driven-architecture.pdf')

    s.week()

    d = s.day('October 21')
    d.lecture('Systems','Web Proxies, Caching, and CDNs')
    d.reading('Web Proxies, Caching, and CDNs',static+'lectures/web-proxies-caching-and-cdns.pdf')
    d.reading("O'Reilly Web Caching Chapter",'http://www.oreilly.com/catalog/webcaching/chapter/ch05.html')


    d = s.day('October 23')
    d.lecture('Security','Network Security')
    d.reading('Network Security',static+'lectures/network-security.pdf')


    d = s.day('October 25')
    d.lecture('Security','Network Security')

    d = s.day('October 26')
    d.assignment('Lab: Web Server',term + 'labs/web-server')

    s.week()

    d = s.day('October 28')
    d.lecture('Performance Measurement','Queueing Theory')
    d.reading('Queueing Theory',static+'lectures/queueing-theory.pdf')

    d = s.day('October 30')
    d.lecture('Performance Measurement','Lab Discussion')

    d = s.day('November 1')
    d.lecture('Performance Measurement','Performance Measurement and Workload Models')
    d.reading('Performance Measurement',static+'/lectures/performance-measurement.pdf')
    d.assignment('Web Application Proposals','https://drive.google.com/folderview?id=0B09H8qp1t9fAdzgwaTg1aERpems&usp=sharing')

    s.week()

    d = s.day('November 4')
    d.lecture('Security','Network Security')

    d = s.day('November 6')
    d.lecture('Web Programming','Team Formation and Agile Development')

    d = s.day('November 7')
    d.assignment('Lab: Queueing Theory',term + '/labs/queueing-theory')

    d = s.day('November 8')
    d.lecture('Web Programming','Introduction to Web Frameworks and MVC')

    s.week()

    d = s.day('November 11')
    d.assignment('Exam | Weeks 5 - 10','')

    d = s.day('November 13')
    d.lecture('Web Programming','Web Design')

    d = s.day('November 15')
    d.assignment('Web Application Idea, Features, and Architecture','')

    d = s.day('November 16')
    d.lecture('Web Programming','Designing Relational Database Models')
    s.week()

    d = s.day('November 18')
    d.lecture('Web Programming','Designing Document Database Models')
    d.reading('Why MongoDB Is Awesome','http://www.slideshare.net/jnunemaker/why-mongodb-is-awesome')
    d.reading('Starbucks Does Not Use Two-Phase Commit','http://eaipatterns.com/ramblings/18_starbucks.html')

    d = s.day('November 20')
    d.lecture('Web Programming','Users and Authentication')

    d = s.day('November 22')
    d.lecture('Web Programming','Templates and CSS')
    d.reading('Javascript',static+'/lectures/javascript.pdf')

    d = s.day('November 23')
    d.assignment('Web Application Layout','')

    s.week()

    d = s.day('November 25')
    d.lecture('Web Programming','Javascript')

    d = s.day('November 26')
    d.lecture('Web Programming','Javascript')

    d = s.day('November 27')
    d.lecture('No Class','Thanksgiving Holiday')

    d = s.day('November 28')
    d.lecture('No Class','Thanksgiving Holiday')


    s.week()

    d = s.day('December 2')
    d.lecture('Web Programming','Web Services')
    d.reading('Interactive REST Tutorial','http://phprestsql.sourceforge.net/')
    d.reading('How I Explained REST to My Wife','http://tomayko.com/writings/rest-to-my-wife')
    d.reading('Google Custom Search API','https://developers.google.com/custom-search/v1/overview')
    d.reading('REST for Amazon','http://scripts.incutio.com/amazon/')
    d.reading('Microsoft Bing JSON Interface','http://msdn.microsoft.com/en-us/library/dd250846.aspx')
    d.assignment('Web Application Milestone','')

    d = s.day('December 4')
    d.lecture('Web Programming','Web Services')


    d = s.day('December 6')
    d.lecture('Security','Web Vulnerabilities')

    s.week()

    d = s.day('December 9')
    d.lecture('Security','Web Vulnerabilities')
    d.assignment('Web Application Milestone','')

    d = s.day('December 11')
    d.assignment('Exam | Weeks 11 - 15','')

    s.week()

    d = s.day('December 17')
    d.assignment('Lab: Web Application',term+'/labs/web-application')

    return render_template('fall-2013/schedule.html',active='schedule',
                           weeks=s.weeks)
