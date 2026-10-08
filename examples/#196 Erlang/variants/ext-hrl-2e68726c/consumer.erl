-module(consumer).
-export([main/0]).
-include("hello.hrl").
main() -> io:format("~s~n", [?CORPUS_GREETING]).
