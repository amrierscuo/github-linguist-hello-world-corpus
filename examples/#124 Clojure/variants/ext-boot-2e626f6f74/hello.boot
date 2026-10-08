(set-env! :resource-paths #{"src"})
(deftask hello [] (with-pass-thru _ (println "Hello, World!")))
