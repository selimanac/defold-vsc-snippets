# Defold API VS Code Snippets


Full api snippets for [Defold Engine](https://www.defold.com/).

All functions, messages and properties are separated and includes all of the parameters. 

Snippet will generate the messages:

`play_sound ->  msg.post(receiver, "play_sound", {[delay], [gain]})`

`model_animation_done -> msg.post(receiver, "model_animation_done", {animation_id, playback})`

Properties are with quotation marks:

`"scale"`

## Release Notes

### 1.0.0

Initial release based on API version 1.2.137. 



-----------------------------------------------------------------------------------------------------------

## Json Parser

I build this snippet with a simple Python script. It parses all json files from api docs and converts them to single snippet file. It is available here. Feel free to update it. 

