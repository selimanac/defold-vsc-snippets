# Defold API VS Code Snippets

Full api snippets for [Defold Engine](https://www.defold.com/).

You can download the snippets from [marketplace](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets). Initial release is based on API version 1.2.137. All functions, messages and properties are separated and includes all the parameters. 

![vcs](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/vcs.png)

------------

### Ordered Tabstops

![Ordered Tabstops](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/orderedtabstops.gif)

### Message Generation



`play_sound ->  msg.post(receiver, "play_sound", {[delay], [gain]})`

`model_animation_done -> msg.post(receiver, "model_animation_done", {animation_id, playback})`

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/input_focus.gif)

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/clear_color.gif)

### Properties with quotation marks

`"scale"`

## Release Notes

### 1.0.2

Missing functions, methods and properties are added.

Args added to the list.

### 1.0.0

Initial release based on API version 1.2.137. 

## Recommended Settings & Extension

Install [vscode-lua](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua): Lua for Visual Studio Code. Provides Intellisense and Linting for Lua in VSCode

Add .script files to your settings

```json
"files.associations": {
        "*.script": "lua",
        "*.gui_script": "lua",
        "*.render_script": "lua"
      }
 ```   




## Json Parser

I build this snippet with a simple [Python script](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). It parses all json files from api docs and converts them to single snippet file. It is available [here](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). Feel free to update it. 
