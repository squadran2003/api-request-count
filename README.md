# api-request-count
A django app that helps you keep count of the
number of requests a user make to your route.

# inspiration
I got this idea when working on our dashboard
at work where I needed to know who and at what
time were making requests to our api. As I Could'nt
find an app that did this I wrote this app

# Getting Started
1)Just drop the apiRequestCount folder into you django app.

2) add the app to your installed apps in settings.py.

3)Run migrations.

4)Import the decorator requestCount from the apps decorators file, see example below

```python

from apiRequestCount.decorators import requestCount


class CountView(APIView):
    @requestCount
    def get(self, request, **kwargs):
        """test view1"""

        return JsonResponse(["All ok"],safe=False,status=status.HTTP_200_OK)

class CountView2(APIView):
    @requestCount
    def get(self, request, **kwargs):
        """test view2"""

        return JsonResponse(["All ok"],safe=False,status=status.HTTP_200_OK)



```
you must had a doc string with the view name, this value is stored as
the view name in the ApiRequest table. In the above examples every request
coming in will be logged with the user, apiview("test view1"), and datetime.
Goes without saying that these views will only work if they are locked
down or only accessible by logged in users.


# Prerequisites
djangorestframework
Django >= 2.1.7

# Running the tests
add the apiRequest app urls to the site wide urls and
then run

```python

    python manage.py test apiRequestCount


```

# Contributing

Developers of all skill levels welcome, if
you have an idea to improve the app
create a branch and then a pull request

