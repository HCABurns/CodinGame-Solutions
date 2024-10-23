(ns Player
  (:require [clojure.string :as str])
  (:gen-class))

(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (let [; the number of points used to draw the surface of Mars.
        surfaceN (Integer/parseInt (read-line))]
    (dotimes [i surfaceN]
      (let [; landX: X coordinate of a surface point. (0 to 6999)
            ; landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
            [landX landY] (map #(Integer/parseInt %) (filter #(not-empty %) (str/split (read-line) #" ")))]))
    (while true
      (let [; hSpeed: the horizontal speed (in m/s), can be negative.
            ; vSpeed: the vertical speed (in m/s), can be negative.
            ; fuel: the quantity of remaining fuel in liters.
            ; rotate: the rotation angle in degrees (-90 to 90).
            ; power: the thrust power (0 to 4).
            [X Y hSpeed vSpeed fuel rotate power] (map #(Integer/parseInt %) (filter #(not-empty %) (str/split (read-line) #" ")))]
        
        ; If speed larger than landing speed, set power to max.
        (if (> vSpeed -39) (output "0 0") (output "0 4"))
      )
    )
  )
)
