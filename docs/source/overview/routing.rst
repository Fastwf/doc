#############
Router system
#############

There are two different components to use to create your application routes:

- ``Fastwf\Core\Router\Mount``
- ``Fastwf\Core\Router\Route``

BaseRoute
=========

Constructor
-----------

``Mount`` and ``Route`` class extends from ``Fastwf\Core\Router\BaseRoute`` and the constructor require an array parameter which respect
the next definition:

+------------------------+------------+-----------------------------------------------------------------------------+
| Property               | Required   | Description                                                                 |
+========================+============+=============================================================================+
| ``path``               | yes        | The path of the route (must not starts with ``/``)                          |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``inputInterceptors``  | no         | A function factory or an array of ``Fastwf\Core\Components\InInterceptor``  |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``guards``             | no         | A function factory or an array of ``Fastwf\Core\Components\Guard``          |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``inputPipes``         | no         | A function factory or an array of ``Fastwf\Core\Components\InPipe``         |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``outputPipes``        | no         | A function factory or an array of ``Fastwf\Core\Components\OutPipe``        |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``outputInterceptors`` | no         | A function factory or an array of ``Fastwf\Core\Components\OutInterceptor`` |
+------------------------+------------+-----------------------------------------------------------------------------+
| ``name``               | no         | A uniq name accros all the application                                      |
+------------------------+------------+-----------------------------------------------------------------------------+

Lazy loading
------------

The ``Mount`` and ``Route`` class allows to declare it's component using a factory function.

.. code-block:: php

    <?php
    // Constructor(
    [
        'path' => 'user',
        'guards' => function () { return [
            new CustomGuard(),
        ];}
    ]
    // )

| The adventage in that case is that all ``Route`` and ``Mount`` components will be instanciated only when usage is required.
| So, when the engine need to access to the property, factory function will be executed and instances can be used.

Mount
=====

The ``Mount`` class require an array parameter which respect the ``BaseRoute`` keys and the next additionnal key:

+------------+------------+--------------------------------------------------------------+
| Property   | Required   | Description                                                  |
+============+============+==============================================================+
| ``routes`` | yes        | A function factory or an array of ``Route`` and/or ``Mount`` |
+------------+------------+--------------------------------------------------------------+

The ``Mount`` class allows to define routes and/or mount point and bind them on specific route path.

.. code-block:: php

    <?php
    // src/RootSettings.php

    namespace Author\App;

    use Fastwf\Core\Router\Mount;
    use Fastwf\Core\Router\Route;
    use Fastwf\Core\Settings\RouteSettings;

    use Author\App\HelloWorldHandler;

    class RootSettings implements RouteSettings
    {

        public function getRoutes($engine)
        {
            return [
                new Mount([
                    'path' => 'admin',
                    'routes' => [
                        // new Route([...]),
                        // ...
                    ],
                ]),
            ];
        }

    }

All routes and mount points defined in ``routes`` array will match the routes starting with ``/admin/`` prefix.

Route
=====

The ``Route`` class require an array parameter which respect the ``BaseRoute`` keys and the next additionnal keys:

+-------------+------------+-----------------------------------------------------------------------+
| Property    | Required   | Description                                                           |
+=============+============+=======================================================================+
| ``methods`` | yes        | An array of http methods ``["GET", "POST"]``                          |
+-------------+------------+-----------------------------------------------------------------------+
| ``handler`` | yes        | A function factory, an instance of ``RequestHandler`` or a class name |
+-------------+------------+-----------------------------------------------------------------------+

See :ref:`getting started RootSettings example<getting_started_settings>` for ``Route`` usage.

.. note::

    Use factory function when the constructor signature of the request handler is redefined. 

Router service
==============

The ``RouterService`` is responsible of route management and it's accessible from the engine context.

For common application development, this service is used to generate the url using route name.

.. code-block:: php

    <?php

    namespace Author\App;

    // use ...

    class CustomHandler extends RequestHandler {

        public function handle($request) {
            $url = $this->context->getService(RouterService::class)
                ->urlFor('route_name');
            
            // Perform operations with $url and return the HttpStreamResponse
            // ...
        }

    }
