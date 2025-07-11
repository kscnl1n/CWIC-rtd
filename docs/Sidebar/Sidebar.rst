Sidebar tools
=============
This page walks you through each tool on the sidebar to the far right of the CFDE workspace:

.. image:: _static/sidebar-images/sidebar1.png
   :alt: TACC create an account
   :align: center
   :width: 1200px

Upload
======

The upload bar allows you to upload datasets to the CFDE workspace. It is a convenient way to upload and access large datasets you need available on CFDE machines. 

For additional tutorials on running machine learning processes on these datasets, see **Creating Your Own Workflow.**



Uploading a dataset
---------------------

To upload a dataset, click on Upload. There should be four options available to you:

.. image:: _static/sidebar-images/upload1.png
   :alt: Upload screen
   :align: center
   :width: 1200px

- **Regular** – for uploading singular flat files (e.g., `.CSV`, `.TXT`, or `.FASTQ`)

  - You can choose to upload locally (from your machine) or remotely.
  - You can also try parsing/fetching the data from a web URL.

- **Composite** – for datasets made of multiple files but treated as one singular unit (e.g., `.bt2`, `.fa`)

  - These will also be immediately available under “Datasets”.

- **Collection** – for datasets composed of multiple files that need to be uploaded as separate datasets,
  such as in the case of pairs or lists (e.g., batch processing or sampling)

- **Rule-based upload** – for when you need advanced collections that are built dynamically with metadata in mind.

.. note::
    For more information about uploading Rule-based datasets to the CFDE Galaxy, look here:
    https://training.galaxyproject.org/training-material/topics/galaxy-interface/tutorials/upload-rules/tutorial.html

    For assistance troubleshooting data uploads, click the question mark in the upper right corner for community support.

To see a full tutorial for uploading a dataset and running a machine learning process on it, see **Creating Your Own Workflow.**

Tools
-----
This opens the preexisting library of NIH-created analysis tools. A majority of the data analysis will be done here.

.. image:: _static/sidebar-images/tools1.png
   :alt: Tools
   :width: 1200px

Because of the volume of tools in the CFDE galaxy interface, there is a search bar for ease of finding.

**Tool Interface**
Most tools in this interface will contain:
- Input datasets and parameters
- Help, citations, & metadata
- A run tool button, which will add output datasets to the history

**New Versions**
New versions of tools can be installed without removing old ones to ensure reproducibility.

**Adding Tools**
To add tools you may not see in the CWIC interface, go to the Galaxy Tool Shed: https://toolshed.g2.bx.psu.edu/
And ask your Galaxy Admin to install it for you. There is currently no way for users to add their own tools to the CFDE workspace.

Workflows
---------
**Workflows** are saved, pre-existing pipelines for data processing and analysis. Each step takes an input (dataset), sends it to a tool for one part of the processing pipeline, and then hands it off to the next tool for the next part. 

The CFDE galaxy workspace does not come with pre-installed workflows–when you open the workflow space, you should see that they are empty:
.. image:: _static/sidebar-images/workflow1.png
   :alt: Empty workflows page
   :align: center
   :width: 1200px

.. image:: _static/sidebar-images/workflow2.png
   :alt: Empty workflows page
   :align: center
   :width: 1200px

**My Workflows**
This is where you can find workflows you have installed into your Galaxy workspace. 

**Workflows Shared with Me**
This is where you can find workflows you have with other people. 

**Public Workflows**
Public workflows are ones publicly-available for anyone to download.
Because the CFDE galaxy is still in development, there are currently no workflows available for download.

Creating/Importing workflows
============================
To the far right of the Workflows tab, you should see two buttons create and import. These are currently the only way to get a workflow pipeline into the CFDE Galaxy portal.