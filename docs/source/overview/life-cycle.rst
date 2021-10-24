##########
Life cycle
##########

This framework is designed to works with php basic request system like apache mod_php or php-fpm.

Engine will be recreated at each client request and the next life cycle is executed:

.. mermaid::

    flowchart TD
        
        subgraph onConfigurationLoaded["Call onConfigurationLoaded()"]
            direction LR
            ConfigurationSettings --> configure["configure($engine, $configuration)"]
        end

        subgraph Runner["Runner->run($request, $match)"]
            direction TB
            InputInterceptors["InputInterceptors->start($context, $request)"] -->
            Guards["Guards->control($context, $request)"] -->
            InputPipes["InputPipes->in($context, $request)"] -->
            RequestHandler["RequestHandler->handle($request)"] -->
            OutputPipes["OutputPipes->out($context, $request, $response)"] -->
            OutputInterceptors["OutputInterceptors->end($context, $request, $response)"]
        end

        HttpRequest([HTTP Request]) -->
        run["Call run()"] --> 
        settings["Call getSettings()"] --> 
        config["Load configuration"] -->
        defaultServices["Register default services"] -->
        onConfigurationLoaded -->
        loadGlobalComponents["Load global route components"] -->
        registerEngineComponents["Register default components"] -->
        handleRequest["Call handleRequest()"] -->
        RouterServiceFindRoute["RouterService->findRoute()"] -->
        NotFoundException{"Catch NotFoundException"} -->|yes| NotFoundExceptionResponse["NotFoundException->getResponse()"]
        NotFoundExceptionResponse --> sendResponse["sendResponse($response)"]
        NotFoundException -->|no| Runner
        Runner --> Throwable{"Catch Throwable"}
        Throwable -->|no| sendResponse
        Throwable -->|yes| handleException["Call Runner->handleException()"]
        handleException -->
        sendResponse -->
        HttpResponse([HTTP Response])
