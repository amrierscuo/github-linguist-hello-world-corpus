-module(greeting_app).
-behaviour(application).
-export([start/2, stop/1]).
start(_Type, _Args) ->
 io:format("Hello, World!~n"),
 {ok, spawn(fun wait/0)}.
stop(_State) -> ok.
wait() -> receive stop -> ok end.
