Module Player
    Sub Main () 
        ' game loop
        While True
            ' Define required variables.
            Dim max_i as Integer
            Dim max_v as Integer
            max_i = 0
            max_v = 0

            ' Find the index of the max height and store in max_index.
            For i as Integer = 0 To 7
                Dim mountainH as Integer
                mountainH = Console.ReadLine() 
                If (mountainH > max_v)
                    max_v = mountainH
                    max_i = i
                End If
            Next

            ' Output the index of the mountain to fire on.
            Console.WriteLine(max_i) 
        End While
    End Sub
End Module
