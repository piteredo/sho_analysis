from cmath import pi
from music21 import *

pitchL1 = ["C#5", "E5", "B3", "G#4"]
pitchL2 = ["B4"]
pitchL3 = ["A4"]
pitchL4 = ["D5", "D4", "A3"]
pitchR1 = ["C#4", "G4", "F#5"]
pitchR2 = ["E4", "F#4", "C5"]
fingers = [pitchL1, pitchL2, pitchL3, pitchL4, pitchR1, pitchR2]
meas = stream.Measure()
d = duration.Duration('whole')

for finger_1_num in range(len(fingers)-2):
    note_list_1 = fingers[finger_1_num]
    for note_1_num in range (len(note_list_1)):
        note_1 = note.Note(note_list_1[note_1_num])
        note_1.duration = d

        for finger_2_num in range(finger_1_num+1, len(fingers)-1):
            note_list_2 = fingers[finger_2_num]
            for note_2_num in range (len(note_list_2)):
                note_2 = note.Note(note_list_2[note_2_num])
                note_2.duration = d

                for finger_3_num in range(finger_2_num+1, len(fingers)):
                    note_list_3 = fingers[finger_3_num]
                    for note_3_num in range (len(note_list_3)):
                        note_3 = note.Note(note_list_3[note_3_num])
                        note_3.duration = d

                        notes = []
                        notes.append(note_1)
                        notes.append(note_2)
                        notes.append(note_3)
                        c = chord.Chord(notes)
                        meas.append(c)

meas.show('musicxml')


