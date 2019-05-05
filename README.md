# EECS341 Final Project Report 

Prepared by: Yihe Guo, Cameron Hochberg, Melody Li, Yue Shu
May 5, 2019

## Introduction

**FitHub** is a virtual gym located on the 4th floor of Veale Center and is open to all CWRU student and faculty. Customers need to register for a membership online before going to the gym. There are five levels of memberships with different sign-up prices: `Bronze`, `Silver`, `Gold`, `Platinum`, and `Diamond`. We are designing websites connecting to the gym database, which allow both users and managers to retrieve and update their information, register in the classes being taught at Veale, or become a course tutor themselves.

## Usage
### Operating Environment

The `FitHub` application is developed under the `django` framework, so as long as the operating environment supports version `Django 2.0.6` or above, the user would be able to run the web server as a localhost. 

### Installation 

Before deploying all the required packages, please make sure you have `Python 3.6.1` or above installed. All the required packages are specified in `requirements.txt`. We have also implemented a shell script `installReq.sh` to do the work for you, so under `Linux` enviroment, just type the below command in your terminal to have the packages installed:

```

$ ./installReq.sh
```

Once you have successfully installed `Django 2.0.6` and all the other requirements, just type the following command in your terminal to run the `FitHub` application: 

```

$ python3 manage.py runserver
```

Now you should be able to land on our welcome page by typing out your localhost IP and default port number `127.0.0.1:8000` in your web browser and start your journey with `FitHub`!