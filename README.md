# IVORT B.R.I.G.H.T - Do Hadoop Everywhere

For those who wondering what's **B.R.I.G.H.T** in **IVORY**, it is **Beautiful, Resourceful, Insightful,Graphical, Hadoop Tool**.  

If you have ever come around a task of automating a Hadoop cluster, though it seems easy but there are a lot of inherent problems in it. Setting up a cluster seems a daunting task, and the thought of automating it gives sweat. Now imagine a person who wants to use the Hadoop's massive parallelism power but couldn't able to do so.
Can you guess the reason? Well! One being stuck with the configuration job.

After spending sometime on internet searching for a tool or library to setup a cluster is a painful task and those which are avaiable are too complex to configure and reuse, 
so all this lead to development of **HBS Library**.

**HBS** stands for **Hadoop Based Solutions Library** which provides easy to configure scripts and a complete **one click cluster setup**. It is a **Python 2.7** library, this version is programmed for **RHEL 6.4** (hence will work on **centOS 6** also).

But IVORY comes in **two parts** and second one being its **WebPortal**. Its web portal provides a **GUI based installation** system and a **Admin Portal** integrated with **Dashboard**  through which admin can **monitor live cluster status**, alongwith this he can **set quota**, kind of **scheduler** and many more cluster configuration parameters.

Now you must be wondering what's with **DO HADOOP EVERYWHERE ?** 
Well this is a one of our best features, we are using the concept of staging of files on a  
Apache Server after splitting or chunking of files. Here is one limitation which Apache Server is having, because it limits the size of file to be uploaded to the server.
So this is a feature to work upon and those who are interested, your contribution will be appreciated.

Well for now we are able to upload upto **200 – 250 MB** (I know its seems nothing when we are talking about Big Data, but still its gets thing in motion) easily through this mechanism. But this gives us flexibility of using Hadoop from anywhere in the network using Web Portal, which is what we were trying to achieve. **So its a little win  for  IVORY.** 


[a link](https://github.com/lordzuko/IVORY-B.R.I.G.H.T/Screenshots/Screenshot from 2015-10-11 12:10:36.png)
[a link](https://github.com/lordzuko/IVORY-B.R.I.G.H.T/Screenshots/Screenshot from 2015-10-11 12:10:48.png)

