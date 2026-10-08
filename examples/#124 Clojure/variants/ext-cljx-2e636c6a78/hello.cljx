(ns corpus.greeting)
(def greeting (str "Hello, " "World!"))
#+clj (println greeting)
#+cljs (js/console.log greeting)
