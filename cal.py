import subprocess

def calling():
	# Jitsi Meet App ID
	app_id = "ibiognfelmneebngbnbeonnllapmffmb"

	# Jitsi Meet room name
	room_name = "Pi"

	# Command to open Jitsi Meet with the specified room name
	command = ["/usr/bin/chromium", "--profile-directory=Default", f"--app-id={app_id}", f"https://meet.jit.si/{room_name}"]

	# Launch Jitsi Meet directly into the "Pi" room
	process = subprocess.Popen(command)
