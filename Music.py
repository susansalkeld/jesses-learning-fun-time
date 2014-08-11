Linear_4ths = ['Bx', 'Ex', 'Ax', 'Dx', 'Gx', 'Cx', 'Fx', 'B#', 'E#', 'A#', 'D#', 'G#', 'C#', 'F#', 'B', 'E', 'A', 'D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb', 'Bbb', 'Ebb', 'Abb', 'Dbb', 'Gbb', 'Cbb', 'Fbb']
Run = True
while Run ==True:
    Note_Choice = raw_input("Enter a note: ")                                  # Assigns a note to a variable.
    if Note_Choice in Linear_4ths:    
        Index = Linear_4ths.index(Note_Choice)                                 # Finds the index of that note.
        Linear_Diatonic_Steps = []                                             # Makes an empty list to hold the notes of a scale.
        for note in Linear_4ths[Index - 5:Index + 2]:                          # Fills empty list with notes. 73625(ROOT)4
            Linear_Diatonic_Steps.append(note)
        Re_Order = [5,3,1,6,4,2,0,5]                                           # Makes a list to reprisent the new order of the notes, low to high rather than in 4ths.
        Linear_Diatonic_Steps = [Linear_Diatonic_Steps[i] for i in Re_Order]   # Reorders notes low to high.
        for note in Linear_Diatonic_Steps:                                     # Prints notes.
            print note
    elif Note_Choice == "q":
        Run = False
    else:
        print 'RAWR!!!!!!\nPlease choose an uppercase note: A,B,C,D,E,F,G.\nIf you would sharp or flat, follow the note with "#" or "b".\nEnter "q" to quit.'