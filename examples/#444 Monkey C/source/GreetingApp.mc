using Toybox.Application;
using Toybox.WatchUi;
using Toybox.System;

class GreetingApp extends Application.AppBase {
    function initialize() { AppBase.initialize(); }
    function getInitialView() {
        System.println("Hello, World!");
        return [new GreetingView()];
    }
}

class GreetingView extends WatchUi.View {
    function initialize() { View.initialize(); }
}
