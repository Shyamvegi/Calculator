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

-  **_/_ -- index shows successful message**

![](/Images/index.png)

-  **consumer queue starts listenig to new tasks in background to reduce delay**

![](/Images/consumerQueue.png)

### Route("/calculate/number1/number2") GET API Endpoint

-  **_calculate/number1/number2/_  -- creates payload {number1,number2,unique_
identifier}**    

![](/Images/calculate.png)

![](/Images/tasksadded.png)

![](/Images/calculate2.png)

-  creates database entry for each new request to this end point

### Route("/get_answer/identifier")

-  **_get_answer/identifier/_ ------- (get response for identifier)** 

### Three Cases:

-  **"status : 404 --- _identifier does not exist_"** 

![](/Images/case1.png)

-  **status : 200 --- _answer was not computed still in queue yet and shows message please wait_**

![](/Images/case2.png)

-  **status : 200 --- _shows the calculated answer_**

![](/Images/case3.png)

### Finished tasks in background by consumer queue thread
![](/Images/finishedtasks.png)
![](/Images/tasksadded2.png)