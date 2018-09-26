# Defold API VS Code Snippets

You can download the snippets from [marketplace](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets)

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

## Recommended Settings & Extension

Add .script files to your settings

```json
"files.associations": {
        "*.script": "lua",
        "*.gui_script": "lua",
        "*.render_script": "lua"
      }
 ```   

Install [vscode-lua](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua): Lua for Visual Studio Code. Provides Intellisense and Linting for Lua in VSCode


## Json Parser

I build this snippet with a simple [Python script](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). It parses all json files from api docs and converts them to single snippet file. It is available [here](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). Feel free to update it. 
