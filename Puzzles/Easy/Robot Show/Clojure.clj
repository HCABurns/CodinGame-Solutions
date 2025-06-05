(ns Solution
  (:require [clojure.string :as str])
  (:gen-class))
  
(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (let [L (Integer/parseInt (read-line))
        N (Integer/parseInt (read-line))
        M (atom 9999)
        MX (atom 0)
        numbers (map #(Integer/parseInt %)
                     (filter #(not (empty? %))
                             (str/split (read-line) #" ")))]
    
    (doseq [b numbers]
      (swap! M min b)
      (swap! MX max b))
    
    (println (max @MX (- L @M)))))
