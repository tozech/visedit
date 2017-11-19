==============
 User stories
==============

Setting
-------

We have a figure, for instance a heatmap. This shows a visualisation of the data. This is typically a matplotlib figure including the controls for zooming, etc.
In addition, we have a table which shows the entire data. The table starts with the index. If the data is two dimension, this is a multi-index. The next columns contain the quantities/values. The figure typically shows only one or few of the value columns. The table can be edited.


Show data in table on click
===========================

If I click the data point in the figure, I want to see the corresponding row in the table.

Order the rows
--------------

* The clicked data point shall be first in the table.
* Neighboring cells shall be next.

  
Restrict table to selected zoom
===============================

If I zoom in the figure, the table shall only show the data shown by the figure.

Performance
-----------

* The update of the table shall not significantly slow down the zooming.

  
Update figure with table changes
================================

If I edit the table, I want the data in the figure to be updated.


Retrieve the changed table
==========================

I want to retrieve the changes I made to the table.


Edit all selected cells at once
===============================

I want to edit all selected cells at once.
