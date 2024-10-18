##########
ka_uts_com
##########

Overview
********

.. start short_desc

**Communication Utilities**

.. end short_desc

Installation
************
.. start installation

The package ``ka_uts_com`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: shell

	$ python -m pip install ka_uts_com

To install with ``conda``:

.. code-block:: shell

	$ conda install -c conda-forge ka_uts_com

.. end installation

This requires that the ``readme`` extra is installed:

.. code-block:: bash

	$ python -m pip install ka_uts_com[readme]

Configuration
*************

The Configuration of standard or personal (tenant specific) Package logging can be defined in Yaml Configuration Files in the data directory <Package Name>/data of the Package.

  .. logging-configuration-files-label:
  .. table:: *Logging Configuration Files*

   +--------+--------------------------------+----------------------------------+
   |Logging |Configuration                   |Description                       |
   |Type    +----------------+---------------+----------------------------------+
   |        |File            |Directory      |                                  |
   +========+================+=========+=====+==================================+
   |standard|log.standard.yml|ka_uts_com/data|the Python Logger compatible      |
   |        |                |               |standard Yaml configuraration file|
   |        |                |               |is used to define standard logging|
   +--------+----------------+               +----------------------------------+
   |personal|log.personal.yml|               |the Python Logger compatible      | 
   |        |                |               |personal Yaml configuration file  |
   |        |                |               |is used to define personal logging|
   +--------+----------------+---------------+----------------------------------+

Modules
*******

Classification
==============

The Modules of Package ``ka_uts_com`` could be classified in the follwing module classes:

#. **Base-Module**
#. **Utility-Modules**
#. **Special-Modules**

Base Modules
------------

  .. base-module-with-classes-label:
  .. table:: *Base Module with classes*

   +------+-------------+----------------------------------------+
   |Module|Type         |Static Classes                          |
   |      |             +-----------+----------------------------+
   |      |             |Name       |Description                 |
   +======+=============+===========+============================+
   |com   |Communication|App        |Setup Application Management|
   |      |             +-----------+----------------------------+
   |      |             |Com        |Communication Management    |
   |      |             +-----------+----------------------------+
   |      |             |Cfg        |Configuaration Management   |
   |      |             +-----------+----------------------------+
   |      |             |Exit       |Setup Exit Rules            |
   |      |             +-----------+----------------------------+
   |      |             |LogStandard|Standard Log Configuration  |
   |      |             +-----------+----------------------------+
   |      |             |LogPersonal|Peronal Log Configuration   |
   |      |             +-----------+----------------------------+
   |      |             |Mgo        |Mongo DB Interface          |
   +------+-------------+-----------+----------------------------+

Utility Modules
---------------

  .. utility-modules-with-classes-label:
  .. table:: *Utility Modules with classes*

   +------+-------------+----------------------------------------------+
   |Module|Type         |Static Classes                                |
   |      |             +---------+------------------------------------+
   |      |             |Name     |                                    |
   +======+=============+=========+====================================+
   |argv  |Commandline  |Argv     |Command Line Arguments Handling     |
   |      |Arguments    |         |                                    |
   +------+-------------+---------+------------------------------------+
   |deq   |Dictionary of|Deq      |Processing of Dictionaries which are| 
   |      |Equates      |         |created out of Parameter Equates    |
   +------+-------------+---------+------------------------------------+
   |fnc   |Function     |Fnc      |Function Managment                  |
   |      |Management   |         |(Show, Execution)                   |
   +------+-------------+---------+------------------------------------+
   |ioc   |I/O Control  |Yaml     |I/O Control for YAML files          |
   |      |             +---------+------------------------------------+
   |      |             |Jinja2   |I/O Control for Jinja2 files        |
   +------+-------------+---------+------------------------------------+
   |log   |Logging      |Log      |Log Management                      |
   +------+-------------+---------+------------------------------------+
   |pacmod|Package and  |Pacmod   |Package and Module Managment        |
   |      |Module       |         |                                    |
   +------+-------------+---------+------------------------------------+
   |str   |String       |Str      |String Processing                   |
   +------+-------------+---------+------------------------------------+
   |timer |Timer        |Timestamp|Timestamp Handling                  |
   |      |             +---------+------------------------------------+
   |      |             |Timer    |Timer Management                    |
   +------+-------------+---------+------------------------------------+

Special Modules
---------------

  .. special-modules-without-classes-label:
  .. table:: *Special-Modules without classes*

   +-----------+---------+------------------------------------------------+
   |Module     |Type     |Statements                                      |
   +===========+=========+================================================+
   |__init__   |Package  |Module with no Statements; the module is used to|
   |           |directory|mark the directory it contains as a package. A  | 
   |           |marker   |dummy Module enforces explicit imports and thus |
   |           |         |clear namespace use and call them with the dot  |
   |           |         |dot notation                                    |
   +-----------+---------+------------------------------------------------+
   |__version__|Version  |Assignment Statements for Version System        |
   |           |         |Variables                                       |
   +-----------+---------+------------------------------------------------+

Base Modul: com
===============

The Base Modul ``com`` contains the subsequent static classes

#. App
#. Com
#. Cfg
#. Exit
#. LogStandards
#. LogPersonal

static Class: App
-----------------

The static Class ``App`` contains the subsequent variables and methods

static Variables
^^^^^^^^^^^^^^^^

  .. app-static-variables-label:
  .. table:: *App static Variables*

   +---------------+-------+-------+---------------------+
   |static Variable|Type   |Default|Description          |
   +===============+=======+=======+=====================+
   |sw_init        |T_Bool |False  |initialisation switch|
   +---------------+-------+-------+---------------------+
   |httpmod        |T_Dic  |None   |http modus           |
   +---------------+-------+-------+---------------------+
   |sw_replace_keys|TN_Bool|False  |replace keys switch  |
   +---------------+-------+-------+---------------------+
   |keys           |TN_Arr |None   |Keys array           |
   +---------------+-------+-------+---------------------+
   |reqs           |T_Dic  |None   |Requests dictionary  |
   +---------------+-------+-------+---------------------+
   |app            |T_Dic  |None   |Appliction dictionary|
   +---------------+-------+-------+---------------------+

static Methods
^^^^^^^^^^^^^^

  .. app-static-methods-label:
  .. table:: *App static Methods*

   +-----------------------------------+---------------------------------------+
   |static Method                      |Parameter / Return Value               |
   +----+------------------------------+---------+------+----+-----------------+
   |Name|Description                   |Name     |Type  |P/RV|Description      |
   +====+==============================+=========+======+====+=================+
   |init|initialise static variables of|cls      |class |P   |current class    |
   |    |class if they are not allready+---------+------+----+-----------------+
   |    |initialized                   |\**kwargs|list  |P   |Keyword arguments|
   +----+------------------------------+---------+------+----+-----------------+
   |sh  |show (return) class           |cls      |class |P   |current class    |
   |    |                              +---------+------+----+-----------------+
   |    |                              |\**kwargs|list  |P   |Keyword arguments|
   |    |                              +---------+------+----+-----------------+
   |    |                              |log      |Logger|P   |                 |
   +----+------------------------------+---------+------+----+-----------------+

static Class: Com
-----------------

The static Class ``Com`` contains the subsequent variables and methods

static Variables
^^^^^^^^^^^^^^^^

  .. com-static-variables-label:
  .. table:: *Com static Variables*

   +-----------------------------------------------+
   |Static Variable                                |
   +-------+------+-------+------------------------+
   |Name   |Type  |Default|Description             |
   +=======+======+=======+========================+
   |cfg    |T_Dic |None   |Configuration dictionary|
   +-------+------+-------+------------------------+
   |log    |Logger|None   |logging Method          |
   +-------+------+-------+------------------------+
   |sw_init|T_Bool|False  |initialisation switch   |
   +-------+------+-------+------------------------+

static Methods
^^^^^^^^^^^^^^

  .. com-static-methods-label:
  .. table:: *Com static Methods*

   +-----------------------------------+--------------------------------------+
   |Static Method                      |Parameter / Return Value              |
   +----+------------------------------+---------+-----+----+-----------------+
   |Name|Description                   |Name     |Type |P/RV|Description      |
   +====+==============================+=========+=====+====+=================+
   |init|initialise static variables of|cls      |class|P   |current class    |
   |    |class if they are not allready+---------+-----+----+-----------------+
   |    |initialized                   |\**kwargs|list |P   |keyword arguments|
   +----+------------------------------+---------+-----+----+-----------------+

static Class: Cfg
-----------------

The static Class ``Cfg`` contains the subsequent variables and methods

static Methods
^^^^^^^^^^^^^^

  .. com-static-methods-label:
  .. table:: *Com static Methods*

   +-----------------------------------+--------------------------------+
   |static Method                      |Parameter / Return Value        |
   +----+------------------------------+------+------+----+-------------+
   |Name|Description                   |Name  |Type  |P/RV|Description  |
   +====+==============================+======+======+====+=============+
   |init|read pacmod yaml file into    |cls   |class |P   |current class|
   |    |dictionary variable _dic and  +------+------+----+-------------+
   |    |return _dic                   |pacmod|T_Dic |P   |pacmod       |
   |    |                              |      |      |    |dictionary   |
   |    |                              +------+------+----+-------------+
   |    |                              |_dic  |TN_Dic|RV  |             |
   +----+------------------------------+------+------+----+-------------+

static Class: Exit
------------------

  .. exit-static-variables-label:
  .. table:: *Exit static Variables*

   +----------------------------------------------------------------+
   |Static Variable                                                 |
   +--------------+-------+-------+---------------------------------+
   |Name          |Type   |Default|Description                      |
   +==============+=======+=======+=================================+
   |sw_critical   |T_Bool |False  |critical switch                  |
   +--------------+-------+-------+---------------------------------+
   |sw_stop       |T_Bool |False  |stop switch                      |
   +--------------+-------+-------+---------------------------------+
   |sw_interactive|T_Bool |False  |interactive switch               |
   +--------------+-------+-------+---------------------------------+

static Class: LogPersonal
-------------------------

The static Class ``LogPersonal`` contains the subsequent variables and methods

static Variables
^^^^^^^^^^^^^^^^

  .. logpersonal-static-variables-label:
  .. table:: *LogPersonal static Variables*

   +--------------------------------------------------------+
   |Static Variable                                         |
   +-------+------+-------+---------------------------------+
   |Name   |Type  |Default|Description                      |
   +=======+======+=======+=================================+
   |sw_init|T_Bool|False  |initialisation switch            |
   +-------+------+-------+---------------------------------+
   |cfg    |T_Dic |None   |Configuration dictionary         |
   +-------+------+-------+---------------------------------+
   |log    |Logger|None   |logging function                 |
   +-------+------+-------+---------------------------------+
   |logfile|str   |None   |Logfile name                     |
   +-------+------+-------+---------------------------------+

static Methods
^^^^^^^^^^^^^^

  .. logpersonal-static-method-label:
  .. table:: *LogPersonal static Methods*

   +----------------------------------+-----------------------------------------+
   |static Method                     |Parameter / Return Value                 |
   +---------+------------------------+---------+--------+----+-----------------+
   |Name     |Description             |Name     |Type    |P/RV|Description      |
   +=========+========================+=========+========+====+=================+
   |init     |Initialize static class |cls      |class   |P   |current class    |
   |         |variables if they are   +---------+--------+----+-----------------+
   |         |not allready initialized|\**kwargs|        |P   |keywords         |
   +---------+------------------------+---------+--------+----+-----------------+
   |read     |                        |pacmod   |T_Dic   |P   |pacmod           |
   |         |                        |         |        |P   |dictionary       |
   |         |                        +---------+--------+----+-----------------+
   |         |                        |filename |str     |P   |                 |
   |         |                        +---------+--------+----+-----------------+
   |         |                        |log_main |str     |RV  |                 |
   +---------+------------------------+---------+--------+----+-----------------+
   |set_level|set static variable log |sw_debug |bool    |P   |debug switch     |
   |         |level in log            |         |        |    |                 |
   |         |configuration handlers  |         |        |    |                 |
   +---------+------------------------+---------+--------+----+-----------------+
   |sh       |show static Logger      |cls      |class   |P   |current class    |
   |         |variable log            +---------+--------+----+-----------------+
   |         |                        |\**kwargs|        |P   |keyword arguments|
   |         |                        +---------+--------+----+-----------------+
   |         |                        |log      |Logger  |P   |                 |
   +---------+------------------------+---------+--------+----+-----------------+
   
static Class: LogStandard
-------------------------

The static Class ``LogStandard`` contains the subsequent variables and methods

static Variables
^^^^^^^^^^^^^^^^

  .. logstandard-static-variables-label:
  .. table:: *LogStandard static Variables*

   +---------------------------------------------------------+
   |Static Variable                                          |
   +-------+-------+-------+---------------------------------+
   |Name   |Type   |Default|Description                      |
   +=======+=======+=======+=================================+
   |sw_init|T_Bool |False  |initialisation switch            |
   +-------+-------+-------+---------------------------------+
   |cfg    |T_Dic  |None   |Configuration dictionary         |
   +-------+-------+-------+---------------------------------+
   |log    |Logger |None   |logging function                 |
   +-------+-------+-------+---------------------------------+
   |logfile|str    |None   |Logfile name                     |
   +-------+-------+-------+---------------------------------+

static Methods
^^^^^^^^^^^^^^

  .. logstandard-static-methods-label:
  .. table:: *LogStandard static Methods*

   +-----------------------------------+-------------------------------------+
   |static Method                      |Parameter / Return Value             |
   +---------+-------------------------+---------+--------+----+-------------+
   |Name     |Description              |Name     |Type    |P/RV|Description  |
   +=========+=========================+=========+========+====+=============+
   |read     |Read log file path with  |pacmod   |T_Dic   |P   |             |
   |         |jinja2 I/O utility       +---------+--------+----+-------------+
   |         |                         |filename |str     |P   |             |
   |         |                         +---------+--------+----+-------------+
   |         |                         |log_main |str     |RV  |             |
   +---------+-------------------------+---------+--------+----+-------------+
   |set_level|Set static variable log  |sw_debug |bool    |P   |             |
   |         |level in log             |         |        |    |             |
   |         |configuration handlers   |         |        |    |             |
   +---------+-------------------------+---------+--------+----+-------------+
   |init     |initialise static        |cls      |class   |P   |current class|
   |         |variables of class if    +---------+--------+----+-------------+
   |         |if they are not allready |\**kwargs|        |P   |             |
   |         |initialized              |         |        |    |             |
   +---------+-------------------------+---------+--------+----+-------------+
   |sh       |show static Logger       |cls      |class   |P   |current class|
   |         |variable                 +---------+--------+----+-------------+
   |         |                         |\**kwargs|        |P   |Keywords     |
   |         |                         +---------+--------+----+-------------+
   |         |                         |log      |Logger  |RV  |             |
   +---------+-------------------------+---------+--------+----+-------------+

Utility Modul: argv
===================

The Modul ``argv`` contains the subsequent static classes.

  .. argv-static-classes-label:
  .. table:: *argv static Classes*

   +-----------------+------------------------------------------------+
   |Module           |Static Classes                                  |
   +----+------------+-----------+------------------------------------+
   |Name|Type        |Name       |Description                         |
   +====+============+===========+====================================+
   |argv|CLI Argument|Argv       |Manage Commandline Arguments as     |
   |    |Management  |           |Equate-Strings                      |
   +----+------------+-----------+------------------------------------+

static Class: Argv
------------------

The static Class ``Argv`` contains the subsequent variables and methods

static variables
^^^^^^^^^^^^^^^^

  .. argv-static-variables-label:
  .. table:: *argv static Variables*

   +------------------------------------------------------------------+
   |Static Variable                                                   |
   +---------------+--------+-------+---------------------------------+
   |Name           |Type    |Default|Description                      |
   +===============+========+=======+=================================+
   |sw_init        |T_Bool  |False  |initialisation switch            |
   +---------------+--------+-------+---------------------------------+
   |httpmod        |T_Dic   |None   |http modus                       |
   +---------------+--------+-------+---------------------------------+
   |sw_replace_keys|TN_Bool |False  |replace keys switch              |
   +---------------+--------+-------+---------------------------------+
   |keys           |TN_Arr  |None   |Keys array                       |
   +---------------+--------+-------+---------------------------------+
   |reqs           |T_Dic   |None   |Requests dictionary              |
   +---------------+--------+-------+---------------------------------+
   |app            |T_Dic   |None   |Appliction dictionary            |
   +---------------+--------+-------+---------------------------------+

static Methods
^^^^^^^^^^^^^^

  .. argv-static-method-label:
  .. table:: *argv static Methods*

   +--------------------------------+-------------------------------------+
   |static Method                   |Parameter / Return Value             |
   +-------------+------------------+---------+--------+----+-------------+
   |Name         |Description       |Name     |Type    |P/RV|Description  |
   +=============+==================+=========+========+====+=============+
   |set_by_pacmod|set current pacmod|d_eq     |T_Dic   |P   |Dictionary of|
   |             |dictionary        |         |        |    |equates      |
   |             |                  +---------+--------+----+-------------+
   |             |                  |root_cls |Class   |P   |Root Class   |
   +-------------+------------------+---------+--------+----+-------------+
   |set_d_eq     |set current pacmod|d_eq     |T_Dic   |P   |Dictionary of|
   |             |dictionary        |         |        |    |equates      |
   |             |                  +---------+--------+----+-------------+
   |             |                  |root_cls |Class   |P   |Root Class   |
   +-------------+------------------+---------+--------+----+-------------+

static Class: Aeq
-----------------

The static Class ``Aeq`` contains the subsequent variables and methods

static Methods
^^^^^^^^^^^^^^

  .. argv-static-method-label:
  .. table:: *argv static Methods*

   +--------------------------------+------------------------------------------------+
   |static Method                   |Parameter / Return Value                        |
   +--------+-----------------------+-------------+------+----+----------------------+
   |Name    |Description            |Name         |Type  |P/RV|Description           | 
   +========+=======================+=============+======+====+======================+
   |sh_value|Show value of equate   |cls          |class |P   |current class         |
   |        |string provided by     +-------------+------+----+----------------------+
   |        |single command line    |key          |str   |P   |Key of equate string  |
   |        |argument               +-------------+------+----+----------------------+
   |        |                       |value        |Any   |P   |Value of equate string|
   |        |                       +-------------+------+----+----------------------+
   |        |                       |d_valid_parms|TN_Dic|P   |Dictionary of valid   |
   |        |                       |             |      |    |keys (parameters)     |
   |        |                       +-------------+------+----+----------------------+
   |        |                       |value        |Any   |RV  |converted Value of the|
   |        |                       |             |      |    |equate-string         |
   |        |                       |             |      |    |according Value type  |
   |        |                       |             |      |    |d_valid_parms         |
   +--------+-----------------------+-------------+------+----+----------------------+
   |sh_d_eq |Show Dictionary created|cls          |class |P   |current class         |
   |        |by parsing array of    +-------------+------+----+----------------------+
   |        |equate-strings provided|a_s_eq       |T_Arr |P   |array of equate       |
   |        |by command line        |             |      |    |strings               |
   |        |arguments              +-------------+------+----+----------------------+
   |        |                       |d_valid_parms|TN_Dic|P   |Dictionary of valid   |
   |        |                       |             |      |    |parameter-keys        |
   |        |                       +-------------+------+----+----------------------+
   |        |                       |d_eq         |TN_Dic|RV  |Dictiony of parameter |
   |        |                       |             |      |    |key, values           |
   +--------+-----------------------+-------------+------+----+----------------------+

Utility Modul: ioc
==================

The Module ``ioc`` provides Classes with I/O Control methods for files;
it contains the subsequent classes classified by the supported file type.


  .. ioc-static-classes-label:
  .. table:: *ioc static Classes*

   +----------------+--------------------------------------------+
   |Module          |Static Classes                              |
   +----+-----------+-------+------------------------------------+
   |Name|Type       |Name   |Description                         |
   +====+===========+=======+====================================+
   |ioc |I/O Control|Jinja2 |I/O Control for Jinja2 files        |
   |    |           +-------+------------------------------------+
   |    |           |Yaml   |MI/O Control for Yaml files         |
   +----+-----------+-------+------------------------------------+

static Class: Jinja2
--------------------

The static Class ``Jinja2`` provides I/O Control methods for Jinja2 files;
it contains the subsequent variables and methods.

static Methods
^^^^^^^^^^^^^^

  .. jinja2-static-methods-label:
  .. table:: *Jinja2 static Methods*

   +--------------------------------+-------------------------------------+
   |static Method                   |Parameter / Return Value             |
   +-------------+------------------+---------+------+----+---------------+
   |Name         |Description       |Name     |Type  |P/RV|Description    |
   +=============+==================+=========+======+====+===============+
   |read         |Read log file path|pacmod   |TN_Dic|P   |               |
   |             |with jinja        +---------+------+----+---------------+
   |             |                  |filename |str   |P   |               |
   |             |                  +---------+------+----+---------------+
   |             |                  |         |TN_Any|RV  |no return value|
   +-------------+------------------+---------+------+----+---------------+
   |read_template|Read log file path|pacmod   |TN_Dic|P   |               |
   |             |with jinja2       +---------+------+----+---------------+
   |             |                  |filename |TN_Any|P   |               |
   |             |                  +---------+------+----+---------------+
   |             |                  |         |TN_Any|RV  |no return value|
   +-------------+------------------+---------+------+----+---------------+

static Class: Yaml
------------------

The static Class ``Yaml`` provides I/O Control methods for Yaml files;
it contains the subsequent variables and methods

static Methods
^^^^^^^^^^^^^^

  .. yaml-static-methods-label:
  .. table:: *Yaml static Methods*

   +-------------------------------+-------------------------------------+
   |static Method                  |Parameter / Return Value             |
   +----+--------------------------+---------+------+----+---------------+
   |Name|Description               |Name     |Type  |P/RV|Description    |
   +====+==========================+=========+======+====+===============+
   |load|Load yaml string into any |string   |str   |P   |               |
   |    |object using yaml loader; +---------+------+----+---------------+
   |    |default is yaml.safeloader|loader   |str   |P   |               |
   |    |                          +---------+------+----+---------------+
   |    |                          |         |TN_Any|RV  |no return value|
   +----+--------------------------+---------+------+----+---------------+
   |read|Read yaml file path into  |path     |str   |P   |               |
   |    |any object using yaml     +---------+------+----+---------------+
   |    |loader; default loader is |loader   |str   |P   |               |
   |    |yaml.safeloader           +---------+------+----+---------------+
   |    |                          |         |TN_Any|RV  |no return value|
   +----+--------------------------+---------+------+----+---------------+

Utility Modul: log
==================

The Module ``log`` provides Classes with I/O Control methods for log files;
it contains the following static classes.


  .. log-static-classes-label:
  .. table:: *log static Classes*

   +---------------------+------------------------------------------+
   |Module               |Static Classes                            |
   +----+----------------+-----+------------------------------------+
   |Name|Type            |Name |Description                         |
   +====+================+=====+====================================+
   |log |Logging         |Log  |Log Management                      |
   +----+----------------+-----+------------------------------------+

static Class: Log
-----------------

static Variables
^^^^^^^^^^^^^^^^

  .. log-static-variables-label:
  .. table:: *Log static Variables*

   +--------------------------------------------------------+
   |Static Variable                                         |
   +-------+------+-------+---------------------------------+
   |Name   |Type  |Default|Description                      |
   +=======+======+=======+=================================+
   |sw_init|T_Bool|False  |initialisation switch            |
   +-------+------+-------+---------------------------------+
   |cfg    |T_Dic |None   |Configuration dictionary         |
   +-------+------+-------+---------------------------------+
   |log    |Logger|None   |logging function                 |
   +-------+------+-------+---------------------------------+

static Sub-Classes
^^^^^^^^^^^^^^^^^^

The Class ``Log`` contains the following static sub-classes.

  .. log-static-sub-classes-label:
  .. table:: *log static Sub-Classes*

   +----------------------------------------------+
   |static Sub-Class                              |
   +----------------------------------------------+
   |Name|Type  |Description                       |
   +====+======++=================================+
   |Eq  |      |Log Management for Equate Messages|
   +----+------+----------------------------------+

static Methods
""""""""""""""

  .. log-methods-label:
  .. table:: Log Methods*

   +---------------------------+---------------------------------------+
   |static Method              |Parameter / Return Value               |
   +-------+-------------------+---------+--------+----+---------------+
   |Name   |Description        |Name     |Type    |P/RV|Description    |
   +=======+===================+=========+========+====+===============+
   |debug  |Log debug message  |cls      |class   |P   |current class  |
   |       |                   +---------+--------+----+---------------+
   |       |                   |key      |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |value    |Any     |P   |               |
   +-------+-------------------+---------+--------+----+---------------+
   |error  |Log error message  |cls      |class   |P   |current class  |
   |       |                   +---------+--------+----+---------------+
   |       |                   |key      |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |value    |Any     |P   |               |
   +-------+-------------------+---------+--------+----+---------------+
   |info   |Log info message   |cls      |class   |P   |current class  |
   |       |                   +---------+--------+----+---------------+
   |       |                   |key      |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |value    |Any     |P   |               |
   +-------+-------------------+---------+--------+----+---------------+
   |warning|Log warning message|cls      |class   |P   |current class  |
   |       |                   +---------+--------+----+---------------+
   |       |                   |key      |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |value    |Any     |P   |               |
   +-------+-------------------+---------+--------+----+---------------+
   |sh     |show equate message|key      |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |value    |Any     |P   |               |
   |       |                   +---------+--------+----+---------------+
   |       |                   |         |str     |RV  |no return value|
   +-------+-------------------+---------+--------+----+---------------+

static Methods
^^^^^^^^^^^^^^

  .. log-methods-label:
  .. table:: Log Methods*

   +-------------------------------+-----------------------------------------+
   |Static Method                  |Parameter / Return Value                 |
   +-------+-----------------------+---------+--------+----+-----------------+
   |Name   |Description            |Name     |Type    |P/RV|Description      |
   +=======+=======================+=========+========+====+=================+
   |debug  |Log debug message      |\*args   |list    |P   |arguments        |
   |       |                       +---------+--------+----+-----------------+
   |       |                       |\**kwargs|list    |P   |keyword arguments|
   +-------+-----------------------+---------+--------+----+-----------------+
   |error  |Log error message      |\*args   |list    |P   |arguments        |
   |       |                       +---------+--------+----+-----------------+
   |       |                       |\**kwargs|list    |P   |keyword arguments|
   +-------+-----------------------+---------+--------+----+-----------------+
   |info   |Log info message       |\*args   |list    |P   |arguments        |
   |       |                       +---------+--------+----+-----------------+
   |       |                       |\**kwargs|list    |P   |keyword arguments|
   +-------+-----------------------+---------+--------+----+-----------------+
   |warning|Log warning message    |\*args   |list    |P   |arguments        |
   |       |                       +---------+--------+----+-----------------+
   |       |                       |\**kwargs|list    |P   |keyword arguments|
   +-------+-----------------------+---------+--------+----+-----------------+

Utility Modul: pacmod
=====================

The Modul ``pacmod`` contains the following static classes.

  .. package-module-management-classes-label:
  .. table:: *Package Module Management Classes*

   +---------------------+-------------------------------------------+
   |Module               |Static Classes                             |
   +------+--------------+------+------------------------------------+
   |Name  |Type          |Name  |Description                         |
   +======+==============+======+====================================+
   |Pacmod|Package Module|Pacmod|Package Module Management           |
   +------+--------------+------+------------------------------------+

static Class: Pacmod
--------------------

static Methods
^^^^^^^^^^^^^^

  .. pacmod-static-methods-label:
  .. table:: Pacmod static Methods*

   +--------------------------------------------+---------------------------------------+
   |Static Method                               |Parameter / Return Value               |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |Name             |Description               |Name     |Type  |P/RV|Description      |
   +=================+==========================+=========+======+====+=================+
   |sh_d_pacmod      |create and show (return)  |root_cls |class |P   |root class       |
   |                 |pacmod dictionary         +---------+------+----+-----------------+
   |                 |                          |tenant   |Any   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |         |T_Dic |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_path_cfg_yaml |show pacmod file path of  |pacmod   |T_Dic |P   |                 |
   |                 |the yaml file             +---------+------+----+-----------------+
   |                 |<pacmod module>.yaml      |         |str   |RV  |no return value  |
   |                 |in the data directory of  |         |      |    |                 |
   |                 |the current module of the |         |      |    |                 |
   |                 |current package           |         |      |    |                 |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_path_keys_yaml|show pacmod file path type|pacmod   |T_Dic |P   |                 |
   |                 |for the yaml file keys.yml+---------+------+----+-----------------+
   |                 |keys.yml in the data      |type\_   |str   |P   |                 |
   |                 |directory of the current  +---------+------+----+-----------------+
   |                 |module of the current     |         |str   |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_pacmod_type   |show pacmod type directory|pacmod   |T_Dic |P   |                 |
   |                 |path                      +---------+------+----+-----------------+
   |                 |                          |type\_   |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |         |str   |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_file_path     |show pacmod file path     |cls      |class |P   |current class    |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |pacmod   |T_Dic |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |type\_   |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |suffix   |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |pid      |Any   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |ts       |Any   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |\**kwargs|      |P   |keyword arguments|
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |         |str   |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_pattern       |show pacmod file path     |pacmod   |T_Dic |P   |                 |
   |                 |pattern                   +---------+------+----+-----------------+
   |                 |                          |type\_   |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |suffix   |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |\**kwargs|      |P   |keyword arguments|
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |         |str   |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_path_cfg_log  |show file path of log     |pacmod   |TN_Dic|P   |                 |     
   |                 |configuration file        +---------+------+----+-----------------+
   |                 |                          |filename |str   |P   |                 |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |         |str   |RV  |no return value  |
   +-----------------+--------------------------+---------+------+----+-----------------+
   |sh_d_pacmod      |show pacmod dictionary    |cls      |class |P   |current class    |
   |                 |                          +---------+------+----+-----------------+
   |                 |                          |\**kwargs|      |P   |keyword arguments|
   +-----------------+--------------------------+---------+------+----+-----------------+

Utility Modul: timer
====================

The Modul ``timer`` contains the following static classes.

  .. timer-static-classes-label:
  .. table:: *timer static Classes*

   +-----------+----------------------------------------------+
   |Module     |Static Classes                                |
   +-----+-----+---------+------------------------------------+
   |Name |Type |Name     |Description                         |
   +=====+=====+=========+====================================+
   |timer|Timer|Timestamp|Timestamop class                    |
   |     |     +---------+------------------------------------+
   |     |     |Timer    |Timer class                         |
   +-----+-----+---------+------------------------------------+

static Class: Timer
-------------------

static Variables
^^^^^^^^^^^^^^^^

  .. timer-static-variables-label:
  .. table:: *Timer static Variables*

   +---------------------------------------------------------+
   |Static Variable                                          |
   +-------+-------+-------+---------------------------------+
   |Name   |Type   |Default|Description                      |
   +=======+=======+=======+=================================+
   |sw_init|T_Bool |False  |initialisation switch            |
   +-------+-------+-------+---------------------------------+
   |cfg    |T_Dic  |None   |Configuration dictionary         |
   +-------+-------+-------+---------------------------------+
   |log    |Logger |None   |logging function                 |
   +-------+-------+-------+---------------------------------+

static Methods
^^^^^^^^^^^^^^

  .. timer-static-methods-label:
  .. table:: Timer static Methods*

   +---------------------------------------+--------------------------------------+
   |static Method                          |Parameter / Return Value              |
   +---------+-----------------------------+---------+-----+----+-----------------+
   |Name     |Description                  |Name     |Type |P/RV|Description      |
   +=========+=============================+=========+=====+====+=================+
   |read     |Read log file path with      |pacmod   |T_Dic|P   |                 |
   |         |jinja2                       +---------+-----+----+-----------------+
   |         |                             |filename |str  |P   |                 |
   |         |                             +---------+-----+----+-----------------+
   |         |                             |log_main |str  |RV  |                 |
   +---------+-----------------------------+---------+-----+----+-----------------+
   |set_level|Set static variable log level|sw_debug |bool |P   |                 |
   |         |in log configuration handlers|         |     |    |                 |
   +---------+-----------------------------+---------+-----+----+-----------------+
   |init     |initialise static variables  |cls      |class|P   |current class    |
   |         |if they are not allready     +---------+-----+----+-----------------+
   |         |initialized                  |\**kwargs|     |P   |keyword arguments|
   +---------+-----------------------------+---------+-----+----+-----------------+
   |sh       |show static variable log     |cls      |class|P   |                 |
   |         |                             +---------+-----+----+-----------------+
   |         |                             |\**kwargs|     |P   |keyword arguments|
   +---------+-----------------------------+---------+-----+----+-----------------+

Special Modul: __version__
==========================

The Modul ``__version__`` contains no classes, but assignment statements for
system variables used by versioning.

  .. modul-__version__-system-variables:
  .. table:: *__version_ System Variables*

   +---------------+-----------------------------------------+
   |System Variable|Example                                  |
   +===============+=========================================+
   |__title__      |'ka_uts_com'                             |
   +---------------+-----------------------------------------+
   |__description__|'Communication Area Utilities.'          |
   +---------------+-----------------------------------------+
   |__url__        |'https://ka-com.readthedocs.io/en/latest'|
   +---------------+-----------------------------------------+
   |__version___   |'2023.2.2'                               |
   +---------------+-----------------------------------------+
   |__build__      |0x022200                                 |
   +---------------+-----------------------------------------+
   |__author_email_|'Bernd Stroehle'                         |
   +---------------+-----------------------------------------+
   |__license__    |'Apache-2.0'                             |
   +---------------+-----------------------------------------+
   |__copyright__  |'Copyright 2023 bs29'                    |
   +---------------+-----------------------------------------+
   |__cake__       |u'\u2728 \U0001f370 \u2728'              |
   +---------------+-----------------------------------------+

Module Data
===========

   +-------------------+-------------------------------------+
   |System Variable    |Description                          |
   +===================+=====================================+
   |log.main.tenant.yml|'ka_uts_com'                         |
   |__copyright__      |'Copyright 2023 bs29'                |
   +-------------------+-------------------------------------+

Appendix
========

.. contents:: **Table of Content**
