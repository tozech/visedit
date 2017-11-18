====================
 qgrid installation
====================

Latest 1.

.. code : bash

   conda create -n qgrid python=3.6
   source activate qgrid
   pip install gqrid --pre
   jupyter nbextension enable --py widgetsnbextension --sys-prefix
   jupyter nbextension enable --py --sys-prefix qgrid

https://github.com/quantopian/qgrid
https://ipywidgets.readthedocs.io/en/latest/user_install.html

   
For qgrid 0.3.3
===============

.. code : bash

   conda create -n visedit python=3.6
   source activate visedit
   pip install notebook==5.0.0
   pip install ipywidgets==6.0.0
   jupyter nbextension enable --py widgetsnbextension --sys-prefix
   pip install qgrid==0.3.3
