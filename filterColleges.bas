Sub filterColleges()

Dim Rng, Cell As Range
Dim RowCount, i As Integer

Set Rng = Range("A1")
Rng.Select
Range(Selection, Selection.End(xlDown)).Select

RowCount = Selection.Rows.Count

For i = 1 To RowCount:
    If InStr(1, Rng, "university") = 0 And InStr(1, Rng, "University") = 0 And InStr(1, Rng, "College") = 0 And InStr(1, Rng, "college") = 0 Then
        Set Rng = Rng.Offset(1, 0)
        Rng.Offset(-1, 0).EntireRow.Delete
    Else
        Set Rng = Rng.Offset(1, 0)
    End If
Next

End Sub
