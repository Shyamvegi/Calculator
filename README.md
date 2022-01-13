# CloudSEK SDE Task
###### Using Django and Django Rest Framework

	> It consists the actual implementation of consumer_queue
    > It works on threading
    > It handles mutiple clients
    > Celery is overkill for this mini task
    > New payload can be added to consumer queue
    > This implementation creates Thread to compute answer for payload in consumer queue without any delay as it works on threading
    > Computes answer and insert it into database for every 10 seconds.

- Handles Mutiple clients at the same time
- followed PEP-8 Standard    
- All cases are handled
- can use docker

## clone the repository using

```sh
$ git clone "https://github.com/Shyamvegi/cloudSEK.git"
```


### set path to project folder

## Make and enter a virtaul env  

```sh
py -m venv nameOfenvfolder
```
```sh
.\envFOlder\Scripts\activate
```  

## Now run requirements file to install all dependencies 

```sh
(env)\pip install -r requirements.txt
```      

## migrate changes

```sh
(env)\ python manage.py makemigrations 
```
```sh
(env)\ python manage.py migrate 
```

## Runserver
```sh
(env)\ python manage.py runserver 
```
![](\Images\initialize.png)


## API END-PONTS  
  
@http://localhost:8000
![](\Images\routes.png)

### AdditonData Model which has number1 number2 and answer as fields
![](\Images\datamodel.png)


### Route("/") API Endpoint

-  / -- index shows successful message  
![](/Images/index.png)

-  consumer queue starts listenig to new tasks in background to reduce delay
![](/Images/consumerQueue.png)

### Route("/calculate/number1/number2") GET API Endpoint

-  calculate/number1/number2/  -- creates payload {number1,number2,unique_identifier}    
![](/Images/calculate.png)
![](/Images/tasksadded.png)
![](/Images/calculate2.png)

-  creates database entry for each new request to this end point

### Route("/get_answer/identifier")
-  get_answer/identifier/ ------- (get response for identifier) 

### Three Cases:

-  "identifier does not exist"  
![](/Images/case1.png)

-  "answer was not computed still in queue yet and shows message please wait"
![](/Images/case2.png)

-  "shows the calculated answer"
![](/Images/case3.png)

### Finished tasks in background by consumer queue thread
![](/Images/finishedtaks.png)
![](/Images/tasksadded2.png)