import subprocess

# Applescripts that controls the GUI and chooses the desired file path
def chooseFile(fullPath):
    args = []
    args.append("osascript")
    args.append("-e")
    args.append('tell application "System Events"')
    args.append("-e")
    args.append("delay 1")
    args.append("-e")
    args.append('keystroke "G" using {command down,  shift down}')
    args.append("-e")
    args.append("delay 2")
    args.append("-e")
    args.append("keystroke " + '"' + fullPath + '"')
    args.append("-e")
    args.append("delay 1")
    args.append("-e")
    args.append("keystroke return")
    args.append("-e")
    args.append("delay 1")
    args.append("-e")
    args.append("keystroke return")
    args.append("-e")
    args.append("end tell")
    subprocess.call(args)
