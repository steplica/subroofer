# subroofer

This project was made with [Stefan Aleksic](https://github.com/ColdSauce).

subroofer was a creation inspired by my rather noisy and rude upstairs neighbors. The overall scheme is an iOS application that lets you choose a sound frequenecy and a duration that it will be played (<i>forever</i> being an option). It then sends an HTTP request to a Flask application running on a raspberry pi. 

Finally, the application utilizes the sound library in Pygame to generate a custom frequency, and then it outputs (loudly) through a subwoofer. Duct taped to the ceiling.
