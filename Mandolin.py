Linear_4ths = ['Bx', 'Ex', 'Ax', 'Dx', 'Gx', 'Cx', 'Fx', 'B#', 'E#', 'A#', 'D#', 'G#', 'C#', 'F#', 'B', 'E', 'A', 'D', 'G', 'C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb', 'Bbb', 'Ebb', 'Abb', 'Dbb', 'Gbb', 'Cbb', 'Fbb']
Run = True
while Run == True:
    Note_Choice = raw_input("Enter a note: ")                                  # Assigns a note to a variable.
    if Note_Choice in Linear_4ths:    
        Index = Linear_4ths.index(Note_Choice)                                 # Finds the index of that note.
        Slice = []                                                             # Makes an empty list to hold the notes of a scale.
        Mode_Choice = raw_input('Enter a scale: ')
        Known_Mode = True
        if Mode_Choice == 'maj':        
            for note in Linear_4ths[Index - 5:Index + 2]:                      # Fills empty list with notes. 73625(ROOT)4
                Slice.append(note)
        elif Mode_Choice == 'mix':
            for note in Linear_4ths[Index - 4:Index + 3]:                      # Fills empty list with notes.
                Slice.append(note)
        elif Mode_Choice == 'dor':
            for note in Linear_4ths[Index - 3:Index + 4]:                      # Fills empty list with notes.
                Slice.append(note)
        elif Mode_Choice == 'min':
            for note in Linear_4ths[Index - 2:Index + 5]:                      # Fills empty list with notes. 25(ROOT)4b7b3b6
                Slice.append(note)
        else:
            Known_Mode = False      
            print 'Please use...\n"maj" for Major\n"min" for Minor\n"dor" for Dorian\n"mix" for Mixolydioan.'
        if Known_Mode == True:
        
            C,Cs,D,Ds,E,F,Fs,G,Gs,A,As,B = '-','-','-','-','-','-','-','-','-','-','-','-'

            if 'Bx' in Slice:
                Cs = 'Bx'
            if 'Ex' in Slice:
                Fs = 'Ex'
            if 'Ax' in Slice:
                B  = 'Ax' 
            if 'Dx' in Slice:
                E  = 'Dx'
            if 'Gx' in Slice:
                A  = 'Gx'
            if 'Cx' in Slice:
                D  = 'Cx'
            if 'Fx' in Slice:
                G  = 'Fx'
            if 'B#' in Slice:
                C  = 'B#'
            if 'E#' in Slice:
                F  = 'E#'
            if 'A#' in Slice:
                As = 'A#' 
            if 'D#' in Slice:
                Ds = 'D#'
            if 'G#' in Slice:
                Gs = 'G#'
            if 'C#' in Slice:
                Cs = 'C#'
            if 'F#' in Slice:
                Fs = 'F#'
            if 'B' in Slice:
                B  = 'B'
            if 'E' in Slice:
                E  = 'E'
            if 'A' in Slice:
                A  = 'A'
            if 'D' in Slice:
                D  = 'D'
            if 'G' in Slice:
                G  = 'G'
            if 'C' in Slice:
                C  = 'C'
            if 'F' in Slice:
                F  = 'F'
            if 'Bb' in Slice:
                As = 'Bb'
            if 'Eb' in Slice:
                Ds = 'Eb'
            if 'Ab' in Slice:
                Gs = 'Ab'
            if 'Db' in Slice:
                Cs = 'Db'
            if 'Gb' in Slice:
                Fs = 'Gb'
            if 'Cb' in Slice:
                B  = 'Cb'
            if 'Fb' in Slice:
                E  = 'Fb'
            if 'Bbb' in Slice:
                A  = 'Bbb'
            if 'Ebb' in Slice:
                D  = 'Ebb'
            if 'Abb' in Slice:
                G  = 'Abb'
            if 'Dbb' in Slice:
                C  = 'Dbb'
            if 'Gbb' in Slice:
                F  = 'Gbb'
            if 'Cbb' in Slice:
                As  = 'Cbb'
            if 'Fbb' in Slice:
                Ds  = 'Fbb'
            
            Variables = [C,Cs,D,Ds,E,F,Fs,G,Gs,A,As,B]

            E = [4,5,6,7,8,9,10,11]
            A = [9,10,11,0,1,2,3,4]
            D = [2,3,4,5,6,7,8,9]
            G = [7,8,9,10,11,0,1,2]

            E_String = [Variables[i] for i in E]
            E_String.insert(1,'|')
            print''.join(E_String[:1]),'       '.join(E_String[1:])

            A_String = [Variables[i] for i in A]
            A_String.insert(1,'|')
            print''.join(A_String[:1]),'       '.join(A_String[1:])

            D_String = [Variables[i] for i in D]
            D_String.insert(1,'|')
            print''.join(D_String[:1]),'       '.join(D_String[1:])

            G_String = [Variables[i] for i in G]
            G_String.insert(1,'|')
            print''.join(G_String[:1]),'       '.join(G_String[1:])
        
    elif Note_Choice == "q":
        Run = False
    else:
        print 'RAWR!!!!!!\nPlease choose an uppercase note: A,B,C,D,E,F,G.\nIf you would like to use a sharp or flat, follow the note with "#" or "b".\nEnter "q" to quit.'