########
Services
########

Introduction
============

A service is an application component instanciated only once by request while engine process client request.

Define a service
================

Fast Web Framework defines the base class ``Service`` that your service must herit from.
So it's possible to define the ``MyService`` like this:

.. code-block:: php

    <?php

    namespace Author\App;

    use Fastwf\Core\Engine\Service;

    class MyService extends Service {

        public function getHelloWorld() {
            // Access to the engine context using $this->context
            return 'Hello world!';
        }

    }


.. note::
    The default constructor expect an engine context, so it's possible to use this context anywhere in implemented methods.

Access to service
=================

Any service can be accessed anywhere the engine context is accessible using ``getService`` method.

.. note::
    While the service is not requested using ``getService`` the instance is not created, so each service can be used only when it's **realy
    required** by application.

The next example allows to access to the service from a custom ``RequestHandler``.

.. code-block:: php

    <?php

    namespace Author\App;

    use Fastwf\Core\Components\RequestHandler;

    class MyHandler extends RequestHandler {
    
        public function handle($request) {
            $service = $this->context->getService(MyService::class);

            // Do anything with $service
            // ...

            return $this->html(
                $service->getHelloWorld()
            );
        }
    
    }

.. warning::
    | Any service can be requested in any service constructor. It can result in circular dependencies.
    | For example ``A::class`` require ``B::class`` and ``B::class`` require ``A::class``.

    | To prevent this issue it's recommanded to:

    - access to the each service directly in the method.
    - If it's better to access to the service in constructor (performance reasons), control strictly service usage to prevent
      circular dependencies.

Register service
================

When a service require more than the engine context the ``getService`` cannot create the instance of the service. In that case, you must
register a service by provinding directly the service instance.

.. code-block:: php

    <?php

    namespace Author\App;

    use Fastwf\Core\Settings\ConfigurationSettings;

    class RootSettings implements RouteSettings {

        // ...

        public function configure($engine, $configuration) {
            $engine->registerService(
                MyService::class,
                new MyService($engine, 'other argument'),
            );
        }

    }

.. note::
    It's possible to register a service implementation class to be loaded when service interface is requested.

    | For example, the ``Engine`` register ``PhpSessionManager`` for ``SessionService`` interface using
    | ``registerService(SessionService::class, PhpSessionManager::class)`` call.
