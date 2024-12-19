(ns Player
  (:gen-class))

(defn -main [& args]
  (while true
    (let [enemy1 (read) dist1 (read) enemy2 (read) dist2 (read)]
      ; Print closer enemy.
      (if (< dist1 dist2) (println enemy1) (println enemy2))
    )))
