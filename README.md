# Defold API Snippets for Visual Studio Code

Full api snippets for [Defold Engine](https://www.defold.com/) is available on [marketplace](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets).  All functions, messages and properties are separated, includes parameters and brief descriptions.

**Marketplace:** https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets  
**Defold Community:** https://www.defold.com/community/projects/121893/  
**Github:** https://github.com/selimanac/defold-vsc-snippets

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

### 1.1.7
* API version 1.2.156

### 1.1.6
* API version 1.2.149

### 1.1.5
* API version 1.2.147


### 1.1.4

* API version 1.2.138
* Missing functions, methods and properties are added properly.
* Properties added to the body.

(Sorry for the version numbering, vsce publish minor cause this )

![focus](https://forum.defold.com/uploads/default/original/2X/0/0529da4cc744d5a2c8b08c9d45807cd86f370c64.png)

### 1.0.2

* Missing functions, methods and properties are added.
* Args added to the list.

### 1.0.0

* Initial release based on API version 1.2.137. 

## Recommended Settings & Extension

### Add .script files to your settings

```json
"files.associations": {
        "*.script": "lua",
        "*.gui_script": "lua",
        "*.render_script": "lua"
      }
 ```   

### You can use those extensions with this snippet:

* [Lua language support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=keyring.Lua)
* [Lint Lua scripts with luac or luajit](https://marketplace.visualstudio.com/items?itemName=dcr30.lualinter)
* [Improved Lua syntax highlighting](https://marketplace.visualstudio.com/items?itemName=jep-a.lua-plus)
* [Support go to defintion and List Document Symbols.](https://marketplace.visualstudio.com/items?itemName=xxxg0001.lua-for-vscode)
* [Intellisense and Linting for Lua](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua)


## Json Parser

I build this snippet with a simple [Python script](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). It parses all json files from api docs and converts them to single snippet file. It is available [here](https://github.com/selimanac/defold-vsc-snippets/blob/master/scr/defold_json_convert.py). Feel free to update it. 
